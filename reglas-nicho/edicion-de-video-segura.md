# Edición de video/proyectos de escritorio sin romper nada

> **Aplica a:** edición de video/escritorio · **Evidencia:** media

**Reglas del origen (Premiere), generalizables a cualquier editor:**
- Trabajar sobre una **copia** (`04.3`) y dejar la versión previa (`04.2`) intacta.
- Usar un proyecto de referencia y copiar sus capas de diseño.
- **Bloquear** las pistas base para que «Seleccionar todo» tome solo las capas de diseño.
- Leer el archivo de proyecto descomprimido como XML para entender su estructura sin tocar nada.

**No funcionó:** controlar la app por pantalla con atajos de teclado (se cruzan con otros paneles). Usar **menús** y estados bloqueados es más fiable; si hay API/script, mejor aún (aunque costó iteraciones).

Relacionado: [[estructura-de-carpetas-por-rol]]
