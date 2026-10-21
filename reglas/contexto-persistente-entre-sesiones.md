# Contexto persistente entre sesiones

> **Aplica a:** cualquier proyecto · **Evidencia:** media

**Principio:** que cualquier sesión nueva arranque con el contexto completo sin depender de la memoria del chat.

**Cómo aplicarlo:**
- **`CLAUDE.md` general del flujo** en la raíz del proyecto: roles, reglas, estructura y enlaces. Pendiente en el proyecto de origen; hacerlo desde el día 1.
- **Memoria por tipo:** perfil, feedback, estado, referencias; con índice de una línea por archivo ([[memoria-de-correcciones]]).
- **ADR vivo** con secciones fechadas para decisiones.
- **Carpetas con rol:** `referencias/` (material del dueño), `interno/` (desarrollo, no se publica), `docs/` (público).

Relacionado: [[../eficiencia/estructura-de-carpetas-por-rol]], [[ciclo-corto-de-iteracion]]
