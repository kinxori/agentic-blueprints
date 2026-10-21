# Reglas para agentes con acceso a dispositivos, cuentas o dinero

> **Aplica a:** agentes con acceso a dispositivos, cuentas o dinero · **Evidencia:** fuerte

**Principio:** fija las líneas rojas por escrito antes de dar acceso.

**Reglas del origen, generalizadas:**
- **Llaves solo en `.env`** (fuera de git y de carpetas sincronizadas). Nunca pedirlas por chat.
- **Dinero:** no abrir apps financieras; pagos solo con toque del dueño, aviso previo y ventana de cancelación (p. ej. 5 s).
- **Dispositivos:** no tocar ajustes críticos (p. ej. accesibilidad); nada fuera de la app del proyecto.
- **Pruebas:** no usar servicios de terceros reales o sensibles (streaming, domótica) como banco de pruebas.
- **Estado honesto:** lo no probado se marca «no verificado».

Relacionado: [[interruptores-con-confirmacion]], [[pruebas-de-seguridad-en-codigo]], [[../metodologias/evidencia-sobre-inferencia]]
