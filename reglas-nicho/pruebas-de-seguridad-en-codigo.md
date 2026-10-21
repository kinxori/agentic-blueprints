# Pruebas de seguridad como código

> **Aplica a:** código con dinero, credenciales o datos personales · **Evidencia:** fuerte

**Principio:** las reglas de seguridad se expresan como pruebas automáticas, no como texto en un documento.

**Por qué:** una regla escrita se olvida; una prueba que falla no. En el origen estas pruebas dieron mucho valor.

**Cómo aplicarlo — pruebas a escribir en todo proyecto con acciones sensibles:**
- **Autorización:** el botón/acción sensible solo funciona para el dueño.
- **Un solo uso:** las confirmaciones no se pueden reutilizar (anti-replay).
- **Límites:** topes de monto, frecuencia y alcance, verificados en prueba.
- **Contenido externo = dato:** texto de web, correos, archivos o APIs nunca se trata como instrucción.
- **Arquitectura:** un `test_arquitectura.py` que verifica la estructura (qué módulo puede importar a cuál, dónde viven los secretos) para que no se desordene con el tiempo.

**Cuándo no aplica:** nunca se omite si hay dinero, credenciales o datos personales.

Relacionado: [[interruptores-con-confirmacion]], [[../eficiencia/puerta-de-preproduccion]]
