# Research Methods UPF 2026

Plan del curso revisado el 13 de octubre de 2026. Abre `index.html` para ver tareas, Gantt y materiales. Elige martes o viernes; los estados iniciales no presuponen que hayas completado entregas anteriores.

## Evaluación

60% tareas durante el curso y participación; 40% MERE: pitch 10%, documento 20%, presentación de póster 10%. Mínimo 5/10. La introducción no anuncia un examen. La guía docente enlazada devuelve un error, por lo que no se ha podido contrastar allí. No se aceptan tareas fuera de plazo según la diapositiva 9 de Introducción.

## Entregas inmediatas

- Assignment 1: 9 octubre. Un capítulo de Eco o de O’Leary y su formulario. Comprobar si ya se envió.
- Formación de equipos y tema: 6 octubre martes / 9 octubre viernes, antes de clase. Grupos de 4.
- Assignment 2: 19 octubre, sin hora publicada. Formación en ética y protección de datos, certificado y formulario de reflexión.
- Assignment 3: 24 octubre, 23:59. PDF de 2 páginas + 1 para referencias con preguntas de investigación, revisión breve, justificación de importancia/originalidad y bibliografía. Cada integrante aporta unas 3–4 referencias; indicar en apéndice quién encontró cada una. Confirmar cómo computa el apéndice. Aula mostraba que no había envío el 13/10.

## Proyecto MERE

Pequeño estudio/experimento sobre la investigación misma: cómo las herramientas IA contribuyen u obstaculizan la búsqueda de información, formulación, análisis de datos o comunicación de resultados. No basta una revisión de literatura sin el estudio previsto por las instrucciones. Paper de máximo 8 páginas + referencias, con declaración de autoría, usando las plantillas docentes. Envío a EasyChair MERE 2026; enlace específico pendiente.

Pitch 7 minutos: 27/30 octubre (martes/viernes, correspondencia inferida por calendario). Primer paper 11 noviembre; peer review 18 noviembre; versión final 25 noviembre; conferencia viernes 27 noviembre o martes 1 diciembre. Las diapositivas no precisan horas para estos hitos.

## Archivos

- `planning/tasks.json` y `tasks.csv`: tareas, dependencias, fechas oficiales frente a bloques de trabajo propuestos.
- `materials/catalog.json`: enlaces, relación con tareas y hashes de 9 archivos descargados.
- `materials/originals/`: materiales locales, fuera de Git.
- `materials/extracted/`: texto para análisis posterior, fuera de Git.
- `projects/mere/`: checklist del proyecto y matrices vacías para literatura y revisión.
- `notes/material-analysis.md`: cómo aplicar los materiales al trabajo.

La presentación Introduction publicada se conserva como enlace; la exportación no admite su formato publicado. Las lecturas externas se catalogan como enlaces, no están todas descargadas. Las secciones sobre formulación, métodos, escritura, investigadores, cierre y competencia digital están bloqueadas. Revisar cada semana para ampliar el plan. Los bloques del Gantt son una propuesta de trabajo; solo los hitos marcados como oficiales provienen del curso.

## GitHub

Nombre recomendado: `upf-research-methods-2026`. Alternativas: `upf-rm-2026` o `mere-2026-research-log`. Mantener privado si contiene trabajo o datos del equipo. Los originales y sus transcripciones quedan excluidos de Git; una imagen del curso prohíbe expresamente su distribución fuera de este.

Desde la carpeta RM:

```sh
git status --short
git add README.md .gitignore index.html planning materials/catalog.json notes projects
git commit -m "Organize Research Methods course plan and materials index"
gh repo create upf-research-methods-2026 --private --source=. --remote=origin --push
```

La última orden crea y sube el repositorio; ejecútala cuando quieras publicarlo en tu cuenta. Alternativa: crear un repositorio privado vacío en GitHub y seguir sus comandos de remote/push. No hay licencia general para materiales de terceros. Los estados del panel se guardan en ese navegador; usa Exportar progreso para conservarlos o moverlos.

## Fuentes

[Curso](https://aulaglobal.upf.edu/course/view.php?id=95580), [Assignment 1](https://aulaglobal.upf.edu/mod/page/view.php?id=1800753), [Assignment 2](https://aulaglobal.upf.edu/mod/url/view.php?id=1800759), [Assignment 3](https://aulaglobal.upf.edu/mod/assign/view.php?id=1800813), [MERE diapositivas 5–6 y 12–14](https://aulaglobal.upf.edu/mod/resource/view.php?id=1800805), [Introducción diapositivas 9–10](https://aulaglobal.upf.edu/mod/url/view.php?id=1800751).
