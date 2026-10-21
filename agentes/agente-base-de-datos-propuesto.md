# Agente de base de datos (propuesto)

> **Aplica a:** proyectos con persistencia · **Evidencia:** hipótesis (no existe aún; derivado de [[../datos/mongo-estado-externo-y-reclamos-atomicos]] y [[../datos/sqlite-local-migraciones-y-llaves]])

**Rol:** revisar y diseñar el modelo de datos; no escribe lógica de negocio.

**Checklist derivado de lo que funcionó:**
1. ¿Cada colección/tabla tiene un módulo dueño y está documentada?
2. ¿Las confirmaciones usan reclamo atómico de un solo uso y caducan?
3. ¿Hay claves/índices únicos para idempotencia (reinicio no duplica envíos)?
4. ¿Los estados de operaciones de dinero son explícitos y hay un job que repara los intermedios?
5. ¿La configuración se lee de forma estricta, con default explícito?
6. ¿Hay telemetría de costos/latencia consultable?
7. ¿Migraciones: esquema exportado y prueba de migración desde la versión anterior?
8. ¿Retención/TTL, backups y tamaño de colecciones de telemetría definidos? (**sin evidencia previa**)
9. ¿Secretos fuera de la base y de los logs?

**Herramientas:** Read, Grep, Glob (solo lectura). **Salida:** veredicto + hallazgos con severidad + NO VERIFICADO, igual que [[../plantilla-de-proyecto/.claude/agents/calidad-codigo]].

**Antes de darlo por bueno:** probarlo sobre KinxoBot o HeyBob y comparar contra lo que ya se sabe.
