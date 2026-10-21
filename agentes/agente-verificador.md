# Agente verificador (por construir)

> **Aplica a:** software · **Evidencia:** hipótesis

**Necesidad:** en dos proyectos distintos el humano/asistente repite a mano build + pruebas + prueba real. Es candidato a agente separado.

**Diseño propuesto (según [[plantilla-de-agente-acotado]]):**
- Rol: ejecutar build, suite de pruebas y la prueba en entorno real; reportar solo hechos.
- No modifica código.
- Salida: informe con lo verificado y lo **«no verificado»** explícito.
- Se apoya en scripts mecánicos ([[../eficiencia/puerta-de-preproduccion]]) y en [[../metodologias/evidencia-sobre-inferencia]].

**Estado:** hipótesis; validar con un uso real antes de darlo por bueno.
