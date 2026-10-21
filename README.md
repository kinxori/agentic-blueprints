# Fabrica de Agentes

Este repositorio es la "Fábrica" de orquestadores. **No se programa aquí.** Sirve exclusivamente como biblioteca central para generar los archivos de arranque de proyectos nuevos.

## Cómo usarlo

Abre un chat nuevo en Claude/Gemini y pega este mensaje tal cual (no hace falta saber de terminal, el asistente clona el repo solo):

```
Clona https://github.com/kinxori/fabrica-de-agentes y úsalo como contexto.

Al terminar de clonar y leer el README, actúa directo como mi Bibliotecario Jefe: no resumas el repo ni preguntes qué quiero hacer con él. Lee GENERADOR_MAESTRO.md y arranca ahí mismo la Entrevista de Contexto (Fase 0) con sus preguntas, para ensamblar después un ARRANQUE.md unificado usando /agentes y /reglas, optimizado para ahorrar tokens y adaptado a mi stack.
```

Responde la entrevista, aprueba el plan, y copia el `ARRANQUE.md` resultante en tu nuevo proyecto local para arrancar a programar en un chat totalmente nuevo.
