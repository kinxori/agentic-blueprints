# Evidencia sobre inferencia

> **Aplica a:** software, apps móviles, depuración · **Evidencia:** fuerte

**Principio:** capturas, trazas y logs son la verdad; las suposiciones no. Lo no probado se marca **«no verificado»**.

**Por qué:** así se hallaron en el origen un bucle de eco, una condición de 3 eventos seguidos que debilitaba un disparador y un bug que se saltaba un evento. Ninguno se veía leyendo código.

**Cómo aplicarlo:**
- Etiquetas de log por componente (`Agente`, `Live`, `WakeWord`…): cada arreglo se verifica leyendo una línea concreta.
- Reproducir con scripts que simulan la entrada (comandos por adb, comandos `live:`/`wake:`) en vez de depender de probar a mano.
- Reportes del usuario mientras prueba («entró en loop») son datos de primera calidad; pídelos y regístralos.
- En informes, separar siempre: verificado / inferido / no verificado.

Relacionado: [[ciclo-corto-de-iteracion]], [[verificar-antes-de-afirmar]]
