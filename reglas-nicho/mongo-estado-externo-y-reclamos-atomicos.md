# Estado en base externa: proceso reiniciable, reclamos atómicos, acceso por dueño

> **Aplica a:** servicios que deben sobrevivir reinicios (bots, jobs, backends pequeños) · **Evidencia:** media-fuerte (KinxoBot; leído en docs y código, sin auditar el esquema completo)

**Principio:** todo el estado vive en la base (Mongo Atlas en KinxoBot); el proceso puede reiniciarse en cualquier momento sin perder nada: pendientes, memoria y órdenes en vuelo están en la base.

**Patrones observados:**
- **Un módulo dueño por colección.** Documentar una tabla colección → qué guarda → quién tiene el acceso. El chat nunca consulta a mano.
- **Reclamo atómico de un solo uso** para confirmaciones (`find_one_and_delete` sobre el pendiente): el botón no se puede pulsar dos veces ni con confirmación vencida. Los pendientes caducan (15 min en memoria).
- **Idempotencia con índices únicos:** `hash` único para noticias y `slot` único para briefings (`reclamar_briefing` con máximo de intentos y espera de reintento), así un reinicio no duplica envíos.
- **Estados explícitos para operaciones de dinero** (`enviando → abierta → cerrada / no_ejecutada`) y un job de vigilancia que repara lo que quedó a medias tras un reinicio.
- **Configuración estricta persistida:** solo el booleano `True` enciende algo; un valor basura no activa nada; claves viejas se ignoran.
- **Telemetría como datos:** `llm_calls` (tokens, caché, ms, costo) y `turnos` permiten decidir con números (p. ej. «2 días mirando /costos» antes de activar algo).
- **Versiones compatibles sobre las mismas colecciones:** la v5 usa las colecciones de la v4, así se cambia de versión sin migrar; el histórico antiguo queda de solo lectura.
- **Índices creados al arrancar** (`asegurar_indices_*`), no a mano.

**Pendiente de validar (no hay evidencia):** política de retención/TTL, tamaño de colecciones de telemetría, y backups. Aquí hay un hueco: el material no los documenta.

Relacionado: [[../arquitectura/gateway-llm-y-presupuesto]], [[../seguridad/interruptores-con-confirmacion]], [[../agentes/agente-base-de-datos-propuesto]]
