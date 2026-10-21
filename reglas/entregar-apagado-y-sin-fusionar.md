# Anti-patrones de entrega

> **Aplica a:** proyectos con ramas/versiones · **Evidencia:** fuerte

Errores repetidos del proyecto de origen, no atrapados por el supervisor:

1. **Entregar todo apagado.** Se construye una función pero queda desactivada, sin avisar. (Caso real, 2026-10-16: el asistente dejó todo lo nuevo apagado por su cuenta y el dueño la vio «igual que antes». Regla resultante: uso diario encendido, dinero apagado; ver [[../seguridad/interruptores-con-confirmacion]].) *Prevención:* checklist de entrega que liste cada interruptor, su estado y cómo activarlo.
2. **Dejar trabajo sin fusionar.** Ramas/PR abiertos y olvidados. *Prevención:* al cerrar una sesión, listar PR y ramas pendientes; nada se da por «hecho» hasta estar fusionado.
3. **Apilar versiones (v5 sobre v4).** Se construye encima de una versión no consolidada. *Prevención:* cerrar y fusionar la versión anterior antes de empezar la siguiente.

Relacionado: [[procesos-no-sustituyen-revision-humana]], [[../seguridad/interruptores-con-confirmacion]]
