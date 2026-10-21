# Anti-patrón: confiar en el agente supervisor y en reglas de proceso

> **Aplica a:** cualquier proyecto con agentes · **Evidencia:** fuerte

**Qué pasó:** el agente supervisor y las reglas de proceso **no evitaron** los peores errores. Los corrigió el ojo del dueño.

**Lección:** un supervisor automático no reemplaza la revisión humana. Los controles que sí funcionaron fueron **mecánicos** (scripts, pruebas), no instrucciones de proceso.

**Cómo aplicarlo:**
- Convertir cada regla de proceso importante en una comprobación automática (ver [[../eficiencia/puerta-de-preproduccion]]).
- Mantener al dueño en el lazo en los puntos de decisión.
- Tratar el valor de los agentes de revisión como **no probado** hasta medirlo (ver pendientes en el README).
