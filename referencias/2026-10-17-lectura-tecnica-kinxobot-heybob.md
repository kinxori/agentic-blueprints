# Fuente 6 — Lectura técnica de KinxoBot y HeyBob (2026-10-17)

**Leído:** ADR 0001–0007, `docs/arquitectura/*`, `REGLAS_PROCESO.md`, `operacion/seguridad.md`, `tests/test_arquitectura.py`, cabeceras de `infra/database.py` y `infra/llm_gateway.py` (KinxoBot); `arquitectura.md`, `decisiones.md`, `pruebas.md` y las secciones de decisión de los ADR 0005, 0006, 0009, 0010 y 0012 (HeyBob); los 5 agentes técnicos de KinxoBot y `system-design` de HeyBob.

**No leído / no verificado:**
- El código de implementación completo (KinxoBot ≈14 300 líneas; HeyBob módulos Kotlin). Las lecciones vienen de la documentación y de fragmentos de código, no de una auditoría de código.
- ADR 0002–0004, 0007, 0008, 0011, 0013–0018 de HeyBob (solo sus resúmenes en `decisiones.md`), `PLANES_EJECUCION_NUBE.md`, `datos` reales de las bases.
- No se corrieron pruebas ni se comprobó que la documentación coincida con el código (los propios docs de HeyBob señalan desfases).

**Lecciones derivadas:** [[../arquitectura/capas-con-dependencias-comprobadas]], [[../arquitectura/orquestador-en-codigo-llm-propone]], [[../arquitectura/politica-de-riesgo-en-codigo]], [[../arquitectura/gateway-llm-y-presupuesto]], [[../arquitectura/honestidad-resiliencia-y-conexion]], [[../datos/mongo-estado-externo-y-reclamos-atomicos]], [[../datos/sqlite-local-migraciones-y-llaves]], [[../codigo/pruebas-sin-red-con-dobles]], [[../codigo/deuda-tecnica-visible]], [[../metodologias/presupuestos-duros-y-supervision-mecanica]], [[../agentes/agente-base-de-datos-propuesto]].
