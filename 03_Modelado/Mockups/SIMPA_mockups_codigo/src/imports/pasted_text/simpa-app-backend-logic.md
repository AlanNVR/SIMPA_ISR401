Ya tengo el sistema de diseño y las 8 pantallas de "SIMPA" construidas (Login, Dashboard, Análisis IA, Registro de Labor, Detalle de Lote, Mapa GPS, Reportes, Alertas). NO cambies el diseño visual. Ahora necesito que le des funcionamiento real y completo: lógica de datos, interactividad, navegación, validaciones y persistencia, usando Supabase como backend. Implementa todo lo siguiente:

=== 1. AUTENTICACIÓN Y ROLES ===
- Login real contra tabla "usuarios" (usuario, contraseña hasheada, nombre completo, rol: Administrador/Supervisor/Operario, lote(s) asignado(s) si aplica).
- Al enviar el formulario: validar campos no vacíos → si están vacíos, mostrar error inline por campo ("Este campo es obligatorio"). Si la combinación usuario/contraseña no existe, mostrar el mensaje de error general debajo del botón sin decir cuál de los dos falló (seguridad).
- Botón mostrar/ocultar contraseña cambia el type del input en tiempo real, sin recargar ni perder el valor.
- Botón "Ingresar" muestra estado de carga (deshabilitado + spinner) mientras valida contra la base de datos.
- "¿Olvidaste tu contraseña?" abre flujo de recuperación: pide correo/usuario registrado, genera token temporal, y (para esta fase) muestra confirmación de "enlace enviado" — no requiere envío real de correo, simularlo con un mensaje de éxito.
- Al autenticar correctamente: guardar sesión (rol, nombre, id de usuario) en estado global/local storage de la app, redirigir a Dashboard, y aplicar de inmediato las restricciones de menú y accesos según el rol.
- Cerrar sesión: limpia el estado global y vuelve a Login, sin dejar datos sensibles en caché.
- Reglas de permisos por rol (aplican a TODA la navegación, no solo visualmente sino bloqueando el acceso):
  - Administrador: acceso total a las 8 pantallas, ve todos los lotes y todos los trabajadores.
  - Supervisor: acceso a Dashboard, Análisis IA, Registro de Labor, Detalle de Lote, Mapa GPS, Reportes y Alertas, pero filtrado solo a los lotes que tiene asignados.
  - Operario: acceso solo a Dashboard (simplificado), Análisis IA, Registro de Labor y Mapa GPS (su propio recorrido); si intenta entrar por URL/navegación directa a Reportes o gestión de lotes, redirigir a Dashboard con un aviso de "No tienes permiso para ver esta sección".

=== 2. DASHBOARD ===
- Las 4 tarjetas KPI deben calcularse dinámicamente desde datos reales:
  - Lotes activos = conteo de lotes con estado "activo" en la tabla "lotes" (filtrado por lotes del rol si es Supervisor/Operario).
  - Labores del día = conteo de registros en "labores" con fecha = hoy.
  - Alertas abiertas = conteo de "alertas" con estado distinto de "atendida".
  - Producción estimada = suma/proyección calculada desde los últimos registros de producción por lote.
- El panel de "Alertas recientes" lista las últimas 5 alertas ordenadas por fecha descendente, actualizándose en tiempo real (o al refrescar) si llega una alerta nueva; cada ítem es clickeable y navega al detalle de esa alerta en la pantalla de Alertas con el ítem preseleccionado.
- Los accesos rápidos deben ejecutar la navegación real a cada pantalla y, si corresponde, prellenar contexto (ej. "Registrar labor" abre el formulario ya con la fecha de hoy).
- El contenido completo de esta pantalla (KPIs, accesos rápidos, alertas visibles) debe cambiar automáticamente según el rol de la sesión activa, sin necesidad de que el usuario elija nada manualmente.

=== 3. ANÁLISIS DE IMAGEN CON IA ===
- El selector de lote solo debe listar los lotes visibles para el rol actual.
- Al activar la cámara (o simular captura si no hay acceso real a cámara del dispositivo, permitir subir una imagen de galería como alternativa funcional): mostrar la vista previa capturada.
- El "indicador de calidad" debe evaluarse (aunque sea con una heurística simple: resolución/brillo de la imagen, o un valor simulado aleatorio consistente) y mostrar el estado correspondiente (Buena/Mejorar iluminación/Muy borrosa) ANTES de habilitar el botón "Analizar".
- El botón "Analizar" debe estar deshabilitado si: no hay foto capturada, o la calidad es insuficiente (<70%), o no se seleccionó lote/tipo de análisis.
- Al presionar "Analizar": enviar la imagen (o sus metadatos) a la función/endpoint de análisis (puede ser una función simulada que devuelve un diagnóstico de un set predefinido de condiciones con su nivel de confianza y recomendación, mientras no haya modelo real de IA conectado), mostrar estado de carga, y luego renderizar la tarjeta de resultado con diagnóstico, % de confianza, severidad y recomendación.
- Botón "Guardar en historial del lote": inserta el registro (foto, diagnóstico, fecha, usuario, lote) en la tabla "diagnosticos", y debe reflejarse inmediatamente en la pestaña "Diagnósticos" del Detalle de ese Lote.
- Botón "Repetir análisis": limpia el resultado y la foto, vuelve al estado de cámara lista, sin perder el lote/tipo seleccionado.

=== 4. REGISTRO DE LABOR ===
- Selector de lote y tipo de labor: al elegir "Polinización" como tipo, mostrar/habilitar la sección de "Estados de antesis" y el bloque de conteo GPS; para otros tipos de labor, ocultar esos bloques específicos de polinización.
- Campo "Fecha": autocompletado con la fecha actual, editable con date picker, sin permitir fechas futuras.
- Campo "Responsable": autocompletado con el nombre del usuario en sesión; si el rol es Administrador/Supervisor, permitir buscar y reasignar a otro trabajador desde la tabla "usuarios" filtrada por rol Operario.
- Estados de antesis: cada chip es seleccionable (toggle), y junto a cada uno debe poder ingresarse la cantidad de inflorescencias contadas en ese estado; validar que al menos un estado tenga cantidad > 0 antes de permitir guardar.
- "Verificación visual": switch que, al activarse, habilita el botón para adjuntar foto de evidencia (obligatorio si el switch está activo).
- "Conteo automático por GPS": al presionar "Iniciar recorrido", activar el seguimiento de ubicación (usar geolocalización del navegador/dispositivo si está disponible; si no, simular incremento automático del contador cada pocos segundos como fallback), mostrar el contador de flores/palmas polinizadas incrementándose en vivo y la distancia recorrida acumulada; al presionar "Detener y guardar", congelar los valores y anexarlos automáticamente al formulario.
- Botón "Guardar labor": valida que todos los campos obligatorios estén completos (lote, tipo, fecha, responsable, y los específicos de polinización si aplica), inserta el registro en la tabla "labores" con todos sus datos relacionados (antesis, verificación, conteo GPS), muestra confirmación de éxito (toast) y limpia el formulario o redirige al Dashboard.

=== 5. DETALLE DE LOTE ===
- La ficha superior y las métricas rápidas deben calcularse/leerse en tiempo real desde las tablas relacionadas (lotes, labores, diagnósticos, producción) para el lote seleccionado.
- Las pestañas deben cargar sus datos de forma perezosa (lazy) al hacer clic, no todo de una vez:
  - Labores: trae el historial real de la tabla "labores" filtrado por ese lote, ordenado por fecha, con paginación si supera cierto número de registros.
  - Monitoreo: grafica variables (humedad, temperatura, sanidad) desde una tabla de mediciones periódicas del lote.
  - Diagnósticos: lista los registros generados desde la pantalla de Análisis IA para ese lote (con su foto, diagnóstico y fecha), clickeables para ver el detalle completo.
  - Análisis (Suelo/Foliar/Clima): sub-tabs que cargan cada uno su tabla de parámetros más reciente, comparando contra rango óptimo (resaltar en rojo/ámbar los valores fuera de rango).
  - Línea de tiempo: construida dinámicamente a partir de la fecha de siembra y las etapas fenológicas registradas, marcando automáticamente en qué etapa está el lote hoy según la fecha actual.
- Si el rol es Supervisor u Operario y el lote no les pertenece, bloquear el acceso a este detalle y mostrar mensaje de "No autorizado".

=== 6. MAPA GPS DE RECORRIDOS Y POLINIZACIÓN ===
- Cargar los recorridos reales guardados desde los registros GPS de la pantalla de Registro de Labor (ruta como serie de coordenadas con timestamp), no datos falsos fijos.
- Filtros funcionales: por trabajador (multi-selección, oculta/muestra su ruta y sus puntos en el mapa al togglear), por lote (recentra y filtra el mapa a los límites de ese lote), por rango de fechas (recalcula qué recorridos se muestran).
- El "Panel de totales de polinización" debe sumar en tiempo real: total de flores polinizadas hoy (según filtros aplicados), compararlo contra la meta diaria configurada (mostrar % de avance en la barra de progreso), y generar el ranking de trabajadores ordenado por productividad descendente.
- Al seleccionar un solo trabajador en el filtro, su ruta se resalta con opacidad completa y color distintivo, mientras el resto de rutas se atenúan (opacidad reducida) sin desaparecer del todo.

=== 7. REPORTES ===
- Al cambiar el "Tipo de reporte" (Producción/Labores/Personal/Alertas), la pantalla debe recargar dinámicamente qué gráficos y qué columnas de tabla se muestran, consultando las tablas correspondientes.
- El selector de período (hoy/semana/mes/personalizado) debe filtrar la consulta a la base de datos por el rango de fechas real; "personalizado" habilita un rango de fechas manual.
- Los filtros adicionales (lote, trabajador, tipo de labor) deben combinarse con el tipo de reporte y el período para armar la consulta final (AND lógico entre todos los filtros activos).
- Botón "Generar reporte": ejecuta la consulta con los filtros actuales, muestra estado de carga, y actualiza gráficos + tabla consolidada con los resultados reales; si no hay datos para los filtros elegidos, mostrar estado vacío claro ("No hay datos para el período seleccionado").
- Botón "Exportar": genera el archivo real en el formato elegido (PDF o Excel) con los datos actualmente mostrados en la tabla (respetando los filtros aplicados), y dispara la descarga.
- La tabla consolidada debe permitir ordenar por columna (clic en encabezado) y paginar si hay más de 15-20 filas.

=== 8. ALERTAS ===
- Las alertas deben generarse automáticamente por reglas de negocio, no solo manualmente, por ejemplo:
  - Un diagnóstico de IA con severidad "crítica" crea automáticamente una alerta vinculada a ese lote.
  - Un parámetro de suelo/foliar/clima fuera del rango óptimo genera una alerta.
  - Ausencia de labores registradas en un lote por más de X días genera una alerta de seguimiento.
- Filtros funcionales (severidad, estado, lote, buscador de texto) deben combinarse y filtrar la lista en tiempo real conforme se van aplicando/quitando.
- Al seleccionar una alerta de la lista, cargar su detalle completo (descripción, lote, evidencia, acción recomendada, historial de cambios de estado) en el panel de detalle.
- Botón "Marcar como atendida": actualiza el estado de la alerta en la base de datos a "Atendida", registra quién la atendió y cuándo, actualiza visualmente el badge sin recargar toda la pantalla, y refleja el cambio también en el contador de "Alertas abiertas" del Dashboard.
- Si no hay alertas que cumplan los filtros seleccionados, mostrar el estado vacío "No hay alertas pendientes" en vez de una lista en blanco.

=== 9. REGLAS TRANSVERSALES ===
- Toda acción que modifique datos (guardar labor, guardar diagnóstico, marcar alerta atendida, etc.) debe mostrar una notificación tipo toast de confirmación de éxito o de error.
- Los formularios no deben permitir enviarse con campos obligatorios vacíos; resaltar en rojo el/los campos faltantes al intentar enviar.
- Los datos deben persistir entre sesiones (recargar la página no debe perder lo ya guardado) usando la base de datos, no solo estado en memoria.
- La navegación entre pantallas debe respetar el historial (botón "atrás" del navegador funciona correctamente) y mantener los filtros/selecciones activas al volver a una pantalla ya visitada en la misma sesión cuando sea razonable (ej. volver a Reportes mantiene el último tipo/período consultado).
- Manejar y mostrar de forma clara los estados de carga (loading) y error de red/base de datos en cada pantalla que consulta datos.