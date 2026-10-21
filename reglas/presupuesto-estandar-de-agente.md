# Presupuesto estándar por agente (una pasada, límite de líneas)

> **Aplica a:** todo agente de revisión/auditoría, en cualquier proyecto · **Evidencia:** fuerte (los 4 agentes técnicos de KinxoBot comparten este patrón, no documentado como regla general hasta ahora)

**Principio:** cada agente de revisión declara, desde su cabecera, un presupuesto duro: **una sola pasada, cero sub-agentes, salida corta, y no repetir lo que ya cubrió un script mecánico.** No es una sugerencia de estilo, es lo que evita que una revisión se vuelva una conversación larga y cara.

**Por qué ahora es regla general y no solo de seguridad:** los agentes `calidad-codigo`, `seguridad-fugas`, `supervisor-cumplimiento` y `revisor-notificaciones` de KinxoBot comparten exactamente este molde y funcionaron bien ([[../agentes/inventario-de-agentes-existentes]]), pero la plantilla general no lo tenía como default — solo como ejemplo suelto en esos agentes. Generalizarlo ahorra tokens en **cualquier** proyecto nuevo, no solo en los de seguridad.

**El molde (copiar en todo agente de revisión nuevo):**
```
Presupuesto duro: una sola pasada, cero sub-agentes, máximo ~10 minutos y ~40 líneas de respuesta.
No repitas lo que ya confirmó `scripts/preflight.sh` ([[../eficiencia/puerta-de-preproduccion]]).
No modifiques archivos (si es de solo lectura).
Si hay más de 3 hallazgos críticos, detente y repórtalos: no sigas buscando.
```

**Excepciones explícitas** (agentes que SÍ necesitan más espacio, y por qué):
- `arquitecto-sistemas`: diseña, no audita; necesita explorar y escribir documentos largos.
- `mentor`: es conversación de enseñanza, no una revisión de una pasada.
- `project-manager` y `disenador`: su trabajo normal es iterativo (organizar, maquetar), no una auditoría puntual.

**Cómo aplicarlo:** al crear un agente nuevo de revisión/auditoría, copiar el molde de presupuesto en su cabecera por defecto, y solo quitarlo si el rol del agente justifica lo contrario (como los de arriba).

Relacionado: [[plantilla-de-agente-acotado]], [[../eficiencia/puerta-de-preproduccion]], [[../metodologias/presupuestos-duros-y-supervision-mecanica]]
