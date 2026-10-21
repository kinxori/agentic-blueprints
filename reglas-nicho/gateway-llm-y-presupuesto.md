# Gateway único de LLM con alias, respaldo y presupuesto

> **Aplica a:** todo proyecto que llame a un LLM de pago · **Evidencia:** fuerte (KinxoBot `llm_gateway`; HeyBob ADR-0005/0010)

**Principio:** todas las llamadas al LLM salen por **un solo punto**. El dominio conoce un puerto (`LlmClient`), no el SDK del proveedor.

**Qué debe tener el gateway:**
- **Niveles de modelo / alias por tarea** (router barato, agente, razonador, voz) en un archivo de configuración; cambiar de modelo sin redeploy ni tocar el dominio. Los IDs nunca viven en el código de negocio.
- **Plazo explícito por nivel**, **un reintento** y **un respaldo** a otro modelo ante 429/503/timeout (no ante 400 «reales»).
- **Presupuesto con corte propio**: por módulo/día (KinxoBot) o por mes con ventana de 30 días corridos (HeyBob, 20 MXN). Los presupuestos de la nube **solo alertan, no cortan**. El tope se lee en caliente en cada llamada y avisa una vez (80 % / agotado).
- **Medición**: cada llamada registra tokens, razonamiento, caché, latencia y costo; el costo lo calcula el adaptador, no el dominio.
- **Un modelo sin precio verificado devuelve costo 0, no una adivinanza** («medir, no asumir»).
- **Validación de sobrescrituras** de alias: solo familias permitidas.
- **Estado opaco del proveedor** (p. ej. *thought signatures* de Gemini): reenviarlo íntegro, sin reconstruirlo; un test de contrato reproduce el 400 si se omite.
- **Imágenes:** fijar siempre la resolución más baja que alcance.
- **Verificar precios y IDs** en la documentación oficial antes de fijarlos; cambian rápido.

**Evaluaciones con LLM real**: aparte de la suite normal, caras, y una vez por cambio de prompt ([[../codigo/pruebas-sin-red-con-dobles]]).

**Enrutar sin LLM cuando se pueda:** reglas fijas (regex ancladas) con batería de evaluación y **cero rutas equivocadas** exigido por una prueba. KinxoBot añade un **router que aprende**: propone reglas semanalmente, las prueba en **modo sombra** y las activa solo con ≥7 días y ≥10 mensajes con 100 % de coincidencia; solo herramientas de lectura.

Relacionado: [[orquestador-en-codigo-llm-propone]], [[../datos/mongo-estado-externo-y-reclamos-atomicos]]
