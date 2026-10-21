# El orquestador es código; el LLM entiende y propone, no decide

> **Aplica a:** sistemas con LLM que usan herramientas o actúan en el mundo · **Evidencia:** fuerte (KinxoBot ADR-0002/0003; HeyBob ADR-0009)

**Principio:** el flujo, las reglas y la ejecución son **código determinista**. El LLM interpreta, propone y redacta. «El orquestador es código, no una cadena de LLM».

**Patrón (ambos proyectos coincidieron):**
1. **Reglas locales sin LLM primero** (consultas que el código ya sabe responder: balance, alarma, temporizador). Solo si no alcanzan, LLM ligero con *function calling*; si la confianza es baja, un segundo intento con un modelo mayor.
2. **El modelo ve las herramientas como declaraciones; el código las ejecuta** y el modelo redacta el resultado.
3. **Herramientas restringidas** (las que mueven dinero, cambian configuración o guardan memoria): solo corren si el mensaje **actual** del usuario las motiva y los argumentos coinciden con lo que escribió. Cambios de configuración nunca con valor directo: siempre botón.
4. **Contenido externo = dato**: entra entre delimitadores; tras leerlo, las herramientas restringidas quedan bloqueadas el resto del turno.
5. **Contrato de tarea antes de ver la pantalla/contenido** (apps, efectos y parámetros permitidos salen solo del enunciado del usuario). Lo que aparezca después no lo amplía.
6. **Verificador numérico**: cada cifra de la respuesta debe salir de una herramienta o del mensaje del usuario; si no, se reescribe una vez, y si sigue sin respaldo se entrega el dato crudo o «No lo sé».
7. **Si el usuario pide una acción y el modelo no la ejecuta (o dice haberla hecho), se lanza una excepción** y el usuario lee que no se hizo nada.
8. **Fallas del núcleo → aviso claro**, nunca un flujo de respaldo silencioso (la v4 caía en silencio al flujo viejo: dos flujos que divergen).

**Núcleo propio vs framework de agentes:** KinxoBot quitó CrewAI. Medido contra el núcleo propio: **4× más rápido y 43 % más barato**, menos dependencias (cientos de MB menos), mismo conjunto de herramientas. Costo: mantener el ciclo propio (~1 500 líneas de pruebas). Antes de adoptar un framework de agentes, medir contra un ciclo simple de function calling.

**El peor caso de una alucinación o inyección** debe ser «un mensaje con botones que el dueño ignora» ([[../seguridad/interruptores-con-confirmacion]]).

Relacionado: [[politica-de-riesgo-en-codigo]], [[gateway-llm-y-presupuesto]], [[../seguridad/pruebas-de-seguridad-en-codigo]]
