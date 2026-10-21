# Generación de imágenes con IA: lo que funcionó

> **Aplica a:** imagen/diseño con IA · **Evidencia:** media

**Reglas ganadas probando y descartando:**
- **Caras individuales:** modelo con identidad entrenada (Soul ID).
- **Grupos:** solo planos abiertos o de espaldas; nunca 3+ caras de frente en plano medio.
- **Poses de una referencia:** primero **analizar la pose y describirla en texto**, luego meterla al prompt. Pasar la imagen directamente copiaba la escena completa.
- **Limpieza de fondo/joyería:** un modelo de edición sirve, pero con varias referencias de personas altera pose y cara. Una referencia de persona a la vez.
- **Memoria visual del proyecto** (colores, objetos, estilo de casas, vehículos permitidos) en archivos para no repetirla ([[contexto-persistente-entre-sesiones]]).

**No funcionó:** face swap y "elements" para caras de grupo; hojas de personaje como solución de consistencia.

Relacionado: [[aprobar-antes-de-generar]], [[../agentes/revisor-con-bucle-de-correccion]]
