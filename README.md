# Fabrica de Agentes

Este repositorio es la "Fábrica" de orquestadores. **No se programa aquí.** Sirve exclusivamente como biblioteca central para generar los archivos de arranque de proyectos nuevos.

## Cómo usarlo

Abre un chat nuevo en Claude/Gemini y pega este mensaje tal cual (no hace falta saber de terminal, el asistente clona el repo solo):

```
Clona https://github.com/kinxori/fabrica-de-agentes en una carpeta aparte (no dentro de mi proyecto), úsalo como contexto, y al terminar de clonar y leer el README actúa directo como mi Bibliotecario Jefe sin resumir el repo ni preguntarme qué hacer: lee GENERADOR_MAESTRO.md y arranca ahí mismo la Fase 0, para después ensamblar un ARRANQUE.md con /agentes y /reglas, copiar solo lo elegido a mi proyecto y borrar el clon.
```

Responde la entrevista, aprueba el plan, y deja que el asistente copie el `ARRANQUE.md` resultante a tu proyecto y borre el clon de la fábrica. Así tu proyecto nuevo arranca limpio, solo con lo que esa entrevista decidió que aplicaba — no con toda la biblioteca.

## Cómo contribuir

¿Tienes una regla, agente o referencia que le sirva a otros? Haz fork, trabaja tu cambio y abre un PR contra la rama `propuestas` (no contra `main`). Desde ahí se revisa y, si aplica, se mergea.
