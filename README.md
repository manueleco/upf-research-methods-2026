# Research Methods UPF 2026

Panel de seguimiento del curso 2026–2027 con tarjetas horizontales, Kanban, Gantt, materiales y calendario. Las 23 tareas distinguen hitos docentes y planificación personal. El análisis y las fuentes están en COURSE.md.

## Abrir el panel

Puedes hacer doble clic en `Abrir-RM.command` o ejecutar desde cualquier directorio:

```sh
python3 "/Users/meco/MBP Files/Gits/upf/RM/serve.py"
```

El lanzador sirve siempre la carpeta docs/ de este proyecto. RM utiliza el puerto preferido 8321. Si está ocupado, prueba los siguientes 31 puertos y, si todos están ocupados, el sistema asigna uno libre. La terminal muestra la URL real; abre esa dirección. No detiene ni modifica los servidores de otros cursos. Ctrl+C detiene únicamente el servidor de RM.

Para escoger otro puerto preferido, añade `--port 8325`. El progreso del navegador depende de la dirección y del puerto: exporta desde la dirección anterior e importa en la nueva si necesitas trasladarlo. Mantener libre el puerto preferido permite volver al mismo progreso en las siguientes sesiones.

El sitio carga data.json, por lo que requiere un servidor local o GitHub Pages. La entrada index.html de la raíz redirige a docs/ para mantener compatible la publicación desde la raíz del repositorio.

## Vistas y cambios

Tarjetas horizontales, Kanban y Gantt comparten búsqueda, fase, grupo y estado. Los estados son Pendiente, En curso, Bloqueada y Completada. El estado puede cambiarse directamente con el desplegable; en Kanban también se puede arrastrar desde Mover.

Fechas y notas abre un diálogo para modificar la planificación local. Los plazos originales permanecen en data.json y se muestran como referencia. Una fecha pasada invita a comprobar el envío; no implica una entrega incumplida. El próximo hito confirmado se calcula sobre el curso completo y usa las fechas de las fuentes.

La página abre en consulta. Desbloquear edición habilita cambios e importación y se vuelve a bloquear al recargar. La clave local está en ACCESS.local.txt, excluido de Git. No es autenticación de servidor y no protege el código público. Los cambios se guardan en este navegador; no se escriben en Moodle ni GitHub.

La clave de almacenamiento es exclusiva de RM y del curso académico. El progreso del panel anterior se migra si existe en el mismo origen. Por confirmar pasa a Pendiente, y las fechas pasadas conservan su señal de revisión.

Exportar cambios genera un JSON con identificador de curso. Importar combina cambios tras validar curso, versión, IDs, estados, fechas y notas. Para trasladar progreso entre dispositivos u orígenes, exporta e importa el archivo. El cambio de puerto o de localhost a GitHub Pages usa otro almacenamiento.

## Archivos

- docs/index.html, tokens.css, style.css y app.js: interfaz estática sin compilación.
- docs/data.json: tareas, fuentes y materiales públicos.
- docs/config.js: hash de desbloqueo de edición.
- docs/calendar.ics: hitos; A3 conserva su horario de 23:59 en Europe/Madrid.
- tasks.csv y planning/: exportaciones del conjunto de tareas.
- COURSE.md: requisitos, evaluación e incertidumbres del curso.
- materials/catalog.json: índice y relación con tareas.
- materials/private/originals/ y extracted/: materiales locales excluidos de Git.
- projects/mere/: checklist y matrices para literatura y revisión.
- ACCESS.local.txt: clave local excluida de Git.

El calendario contiene ambas ramas martes/viernes; conserva la que corresponde a tu grupo. La hora de los hitos distintos de A3 sigue pendiente de publicación. Las exportaciones CSV y calendario reflejan el plan publicado, no los cambios guardados en el navegador.

## GitHub Pages

Repositorio: https://github.com/manueleco/upf-research-methods-2026

En Settings → Pages selecciona Deploy from a branch, rama main y carpeta /docs. La publicación desde / (root) también funciona mediante la redirección de entrada. URL prevista: https://manueleco.github.io/upf-research-methods-2026/.

Actualizar el plan público requiere modificar docs/data.json y regenerar las exportaciones, hacer commit y push con tu cuenta. Los archivos de materials/private/ y ACCESS.local.txt están excluidos. Solo docs/ contiene los archivos del sitio. Los materiales docentes no se redistribuyen; la web abre sus fuentes en Aula Global.
