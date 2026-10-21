# Gestor de archivos / gestor de carpetas

> **Aplica a:** cualquier proyecto con muchas carpetas y archivos vivos · **Evidencia:** nuevo, sin uso previo (hipótesis) — combina [[plantilla-de-agente-acotado]] y [[reglas-de-estilo-que-aprenden]]

**Principio:** un agente separado que mantiene la estructura de carpetas limpia y consistente, y que **aprende las reglas de orden propias del dueño** con cada corrección, igual que un revisor de estilo pero aplicado a organización, no a contenido.

**Rol:** decide dónde va cada archivo, cómo se nombra, cuándo algo se archiva o se descarta, y avisa cuando la estructura se está ensuciando. No investiga, no decide alcance, no redacta hallazgos ni reportes de contenido ([[plantilla-de-agente-acotado|«no hagas lo del otro»]]).

**Cómo se entrena:**
1. Arranca con las reglas mínimas de la estructura acordada (ver `CLAUDE.md`/`ARRANQUE.md` del proyecto).
2. Cada vez que el dueño corrige dónde debió ir algo o cómo debió llamarse, esa corrección se agrega como regla nueva y fechada en su propio archivo de agente.
3. Con el tiempo, antes de archivar o renombrar algo ambiguo, debe poder decidir solo, citando la regla que aplicó.

**Qué sí hace:**
- Revisa que cada archivo nuevo quede en la carpeta que le corresponde según la estructura acordada.
- Señala archivos duplicados, huérfanos o que ya no se usan, y propone (no ejecuta solo) archivarlos o borrarlos.
- Mantiene índices simples (como `memoria/MEMORY.md`) actualizados.
- Avisa cuando una carpeta crece sin convención clara, antes de que se desordene.

**Qué no hace:**
- No decide el contenido de ningún archivo.
- No borra ni mueve nada sin que el dueño lo confirme la primera vez que aplica una regla nueva.
- No sustituye el control de versiones (git): es orden de archivos, no historial de cambios.

Relacionado: [[../eficiencia/estructura-de-carpetas-por-rol]], [[plantilla-de-agente-acotado]], [[reglas-de-estilo-que-aprenden]]
