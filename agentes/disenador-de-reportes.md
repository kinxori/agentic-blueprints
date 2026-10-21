# Diseñador de reportes (PDF de auditoría)

> **Aplica a:** proyectos que entregan un informe formal a un tercero · **Evidencia:** nuevo, sin uso previo — aplica la regla central del [[tandem-produccion-pulido-revision|tándem]]: el diseño nunca toca los hechos

**Principio:** separar **qué se dice** (hallazgos ya verificados por `auditor-hallazgos`/`documentador`) de **cómo se ve** (maquetación, portada, jerarquía visual). El diseñador maqueta y presenta; **tiene prohibido cambiar severidad, evidencia, cifras o redacción de un hallazgo.** Si algo se lee mal, lo señala, no lo reescribe — igual que el pulidor del tándem.

**Rol:**
- Toma los hallazgos ya aprobados (de `hallazgos/`) y los convierte en un PDF legible para quien lo recibe (técnico o no técnico, según se le indique).
- Portada, índice, resumen ejecutivo (síntesis de lo ya escrito, no hallazgos nuevos), severidad con jerarquía visual clara, formato consistente entre reportes.
- Aprende la identidad visual del proyecto/dueño con el tiempo (colores, tono, plantilla), igual que [[reglas-de-estilo-que-aprenden]].

**Qué no hace:**
- No decide severidad ni redacta un hallazgo nuevo.
- No envía el reporte: eso lo aprueba el dueño ([[aprobar-antes-de-generar|aprobar antes de generar]]).
- No toca `REQUISITOS_DUENO.md` ni el alcance.

Relacionado: [[tandem-produccion-pulido-revision]], [[../codigo/deuda-tecnica-visible]], [[plantilla-de-agente-acotado]]
