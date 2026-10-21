# Estructura de carpetas legible a primera vista

> **Aplica a:** cualquier proyecto · **Evidencia:** media

**Principio:** una convención simple que un agente nuevo entienda sin explicación.

**Ejemplo del origen (producción de contenido):**
- `Investigacion/<tipo>/NN-slug/` y `Produccion/<tipo>/NN-slug/` con **el mismo número** en ambos lados.
- Tipos numerados por separado.
- `assets/` solo para recursos de edición.
- Credenciales/claves fuera de la carpeta sincronizada (p. ej. fuera de Drive) y una carpeta `_shared` para futuras APIs.

**Ejemplo (apps):** `referencias/`, `interno/`, `docs/` según quién ve qué.

**Cómo aplicarlo:** documentarla en el `CLAUDE.md` ([[../metodologias/contexto-persistente-entre-sesiones]]) y hacerla cumplir con una prueba si el proyecto es de código ([[../seguridad/pruebas-de-seguridad-en-codigo]]).

**Nota:** automatizar con scripts de edición de apps de escritorio (p. ej. portada vía ExtendScript) funcionó pero fue lo más lento; evaluar el costo antes.
