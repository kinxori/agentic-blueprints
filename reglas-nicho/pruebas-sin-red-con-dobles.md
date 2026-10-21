# Pruebas sin red ni dinero; evals con LLM aparte

> **Aplica a:** cualquier proyecto con APIs de pago o dinero · **Evidencia:** fuerte (KinxoBot ADR-0007; HeyBob `pruebas.md`)

**Principio:** las pruebas deben poder correr siempre, en cualquier máquina y sin gastar. Todo módulo de negocio recibe sus dependencias por parámetro; las pruebas usan **dobles** (broker simulado, Telegram falso, base en memoria, gateway LLM con guion).

**Estructura de la suite:**
- Suite normal: segundos, sin red; es la puerta del preflight. Incluye las **pruebas de seguridad** (inyección, dueño único, un solo uso, límites).
- **Evals con LLM real** en carpeta aparte: cuestan centavos y se corren a propósito, una vez por cambio de prompt.
- **Pruebas adversariales**: texto de pantalla que intenta dar órdenes; fixtures capturados de una app sandbox.
- **Pruebas de contrato** del adaptador (reproducen el 400 si se omite estado opaco).
- Al agregar una herramienta o interruptor, la prueba **obliga a clasificarla/anunciarla** (`test_nucleo_chat`, `test_arranque`): la prueba es el recordatorio.

**Trampas reales (HeyBob):**
- Un `.env` con llave hace que `./gradlew test` **llame a la API real** y cueste dinero. Las pruebas en vivo deben requerir un opt-in explícito, no la mera presencia de la llave.
- Pruebas con audio real están en `.gitignore`: un clon limpio las falla. Documentarlo o aportar datos sintéticos.
- **Sin integración continua:** las pruebas solo corren si alguien las lanza.
- Las cifras de conteo de pruebas pueden quedar viejas: decir de qué build y fecha son, y que no se volvieron a correr.
- Módulos sin pruebas (UI, acciones, wake word) deben aparecer listados como tales.

**Deuda reconocida (KinxoBot):** pruebas estilo script (`check(...)`) en lugar de funciones pytest, lo que impide ejecutar un caso suelto.

Relacionado: [[../eficiencia/puerta-de-preproduccion]], [[../seguridad/pruebas-de-seguridad-en-codigo]], [[../arquitectura/gateway-llm-y-presupuesto]]
