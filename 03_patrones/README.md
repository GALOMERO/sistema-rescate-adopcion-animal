# Sistema de control de rescate y adopción animal

Avance 3 de 4 de la Actividad 1 de Desarrollo de Sistemas Informáticos, UTM.
Autor: [NOMBRE Y APELLIDO]. Repositorio: [ENLACE REAL].

## Documentación
- `docs/Actividad_1.docx`: informe editable en la plantilla institucional.
- `docs/Actividad_1.pdf`: exportación para revisión o entrega.
- `docs/requerimientos.md`: alcance y criterios de aceptación.

## Diagramas
La carpeta `diagramas/` contiene PNG para lectura, SVG y fuentes PlantUML `.puml` para edición. Los SVG y PNG son representaciones del mismo diseño; la distribución visual del PlantUML puede variar.

## Ejecución con Python 3.10 o superior
No requiere dependencias externas. Desde la raíz del proyecto:

```bash
python -m rescate.demo
python -m unittest discover -s tests -v
```

En Windows puede usarse `py` en lugar de `python` si así funciona la instalación.
El programa es un prototipo didáctico de consola: datos en memoria, mensajes simulados y sin autenticación. No es una plataforma productiva ni envía correos reales.

## Patrones implementados
- Factory Method: `rescate/fabricas.py`, método `crear_animal` redefinido por cada creador.
- Observer: `rescate/notificaciones.py`, `PublicadorCasos` y `Observador`.
- Adapter: `rescate/notificaciones.py`, `CorreoAdapter` integra `ServicioCorreo`.
- MVC: modelo en `modelos.py`, controlador en `controlador.py` y vista en `vista.py`.

## Gitflow
`master` conserva la entrega estable; `develop` integra avances. Las ramas `feature/analisis`, `feature/uml`, `feature/patrones` y `feature/documentacion` se crean desde `develop`. La entrega se prepara en `release/1.0.0` y se integra en `master` y `develop`.
