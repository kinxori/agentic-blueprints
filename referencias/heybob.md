# HeyBob

Asistente personal para Android que entiende lo que le pides, habla en tiempo real y opera cualquier app por el servicio de accesibilidad (como lo haría una persona), con una política de seguridad determinista que el modelo no puede saltarse. App personal: sin cuentas, sin servidor propio, sin suscripción; todo vive en el teléfono.

**Stack:** Kotlin, módulos JVM puros para el núcleo (`:core:model`, `:core:policy`, `:core:agent`) separados de Android (`:platform:*`, `:feature:ui`), Gemini (flash-lite/flash/pro/live) como modelo, Room para persistencia local, openWakeWord (ONNX) para "Hey Bob".

**Seguridad:** `PolicyEngine` vive en código puro (no Android); el modelo puede subir el nivel de riesgo de una acción pero nunca bajarlo. Denylist financiera dura, pago solo con toque físico, aviso + 5s para cancelar acciones con efecto, nunca reintenta un efecto ya ejecutado.

Lecciones que deja: honestidad y resiliencia del asistente (no afirma lo que no verificó), deuda técnica visible, pruebas sin red con dobles.
