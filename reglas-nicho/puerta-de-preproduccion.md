# Puerta de preproducción mecánica

> **Aplica a:** software con despliegue · **Evidencia:** fuerte

**Principio:** antes de producción, un script determinista y gratis hace las comprobaciones baratas. Los agentes de revisión (caros) entran después y una sola vez.

**Por qué:** gastar tokens en lo que un script puede verificar es desperdicio. Ordenar de barato a caro filtra el 90 % de los problemas sin costo.

**Cómo aplicarlo:**
1. Script único (`preflight`) que corre: sintaxis/lint, pruebas, escaneo de secretos, validación de mensajes/textos al usuario.
2. Si falla, se corrige y se repite el script; no se invoca a ningún agente.
3. Solo con el script en verde se lanzan los agentes de revisión, una pasada.
4. Cualquier verificación que se pueda volver script, se vuelve script.

**Cuándo no aplica:** prototipos desechables.

Relacionado: [[../seguridad/pruebas-de-seguridad-en-codigo]]
