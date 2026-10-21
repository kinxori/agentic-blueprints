# KinxoBot

Asistente de trading por Telegram para un solo dueño. Opera su cuenta real de Binance Futures (solo con botón de confirmación), lleva diario de operaciones, mide tendencias/noticias y gestiona un portafolio en IBKR (paper).

**Stack:** Python 3.11, Gemini (chat + function calling) como LLM gateway con control de costo, MongoDB Atlas (estado), despliegue en Railway (Docker).

**Arquitectura:** capas con dependencia de una sola vía — `infra` → negocio (`market`, `trading`, `chat`, `journal`, `intel`, `equities`) → `tools` → `app`, verificada por `tests/test_arquitectura.py`. Solo el paquete `trading/` puede enviar órdenes reales.

**Seguridad:** el bot nunca ejecuta una orden sola; la propone y solo sale si el dueño pulsa "Confirmar", con límites en código, SL/TP obligatorios y reclamo atómico de un solo uso.

Lecciones que deja: capas con dependencias comprobadas, orquestador donde el LLM propone y el código decide, gateway de LLM con presupuesto, estado externo en Mongo con reclamos atómicos.
