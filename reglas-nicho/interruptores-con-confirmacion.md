# Interruptores con confirmación por botón

> **Aplica a:** acciones irreversibles o con dinero · **Evidencia:** fuerte

**Principio:** todo lo que mueve dinero o tiene efecto irreversible está detrás de un interruptor explícito, apagado por defecto, y activarlo exige confirmación por botón del dueño.

**Por qué:** separa «el sistema funciona» de «el sistema actúa». Permite probar sin riesgo y da al dueño el control final.

**Cómo aplicarlo:**
- Modos claramente nombrados (p. ej. simulación vs LIVE) y definidos en el glosario.
- Estado por defecto: apagado/simulación.
- Cambiar a modo real = botón de confirmación, solo dueño, un solo uso (ver [[pruebas-de-seguridad-en-codigo]]).
- Registrar quién y cuándo lo activó.

**Defaults (KinxoBot ADR-0004, nació de ese error):** lo de **uso diario va encendido**; lo que **mueve dinero va apagado**. Los interruptores son estrictos (solo `True` enciende), se guardan en la base para cambiarlos en caliente, los riesgosos piden botón aunque el valor venga en el mensaje, y el aviso de arranque lista lo encendido (una prueba falla si se agrega un interruptor sin anunciarlo). Detalle: [[../arquitectura/politica-de-riesgo-en-codigo]].

**Ojo (anti-patrón del origen):** «entregar todo apagado» sin avisar es también un fallo. Ver [[../anti-patrones/entregar-apagado-y-sin-fusionar]].
