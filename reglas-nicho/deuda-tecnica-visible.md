# Deuda técnica visible y ADR vivos

> **Aplica a:** cualquier proyecto que dure más de unas semanas · **Evidencia:** fuerte (KinxoBot `deuda-tecnica.md`; HeyBob `decisiones.md`)

**1. Una tabla de deuda técnica** (tema · detalle · prioridad), revisada antes de cada versión menor. Incluye por qué *no* se hizo todavía. Ejemplos: módulos de ~900 líneas, estado global en `app/`, pruebas estilo script, un radar pausado sin decidir si se retira, comentarios con etapas viejas.

**2. ADR corto y fechado.** Formato: Estado · Contexto · Opciones (2–3, con las descartadas) · Decisión · Consecuencias (+/−) · Personal/Público · Cuándo revisar. Ejemplo de buen ADR corto: «La v5 es un producto nuevo y aislado de la v4» (alternativas descartadas: seguir sobre el archivo de 3 700 líneas, borrar v4, hacer fork).

**3. Jerarquía explícita cuando hay contradicción:** (1) decisiones del dueño, (2) el ADR más reciente sobre el tema, (3) el código (sus comentarios citan ADR y fecha del hallazgo).

**4. Los documentos se desincronizan; hay que detectarlo.** En HeyBob el índice de ADR solo listaba hasta el 0009 y el ADR decía SDK 36 mientras el código usaba 35 («diferencia sin registrar»). Un índice único + un chequeo mecánico (script que compare ADR/índice/versiones) lo evita. Los estados («propuesto» vs «aplicado») deben actualizarse al implementar.

**5. Enmiendas visibles:** cuando una decisión cambia (confirmación previa → aviso + 5 s), se anota como enmienda fechada en el ADR original, no se reescribe la historia.

**6. Retirar lo que no tiene evidencia de ventaja.** El auto trader demo se eliminó (ADR-0006) tras medir 3 meses contra el azar: menos código y superficie de error. Si algún día se reconstruye, con el mismo modelo de seguridad.

Relacionado: [[../metodologias/contexto-persistente-entre-sesiones]], [[../anti-patrones/entregar-apagado-y-sin-fusionar]]
