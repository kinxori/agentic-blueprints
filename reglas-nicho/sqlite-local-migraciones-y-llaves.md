# Datos locales en el dispositivo: Room, migraciones a mano y llaves

> **Aplica a:** apps móviles con datos propios · **Evidencia:** media (HeyBob, `arquitectura.md` y ADR-0005/0007)

**Principio:** en una app personal, todo vive en el teléfono; la base local guarda la **auditoría** y de ella se calcula el gasto.

**Lo que hizo HeyBob:**
- Room `version = 8`, **migraciones escritas a mano de la 1 a la 8** para no perder la auditoría (de ella sale el gasto mensual).
- Tablas por función: `audit_entries` (nodo, modelo, tokens, costo, latencia), `episodes` + `episode_steps` (cada tarea y sus pasos), `lessons`, `user_rules`, `memory_items`, `conversation_turns`, `connectors`.
- Ajustes en DataStore. **Llave del LLM cifrada con AES/GCM directo contra Android Keystore** (se evitó una librería de seguridad por dudas de mantenimiento); nunca en el APK, repo ni logs.
- **Aprendizaje sin LLM donde se pueda:** un `LessonMiner` deriva lecciones de los episodios; el LLM solo escribe la receta final.

**Riesgo anotado (observación, no verificada con el equipo):** «sin esquema exportado» implica que las migraciones a mano no se pueden comprobar automáticamente. Para un proyecto nuevo, exportar el esquema y probar cada migración sobre una base de la versión anterior.

**Para la fase pública:** la llave en el dispositivo solo es aceptable en modo personal; después, proxy propio.

Relacionado: [[mongo-estado-externo-y-reclamos-atomicos]], [[../agentes/agente-base-de-datos-propuesto]]
