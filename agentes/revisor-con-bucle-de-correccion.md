# Revisor entrenado con bucle: revisa → corrige → revisa → entrega

> **Aplica a:** contenido, imagen, lotes de salida · **Evidencia:** fuerte

**Principio:** un agente revisor revisa cada lote **antes** de que lo vea el dueño, y se entrena con el feedback acumulado de este.

**Por qué:** en el origen (`revisor-naturalidad`), tras entrenarlo con correcciones (complexión de los personajes, vehículos y objetos coherentes con la época, comer con cubiertos correctos, no repetir caras) atrapa esos errores solo. El valor está en el bucle, no en una sola pasada.

**Cómo aplicarlo:**
1. Generador produce el lote.
2. Revisor lo audita contra su lista de reglas.
3. Se corrige lo detectado y se **vuelve a revisar**.
4. Solo entonces se envía al dueño.
5. Cada corrección del dueño que se escapó → nueva regla en el archivo del revisor ([[reglas-de-estilo-que-aprenden]]).

Contrasta con los revisores sin entrenar ni bucle, de valor aún no demostrado: ver [[../anti-patrones/procesos-no-sustituyen-revision-humana]].
Usa la [[plantilla-de-agente-acotado]].
