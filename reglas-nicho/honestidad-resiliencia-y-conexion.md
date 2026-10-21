# Honestidad ante lo no verificado, resiliencia y código sin conectar

> **Aplica a:** agentes que actúan y reportan resultados · **Evidencia:** fuerte (HeyBob ADR-0010/0012)

**1. No decir «Listo» sin evidencia.** Tres resultados de verificación: `VERIFIED → OK`, `UNKNOWN → OK_UNVERIFIED`, `FAILED → VERIFY_FAILED`. Con `UNKNOWN` no se bloquea ni se reintenta (no hay evidencia de fallo), pero el mensaje al usuario ya no es «Listo». Excepción razonable: si `UNKNOWN` es un límite de la plataforma (p. ej. no se puede leer un temporizador), usar plantilla neutra para no generar alarma sin motivo. Nació del reporte «me dijiste que sí y no creaste el evento».

**2. El reintento es una decisión de seguridad.** Solo el orquestador marca un resultado como reintentable, y solo si el fallo es transitorio **y** ningún efecto irreversible o persistente pudo haberse ejecutado. Máximo un reintento; nunca un comando con varias rutas (repetiría las que sí salieron bien).

**3. Supervisor de tareas con vida propia.** Las tareas viven en un scope de aplicación, no de la pantalla (la tarea moría con la Activity); una a la vez; el kill switch registra el trabajo **antes** de arrancarlo; cualquier excepción no prevista se reporta como `INTERNAL_ERROR` en vez de tumbar el proceso.

**4. Ningún fallo de red sin atrapar.** Se halló un código de resultado `NETWORK` con plantilla pero que **nada producía**: un fallo real de red habría tumbado la corrutina. Solución: un envoltorio único (`llmGuarded`) en las llamadas al LLM, sin tragarse `CancellationException`. Distinguir «tope de gasto alcanzado» de «fallo de red».

**5. Código construido pero sin conectar.** `AuditLog` y `totalCostSince` llevaban días escritos **sin un solo llamador**; faltaba cableado, no infraestructura. Ante «falta una función», buscar primero si ya existe sin usar. Y al revés: al cerrar una tarea, comprobar que lo nuevo esté conectado.

**6. Capacidad lista ≠ capacidad activada.** Un tope por tarea ($0.05) se construyó y probó pero se dejó **desactivado** porque el dueño no confirmó el valor: no se activa por inferencia.

**7. Verificar sospechas antes de «arreglar».** La sospecha de un esquema vacío se comprobó con una llamada real y se descartó como bug; quedó solo una nota para cuando algo lea esa clave.

Relacionado: [[../metodologias/evidencia-sobre-inferencia]], [[politica-de-riesgo-en-codigo]]
