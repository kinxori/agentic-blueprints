# Glosario de requisitos del dueño (`REQUISITOS_DUENO.md`)

> **Aplica a:** cualquier proyecto · **Evidencia:** fuerte

**Principio:** mantener un archivo con los requisitos del dueño y un glosario de términos con significado exacto. Elimina malas interpretaciones de raíz.

**Por qué:** términos ambiguos producían decisiones equivocadas. Ejemplos del origen: «crypto trade = LIVE», «recap = 08:00/20:00», «RVOL apagado».

**Cómo aplicarlo:**
- Crear `REQUISITOS_DUENO.md` al arrancar el proyecto.
- Cada término ambiguo se define en una línea, con valor concreto (horas, modo, estado on/off).
- Incluir el estado por defecto de cada interruptor (encendido/apagado) y quién lo cambia.
- Todo agente lo lee antes de actuar; ante un conflicto, el glosario manda.
- Cuando el dueño use un término nuevo o lo redefina, se actualiza el glosario en el momento.

**Cuándo no aplica:** proyectos de un solo uso sin vocabulario propio.
