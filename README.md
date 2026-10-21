# Gestionador Central de Agentes

Este repositorio es la "Fábrica" de orquestadores. **No se programa aquí.** Sirve exclusivamente como biblioteca central para generar los archivos de arranque de proyectos nuevos.

## Cómo usarlo

Cada vez que vayas a iniciar un proyecto nuevo, abre un chat en Claude/Gemini, conecta este repositorio como contexto y envía el siguiente prompt:

> **Actúa como mi Bibliotecario Jefe. Quiero iniciar un proyecto de [TIPO DE PROYECTO]. Lee `GENERADOR_MAESTRO.md` y las carpetas `/agentes` y `/reglas` para ensamblar un archivo `ARRANQUE.md` unificado, optimizado para ahorrar tokens y adaptado a este stack. Incluye la Entrevista de Contexto (Fase 0) con 4 preguntas clave para este nicho. Entrégame el bloque de código listo para copiar.**

Copia el resultado, pégalo en un archivo `ARRANQUE.md` en tu nuevo proyecto local, y arranca a programar en un chat totalmente nuevo.