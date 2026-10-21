# Capas con regla de dependencias comprobada por una prueba

> **Aplica a:** cualquier proyecto con código · **Evidencia:** fuerte (KinxoBot ADR-0005; HeyBob principio 4)

**Principio:** divide el código en capas y fija la regla «una capa solo importa hacia abajo». Esa regla no vive en un documento: la comprueba una prueba que falla.

**Estructura de referencia (KinxoBot, Python):**
`infra` (BD, gateway LLM, config, logs; no importa nada) → módulos de negocio (`market`, `trading`, `chat`, `journal`…) → `tools` → `app` (único que ensambla todo). Los módulos de negocio **no conocen el canal de entrada** (Telegram): reciben por parámetro lo que necesitan (cliente, reloj, LLM).

**Equivalente en HeyBob (Kotlin/Android):** `core:*` es Kotlin puro y no importa `android.*` ni conoce Gemini; los **adaptadores** sí (puertos y adaptadores). Un solo proceso por límite de RAM.

**Qué comprueba `test_arquitectura.py` (copiar la idea):**
- Ningún módulo importa una capa superior (análisis con `ast`, incluye imports dentro de funciones).
- Nada importa código muerto/de versiones anteriores ni `tests/`/`scripts/`.
- **Solo el paquete autorizado contiene llamadas peligrosas** (p. ej. API de órdenes de dinero).
- Cada paquete y módulo tiene un docstring que dice qué es.
- Tope de tamaño por módulo (2 000 líneas); la deuda queda a la vista.

**Beneficios observados:** estructura legible por un agente nuevo, pruebas sin red, imposible que negocio dependa de la app.

**Costos reconocidos:** `app/` terminó con estado global por módulo (deuda anotada); varios módulos de ~900 líneas.

Relacionado: [[../seguridad/pruebas-de-seguridad-en-codigo]], [[../eficiencia/estructura-de-carpetas-por-rol]], [[../codigo/deuda-tecnica-visible]]
