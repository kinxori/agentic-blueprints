# Cuestionario de entorno al arrancar

> **Aplica a:** cualquier proyecto nuevo, sobre todo si usa agentes o conectores · **Evidencia:** nuevo, sin uso previo (hipótesis)

**Principio:** antes de hacer cualquier trabajo real, la primera acción en un proyecto nuevo es que el asistente detecte qué tiene disponible en esa sesión (conectores, herramientas, skills) y le pregunte al dueño, uno por uno, cuáles quiere habilitar para cada agente. No se asume ni se activa nada solo.

**Por qué:** los conectores y las herramientas disponibles dependen de la cuenta y la sesión, no del archivo del agente ([[../agentes/disenador-de-reportes]] es el ejemplo: solo sirve con un conector de diseño, pero cuál exista varía). Preguntarlo al inicio evita que un agente se quede corto de herramientas sin que nadie lo note, o que use un conector que el dueño no quería dar por hecho.

**Cómo aplicarlo:**
1. Al abrir el proyecto por primera vez, antes de tocar archivos: listar qué conectores/herramientas/skills aparecen disponibles en esa sesión.
2. Para cada agente de la plantilla, decir qué le serviría de lo detectado (igual que la tabla de [[../proyectos-arrancados/estudio-ciberseguridad/ARRANQUE|un ARRANQUE.md]] ya hace a mano) y preguntar: ¿lo habilito para este agente, sí o no?
3. **También decir lo que NO está disponible pero ayudaría.** No limitarse a lo detectado: si un agente se beneficiaría claramente de un conector o skill que el dueño no tiene activado (p. ej. un conector de diseño para el `disenador`, uno de hojas de cálculo para análisis de datos), nombrarlo explícitamente con el beneficio concreto, para que el dueño decida si vale la pena activarlo. No se da por hecho que «si no está, no se menciona».
4. Guardar la respuesta en el `tools:` de cada agente y, si aplica, en `REQUISITOS_DUENO.md` (qué conectores están permitidos y cuáles no, por si hay datos sensibles de por medio).
5. Repetir el chequeo si el dueño agrega o quita un conector después; no asumir que sigue igual.
6. **Este cuestionario es una sección fija de todo `ARRANQUE.md`** (ver [[../ARRANQUE-PLANTILLA]]), no un paso aparte: así cada proyecto nuevo arranca con la decisión de herramientas ya resuelta, y el formato se compara y mejora de un proyecto al siguiente.

**Cuándo no aplica:** proyectos de un solo agente sin conectores, donde no hay nada que detectar.

Relacionado: [[../agentes/plantilla-de-agente-acotado]], [[aprobar-antes-de-generar]]
