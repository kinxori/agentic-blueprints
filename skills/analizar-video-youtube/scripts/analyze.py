#!/usr/bin/env python3
"""Analiza un video de YouTube con Gemini (comprensión nativa de video/audio).

No descarga el video ni extrae frames: le pasa la URL de YouTube directamente
a la API de Gemini, que entiende visual + audio + timing en una sola llamada.

Uso:
    python3 analyze.py <youtube_url> [--question "enfoque específico"] [--model gemini-3.6-flash]
    python3 analyze.py --check    # solo valida que la API key funcione

La API key se lee de la variable de entorno GEMINI_API_KEY. Consíguela en
https://aistudio.google.com/apikey.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

DEFAULT_MODEL = "gemini-3.6-flash"
ENDPOINT_TMPL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

DEFAULT_PROMPT = """\
Analiza este video de YouTube y entrega un análisis estructurado en las \
siguientes secciones, con marcas de tiempo aproximadas (mm:ss) cuando aplique:

1. NARRATIVA / ESTRUCTURA: cómo está contado, gancho inicial, giros, cierre.
2. ELEMENTOS VISUALES: composición, edición, gráficos, texto en pantalla, \
   b-roll, momentos visualmente destacados.
3. ELEMENTOS AUDITIVOS: música, efectos de sonido, tono de voz, silencios.
4. RITMO Y PAUSAS: dónde se usan pausas deliberadas y con qué efecto.
5. TONO: formal, humorístico, dramático, etc., y momentos que lo marcan.
6. OBSERVACIONES GENERALES: qué funciona bien para retención y qué se \
   podría mejorar.

Sé específico y cita momentos concretos del video en vez de generalizar.
"""


def require_key() -> str:
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise SystemExit(
            "Falta GEMINI_API_KEY. Consigue una llave en "
            "https://aistudio.google.com/apikey y expórtala como variable "
            "de entorno (export GEMINI_API_KEY=...) o guárdala en tu .env."
        )
    return key


def call_gemini(model: str, api_key: str, parts: list[dict]) -> dict:
    url = ENDPOINT_TMPL.format(model=model)
    body = json.dumps({"contents": [{"parts": parts}]}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"ERROR HTTP {e.code} de Gemini API:\n{detail}")
    except urllib.error.URLError as e:
        raise SystemExit(f"ERROR de red al llamar a Gemini API: {e}")


def extract_text(response: dict) -> str:
    try:
        candidates = response["candidates"]
        parts = candidates[0]["content"]["parts"]
        return "\n".join(p.get("text", "") for p in parts if "text" in p)
    except (KeyError, IndexError):
        return json.dumps(response, indent=2, ensure_ascii=False)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video_url", nargs="?", help="URL del video de YouTube")
    parser.add_argument(
        "--question", "-q", default=None,
        help="Enfoque específico o pregunta adicional sobre el video",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Modelo Gemini a usar")
    parser.add_argument(
        "--check", action="store_true",
        help="Solo valida que la API key funcione (llamada mínima, sin video)",
    )
    args = parser.parse_args()

    api_key = require_key()

    if args.check:
        response = call_gemini(args.model, api_key, [{"text": "Responde solo con: ok"}])
        print("Auth OK. Respuesta de prueba:", extract_text(response).strip())
        return

    if not args.video_url:
        parser.error("video_url es requerido (o usa --check)")

    prompt = DEFAULT_PROMPT
    if args.question:
        prompt += f"\n\nEnfoque adicional pedido por el usuario: {args.question}\n"

    parts = [
        {"file_data": {"file_uri": args.video_url}},
        {"text": prompt},
    ]
    response = call_gemini(args.model, api_key, parts)
    print(extract_text(response))


if __name__ == "__main__":
    main()
