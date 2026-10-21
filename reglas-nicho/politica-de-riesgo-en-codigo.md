# Política de riesgo en código (PolicyEngine)

> **Aplica a:** agentes que ejecutan acciones con efectos (dispositivos, cuentas, dinero) · **Evidencia:** fuerte (HeyBob ADR-0006; KinxoBot `ordenes-reales`)

**Principio:** un módulo determinista, sin dependencias de plataforma y con pruebas masivas, aprueba, degrada o bloquea cada acción. **El modelo puede subir el riesgo de una acción, nunca bajarlo:** `riesgo = max(declarado por el LLM, heurística, categoría de app, sensibilidad de pantalla, procedencia)`.

**Niveles (adaptables):**
| Nivel | Qué es | Fricción |
|---|---|---|
| R0 | Lectura | Ninguna |
| R1 | Reversible/local | Aviso + ventana de cancelación (HeyBob: 5 s) |
| R2 | Enviar, pagar, borrar | Confirmación explícita por toque físico |
| R3 | Prohibido | Bloqueo sin anulación en la sesión |

**Reglas que valió la pena fijar:**
- **Denylist siempre gana a la allowlist.** Detección por paquete **y** por categoría/pantalla (los paquetes nuevos no estarán en la lista).
- **Una app fuera de la allowlist solo se añade desde ajustes**, nunca con un «¿te dejo?» a mitad de una tarea (sería un vector de inyección).
- **Procedencia de parámetros** (`USER`, `SKILL`, `SCREEN`): un R2 con parámetros de pantalla no declarados exige advertencia o se bloquea.
- **Confirmación:** UI propia, texto derivado de la acción estructurada (no de prosa del LLM), token de un solo uso ligado al hash de la acción, fuera del alcance del propio agente de accesibilidad.
- **Voz no aprueba R2 por defecto** (un micrófono no distingue al dueño de una TV o del TTS propio). Excepción solo como ajuste opt-in apagado de fábrica y con frase ligada al hash de la acción.
- **Presupuestos por tarea** (pasos, tiempo, costo, ráfaga) evaluados en cada acción.
- **Kill switch** en dos niveles (cancelar la tarea; deshabilitar el servicio).
- **Reintentos:** nunca de R2 ni de efectos persistentes.

**Lección sobre probar defensas:** `noHideDescendants` bloqueaba `performAction`, pero `dispatchGesture` (coordenadas de pantalla) **lo rodeaba**. La regla quedó «validada solo frente a performAction». Prueba cada defensa contra la vía de ataque realista, no solo contra la obvia, y deja registrado lo que quedó *sin* cubrir.

**Modelo en KinxoBot (dinero):** límites todos en código (símbolos permitidos, apalancamiento, margen por orden y total, SL/TP obligatorios, una orden por símbolo, cierre de emergencia si algo falla tras abrir, vigilancia cada minuto) y llave sin permiso de retiros. Cliente de **solo lectura con lista blanca de métodos** para todo lo que no sea operar.

Relacionado: [[orquestador-en-codigo-llm-propone]], [[../seguridad/interruptores-con-confirmacion]], [[../seguridad/reglas-para-agentes-con-acceso-real]]
