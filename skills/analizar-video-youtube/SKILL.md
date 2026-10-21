---
name: analizar-video-youtube
description: Analiza un video de YouTube con Gemini (comprensión nativa de video/audio) — narrativa, elementos visuales, elementos auditivos, ritmo/pausas y tono. Úsalo cuando el usuario pida analizar, desglosar o estudiar un video de YouTube (propio o de referencia/competencia).
argument-hint: "<youtube-url> [enfoque u pregunta específica]"
allowed-tools: Bash, Read
user-invocable: true
---

# /analizar-video-youtube

Analiza un video de YouTube directamente por URL usando la comprensión nativa
de video de Gemini (no requiere descargar el video, extraer frames ni
transcribir audio por separado — Gemini procesa visual + audio + timing en
una sola llamada).

## Requisito: tu propia API key de Gemini

Este skill necesita `GEMINI_API_KEY` en el entorno (consíguela gratis en
https://aistudio.google.com/apikey). No la pidas por chat ni la escribas tú
mismo salvo que el usuario te la entregue explícitamente — si falta, dile
cómo configurarla y detente ahí.

## Resolver `SKILL_DIR`

`SKILL_DIR` es la carpeta que contiene este `SKILL.md` (sibling de
`scripts/analyze.py`).

## Paso 1 — Ejecutar el análisis

```bash
python3 "${SKILL_DIR}/scripts/analyze.py" "<youtube_url>" [--question "<enfoque específico>"]
```

- `<youtube_url>`: la URL del video (debe ser público, no restringido por edad ni privado).
- `--question`: opcional, un enfoque o pregunta adicional del usuario (ej. "compara el gancho de este video con nuestro estilo").

El script imprime a stdout un análisis estructurado en 6 secciones: NARRATIVA/ESTRUCTURA,
ELEMENTOS VISUALES, ELEMENTOS AUDITIVOS, RITMO Y PAUSAS, TONO, y OBSERVACIONES GENERALES,
con marcas de tiempo aproximadas.

## Paso 2 — Responder al usuario

Lee la salida del script y preséntala al usuario de forma clara (puedes
reorganizarla, resumirla o resaltar lo más relevante según lo que haya
pedido). Si el usuario pidió algo puntual (ej. "solo dime los chistes" o
"solo dime la estructura"), prioriza esa parte de la respuesta.

## Notas

- Solo funciona con URLs públicas de YouTube (no videos privados o solo-no-listados en algunos casos, ni con restricción de edad).
- Videos muy largos pueden acercarse a límites de la API — si falla por longitud, informa al usuario en vez de reintentar en loop.
- No repitas ni muestres la API key en ningún momento, incluso si aparece en un mensaje de error.
- El prompt de análisis es genérico; si tu proyecto tiene una marca/tono propio (ej. un canal con estilo definido), ajusta `DEFAULT_PROMPT` en `scripts/analyze.py` a tu caso al copiar este skill.
