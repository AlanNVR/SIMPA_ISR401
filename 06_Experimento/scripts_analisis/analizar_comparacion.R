#!/usr/bin/env Rscript

suppressPackageStartupMessages(
  library(ordinal)
)

entrada <- "07_Datos/datos_procesados/puntuaciones_experimento_con_origen.csv"

salida_descriptiva <- "07_Datos/resultados/comparacion_descriptiva.csv"
salida_modelos <- "07_Datos/resultados/modelo_ordinal_mixto.csv"
salida_resumen <- "07_Datos/resultados/resumen_modelos_ordinales.txt"
salida_meta <- "07_Datos/resultados/metadatos_modelo_ordinal.txt"

dimensiones <- c("COM", "AMB", "VER", "COR", "CON")
origenes <- c("Humano", "LLM")

if (!file.exists(entrada)) {
  stop(paste("No existe:", entrada))
}

datos <- read.csv(
  entrada,
  stringsAsFactors = FALSE,
  check.names = FALSE
)

columnas_necesarias <- c(
  "evaluador",
  "requisito",
  "origen",
  "id_original",
  "dimension",
  "puntuacion",
  "orden"
)

faltantes <- setdiff(columnas_necesarias, names(datos))

if (length(faltantes) > 0) {
  stop(
    paste(
      "Faltan columnas:",
      paste(faltantes, collapse = ", ")
    )
  )
}

if (nrow(datos) != 750) {
  stop(
    paste(
      "Se esperaban 750 filas y hay",
      nrow(datos)
    )
  )
}

if (any(is.na(datos$puntuacion))) {
  stop("Existen puntuaciones vacias.")
}

if (any(!datos$puntuacion %in% 1:5)) {
  stop("Existen puntuaciones fuera del rango 1-5.")
}

if (!setequal(unique(datos$dimension), dimensiones)) {
  stop("Las dimensiones no coinciden con las cinco esperadas.")
}

if (!setequal(unique(datos$origen), origenes)) {
  stop("Los origenes no coinciden con Humano y LLM.")
}

if (length(unique(datos$evaluador)) != 3) {
  stop("Se esperaban exactamente 3 evaluadores.")
}

if (length(unique(datos$requisito)) != 50) {
  stop("Se esperaban exactamente 50 requisitos.")
}

# Humano sera la categoria de referencia.
datos$origen <- factor(
  datos$origen,
  levels = c("Humano", "LLM")
)

datos$evaluador <- factor(datos$evaluador)
datos$requisito <- factor(datos$requisito)

# ------------------------------------------------------------
# Estadistica descriptiva
# ------------------------------------------------------------

descriptivos <- list()
contador <- 1

for (dimension in dimensiones) {

  for (origen in origenes) {

    sub <- datos[
      datos$dimension == dimension &
      datos$origen == origen,
    ]

    if (nrow(sub) != 75) {
      stop(
        paste(
          dimension,
          origen,
          "deberia tener 75 observaciones y tiene",
          nrow(sub)
        )
      )
    }

    if (length(unique(sub$requisito)) != 25) {
      stop(
        paste(
          dimension,
          origen,
          "deberia contener 25 requisitos."
        )
      )
    }

    x <- sub$puntuacion

    descriptivos[[contador]] <- data.frame(
      dimension = dimension,
      origen = origen,
      n_observaciones = length(x),
      n_requisitos = length(unique(sub$requisito)),
      media = round(mean(x), 6),
      mediana = round(median(x), 6),
      desviacion_tipica = round(sd(x), 6),
      q1 = round(
        as.numeric(
          quantile(x, 0.25, names = FALSE)
        ),
        6
      ),
      q3 = round(
        as.numeric(
          quantile(x, 0.75, names = FALSE)
        ),
        6
      ),
      iqr = round(IQR(x), 6),
      stringsAsFactors = FALSE
    )

    contador <- contador + 1
  }
}

descriptivos <- do.call(
  rbind,
  descriptivos
)

# ------------------------------------------------------------
# Modelos ordinales mixtos
#
# puntuacion ~ origen + (1 | evaluador) + (1 | requisito)
#
# Humano = referencia
# origenLLM = efecto de LLM frente a Humano
# ------------------------------------------------------------

resultados <- list()
resumenes <- character()

for (dimension in dimensiones) {

  sub <- datos[
    datos$dimension == dimension,
  ]

  if (nrow(sub) != 150) {
    stop(
      paste(
        dimension,
        "deberia tener 150 observaciones y tiene",
        nrow(sub)
      )
    )
  }

  sub$puntuacion_ord <- ordered(
    sub$puntuacion,
    levels = sort(unique(sub$puntuacion))
  )

  advertencias <- character()

  ajuste <- tryCatch(
    withCallingHandlers(
      clmm(
        puntuacion_ord ~ origen +
          (1 | evaluador) +
          (1 | requisito),
        data = sub,
        link = "logit",
        Hess = TRUE,
        nAGQ = 1,
        na.action = na.fail
      ),
      warning = function(w) {
        advertencias <<- c(
          advertencias,
          conditionMessage(w)
        )
        invokeRestart("muffleWarning")
      }
    ),
    error = function(e) e
  )

  resumenes <- c(
    resumenes,
    "",
    paste(
      "============================================================"
    ),
    paste("DIMENSION:", dimension),
    paste(
      "============================================================"
    )
  )

  if (inherits(ajuste, "error")) {

    resultados[[dimension]] <- data.frame(
      dimension = dimension,
      contraste = "LLM vs Humano",
      beta = NA,
      error_estandar = NA,
      z = NA,
      p_crudo = NA,
      p_holm = NA,
      odds_ratio = NA,
      or_ic95_inferior = NA,
      or_ic95_superior = NA,
      aic = NA,
      logLik = NA,
      estado = "ERROR",
      stringsAsFactors = FALSE
    )

    resumenes <- c(
      resumenes,
      paste(
        "ERROR:",
        conditionMessage(ajuste)
      )
    )

    next
  }

  tabla_coef <- coef(
    summary(ajuste)
  )

  if (!"origenLLM" %in% rownames(tabla_coef)) {
    stop(
      paste(
        "No se encontro el coeficiente origenLLM en",
        dimension
      )
    )
  }

  beta <- tabla_coef[
    "origenLLM",
    "Estimate"
  ]

  se <- tabla_coef[
    "origenLLM",
    "Std. Error"
  ]

  z <- tabla_coef[
    "origenLLM",
    "z value"
  ]

  p <- tabla_coef[
    "origenLLM",
    "Pr(>|z|)"
  ]

  limite_inf_beta <- beta - 1.96 * se
  limite_sup_beta <- beta + 1.96 * se

  resultados[[dimension]] <- data.frame(
    dimension = dimension,
    contraste = "LLM vs Humano",
    beta = beta,
    error_estandar = se,
    z = z,
    p_crudo = p,
    p_holm = NA_real_,
    odds_ratio = exp(beta),
    or_ic95_inferior = exp(limite_inf_beta),
    or_ic95_superior = exp(limite_sup_beta),
    aic = AIC(ajuste),
    logLik = as.numeric(logLik(ajuste)),
    estado = if (
      length(advertencias) == 0
    ) "SIN_ADVERTENCIAS" else "CON_ADVERTENCIAS",
    stringsAsFactors = FALSE
  )

  if (length(advertencias) > 0) {
    resumenes <- c(
      resumenes,
      "",
      "ADVERTENCIAS:",
      paste0("- ", advertencias)
    )
  }

  resumenes <- c(
    resumenes,
    "",
    capture.output(
      summary(ajuste)
    )
  )
}

resultados <- do.call(
  rbind,
  resultados
)

# Holm-Bonferroni exclusivamente sobre los cinco
# contrastes del efecto de origen.
validos <- !is.na(
  resultados$p_crudo
)

resultados$p_holm[validos] <- p.adjust(
  resultados$p_crudo[validos],
  method = "holm"
)

resultados$significativo_holm <- ifelse(
  is.na(resultados$p_holm),
  NA,
  resultados$p_holm < 0.05
)

# Redondeo solo para archivos de reporte.
columnas_numericas <- c(
  "beta",
  "error_estandar",
  "z",
  "p_crudo",
  "p_holm",
  "odds_ratio",
  "or_ic95_inferior",
  "or_ic95_superior",
  "aic",
  "logLik"
)

for (columna in columnas_numericas) {
  resultados[[columna]] <- round(
    resultados[[columna]],
    6
  )
}

dir.create(
  "07_Datos/resultados",
  recursive = TRUE,
  showWarnings = FALSE
)

write.csv(
  descriptivos,
  salida_descriptiva,
  row.names = FALSE,
  fileEncoding = "UTF-8"
)

write.csv(
  resultados,
  salida_modelos,
  row.names = FALSE,
  fileEncoding = "UTF-8",
  na = ""
)

writeLines(
  c(
    "MODELOS ORDINALES MIXTOS — RQ1",
    "",
    paste(
      "Formula:",
      "puntuacion ~ origen + (1 | evaluador) + (1 | requisito)"
    ),
    "Enlace: logit acumulativo / probabilidades proporcionales",
    "Referencia de origen: Humano",
    "Contraste: LLM vs Humano",
    "Correccion multiple: Holm-Bonferroni sobre cinco efectos de origen",
    resumenes
  ),
  salida_resumen,
  useBytes = TRUE
)

writeLines(
  c(
    "Metadatos del analisis ordinal mixto",
    "-----------------------------------",
    paste(
      "R:",
      R.version.string
    ),
    paste(
      "ordinal:",
      as.character(
        packageVersion("ordinal")
      )
    ),
    paste(
      "Sistema:",
      paste(
        Sys.info()[c("sysname", "release", "machine")],
        collapse = " | "
      )
    ),
    paste(
      "Fecha de ejecucion:",
      format(
        Sys.time(),
        "%Y-%m-%d %H:%M:%S %z"
      )
    ),
    "",
    "Modelo principal:",
    "puntuacion ~ origen + (1 | evaluador) + (1 | requisito)",
    "",
    "Respuesta: ordinal",
    "Escala original: 1-5",
    "Efecto fijo: origen",
    "Referencia: Humano",
    "Interceptos aleatorios: evaluador y requisito",
    "Enlace: logit",
    "nAGQ: 1",
    "Correccion multiple: Holm",
    "alpha: 0.05",
    "",
    "Nota:",
    "Un odds ratio > 1 indica desplazamiento estimado hacia",
    "puntuaciones ordinales mayores para LLM respecto a Humano."
  ),
  salida_meta,
  useBytes = TRUE
)

cat("Analisis RQ1 completado.\n\n")

cat("Resultados principales:\n")
print(
  resultados[
    ,
    c(
      "dimension",
      "beta",
      "p_crudo",
      "p_holm",
      "odds_ratio",
      "or_ic95_inferior",
      "or_ic95_superior",
      "estado"
    )
  ],
  row.names = FALSE
)

cat("\nArchivos generados:\n")
cat("-", salida_descriptiva, "\n")
cat("-", salida_modelos, "\n")
cat("-", salida_resumen, "\n")
cat("-", salida_meta, "\n")
