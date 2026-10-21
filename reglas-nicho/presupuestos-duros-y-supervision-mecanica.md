# Presupuestos duros y supervisión mecánica de planes

> **Aplica a:** trabajo delegado a sesiones/agentes en la nube · **Evidencia:** media (KinxoBot `REGLAS_PROCESO.md`; efectividad no medida más allá del Plan 3)

**Principio:** avanzar sin quemar tokens, créditos ni tiempo, y sin que nada llegue a producción sin verificarse. Los límites son **numéricos y se supervisan con un script**, no con un agente.

**Reglas del origen:**
- Un plan por sesión. Commits de **punto de control** `chk(planN): paso K — t=<min> agentes=<n>` al terminar cada paso.
- Tiempo: 3 h por plan (a las 2 h se entrega lo que haya). Sub-agentes: 0 por defecto, máximo 3 y de uno en uno; auditorías en una sola pasada. Un comando sin avance en 5 min se detiene.
- Dinero: revisar el panel de créditos tras cada plan; si uno gastó más de $25 no se lanza el siguiente hasta entender por qué. Pruebas con LLM real: una vez por plan y en local.
- **Supervisor mecánico** (`supervisor_nube.py`): lee los puntos de control y commits en GitHub y alerta por exceso de tiempo, falta de avance, 3 rondas de auditoría, >3 sub-agentes o falta de checkpoints. Cero tokens.
- **Verificación local en una orden** (`verificar_plan.py <rama>`): pruebas sin red + supervisor. Nada se fusiona sin bloque final y verificación en verde.
- **Activación de a uno**, esperando evidencia entre cada uno (2 días mirando costos antes del siguiente). Dinero real: solo con la primera orden hecha junto al dueño.
- **Quién hace qué:** nube = código y pruebas sin red; local = verificación con llaves, fusión, despliegue; dueño = luz verde e interruptores.
- Un plan que incumple se corta y se relanza con alcance reducido. Se registra la decisión (el Plan 3 lanzó **121 sub-agentes** antes de conocer las reglas; se aceptó porque relanzar costaba más).

**Matiz:** las reglas aparecieron *después* del gasto; y el supervisor-agente no atrapó los errores de entrega ([[../anti-patrones/procesos-no-sustituyen-revision-humana]]). Lo que sí es verificable por máquina (tiempo, sub-agentes, checkpoints) conviene mecanizarlo.

Relacionado: [[../eficiencia/puerta-de-preproduccion]], [[aprobar-antes-de-generar]]
