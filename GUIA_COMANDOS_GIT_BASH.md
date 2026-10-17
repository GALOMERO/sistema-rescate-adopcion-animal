# Guía para crear el proyecto y publicar sus cuatro avances

Esta guía está preparada para Windows con Git Bash. Los archivos de cada avance ya están creados. Copiarás una carpeta por etapa al mismo repositorio; cada copia reemplaza el Word y el PDF anteriores y agrega los nuevos componentes. Git conserva todas las versiones.

La actividad exige el diseño lógico, diagramas, tres patrones y Gitflow. El paquete agrega un prototipo de consola para demostrar los patrones. La entrega en el aula virtual es el **PDF final con el enlace público de GitHub y capturas reales**. Las versiones previas se publican como avances en GitHub.

## 1 Preparación

1. Instala Git para Windows desde https://git-scm.com/download/win y abre **Git Bash**.
2. Para ejecutar el prototipo, instala Python 3.10 o superior desde https://www.python.org/downloads/windows/. Marca la opción para agregar Python al PATH. No necesitas instalar librerías.
3. Ten acceso a Microsoft Word para personalizar los documentos y exportarlos a PDF.
4. Entra a tu cuenta de GitHub. Crea un repositorio llamado exactamente **rescate-adopcion-animal**, con visibilidad **Public** y sin README, licencia ni .gitignore iniciales.
5. Extrae el ZIP completo. Debes ver la carpeta **Actividad_DSI_Gitflow**, con esta guía y las carpetas `00_inicio`, `01_analisis`, `02_uml`, `03_patrones` y `04_final`.
6. Abre Git Bash **dentro de Actividad_DSI_Gitflow**, donde están esas cinco carpetas. Ejecuta los bloques en orden, en la misma ventana. Si un comando falla, corrige el problema antes de avanzar.

Los textos entre corchetes en los documentos son campos por completar. No uses el nombre ni el correo del profesor que aparecen como ejemplo en el tutorial.

## 2 Crear la carpeta y configurar tu identidad

Primero verifica que estás en el lugar correcto:

```bash
pwd
ls
git --version
```

En `ls` deben aparecer las cinco carpetas del paquete. Luego ejecuta:

```bash
PAQUETE="$PWD"
mkdir ../rescate-adopcion-animal
cd ../rescate-adopcion-animal
git init -b master
read -r -p "Tu nombre y apellido: " NOMBRE_ESTUDIANTE
read -r -p "Tu correo de GitHub: " CORREO_GIT
read -r -p "Tu usuario de GitHub: " USUARIO_GITHUB
git config user.name "$NOMBRE_ESTUDIANTE"
git config user.email "$CORREO_GIT"
git config --get user.name
git config --get user.email
```

Escribe tus datos y pulsa Enter después de cada pregunta. La configuración se aplica solo a este proyecto. Si `mkdir` indica que la carpeta ya existe, detente: usa una carpeta nueva o revisa si contiene un trabajo anterior. No borres archivos para continuar.

La carpeta del paquete y el repositorio quedan al mismo nivel. **No copies el paquete entero dentro del repositorio.** Los comandos siguientes copian solo el avance correspondiente.

## 3 Publicar el inicio y crear develop

```bash
cp -R "$PAQUETE/00_inicio/." .
git add .
git commit -m "chore: iniciar proyecto de rescate y adopcion"
URL_REPO="https://github.com/$USUARIO_GITHUB/rescate-adopcion-animal.git"
git remote add origin "$URL_REPO"
git remote -v
git push -u origin master
git checkout -b develop
git push -u origin develop
```

Si aparece una ventana de acceso, autentícate con tu cuenta de GitHub. No escribas tu contraseña normal como contraseña de Git por HTTPS. Con Git Credential Manager normalmente se abre el navegador. Si tu instalación requiere un token, sigue el tutorial proporcionado y no lo pegues en archivos, capturas ni en la URL del repositorio.

Se usa **master**, tal como exige la guía de la actividad. Mantén ese nombre durante todo este procedimiento aunque el tutorial genérico use `main`.

## 4 Avance 1 con análisis y requerimientos

### Copiar los archivos

```bash
git checkout develop
git checkout -b feature/analisis
cp -R "$PAQUETE/01_analisis/." .
git status
```

Abre `docs/Actividad_1.docx` **dentro del repositorio**, escribe tu nombre y paralelo, guarda y cierra Word. Personaliza también el autor y el enlace de `README.md`. Exporta desde Word como PDF y reemplaza `docs/Actividad_1.pdf`. La portada conserva el semestre quinto y actualiza el período al de la actividad.

### Guardar, publicar e integrar

```bash
git add .
git commit -m "docs: analizar actores y requerimientos del refugio"
git push -u origin feature/analisis
git checkout develop
git merge --no-ff feature/analisis -m "merge: integrar analisis en develop"
git push origin develop
```

En GitHub, selecciona `develop` y revisa los archivos. El historial de `docs/Actividad_1.docx` contiene ahora el primer avance.

## 5 Avance 2 con diagramas UML

```bash
git checkout develop
git checkout -b feature/uml
cp -R "$PAQUETE/02_uml/." .
git status
```

La copia reemplaza el Word y el PDF por el segundo avance y agrega los diagramas de casos de uso y clases. Vuelve a completar nombre y paralelo en el nuevo Word, y el autor y el enlace en el README. Guarda, exporta el PDF con el mismo nombre y cierra Word.

```bash
git add .
git commit -m "design: agregar casos de uso y clases UML"
git push -u origin feature/uml
git checkout develop
git merge --no-ff feature/uml -m "merge: integrar modelado UML en develop"
git push origin develop
```

Las imágenes PNG se abren directamente. Los SVG se pueden ampliar y los `.puml` son fuentes editables PlantUML. Los textos y relaciones de los diagramas corresponden al diseño; el renderizado de PlantUML puede distribuirlos de otra manera.

## 6 Avance 3 con patrones y código

```bash
git checkout develop
git checkout -b feature/patrones
cp -R "$PAQUETE/03_patrones/." .
python --version
```

Elige el comando de Python que funcione en tu equipo. Si el anterior muestra Python 3.10 o superior:

```bash
PY_CMD=python
```

Si `python` no funciona pero `py --version` muestra una versión compatible:

```bash
PY_CMD=py
```

Ejecuta la demo y las diez pruebas desde la raíz del repositorio:

```bash
$PY_CMD -m rescate.demo
$PY_CMD -m unittest discover -s tests -v
```

La demostración muestra Luna adoptada, Milo rescatado y el ave derivada, además de tres notificaciones simuladas y cero incidencias. Las pruebas deben terminar con **Ran 10 tests** y **OK**. Guarda una captura propia de ambos resultados en una ubicación temporal para insertarla en el informe final. Esto no envía correos reales.

Completa tus datos en el nuevo Word y README, guarda, exporta `docs/Actividad_1.pdf` y cierra Word. Luego:

```bash
git add .
git commit -m "feat: implementar Factory Method Observer Adapter y MVC"
git push -u origin feature/patrones
git checkout develop
git merge --no-ff feature/patrones -m "merge: integrar patrones y prototipo en develop"
git push origin develop
git log --graph --oneline --decorate --all
```

Toma una captura legible del historial. Si aparece el visor de Git, pulsa `q` para salir. También puedes ejecutar `git --no-pager log --graph --oneline --decorate --all` para evitar ese visor.

## 7 Avance 4 con documentación y evidencias

```bash
git checkout develop
git checkout -b feature/documentacion
cp -R "$PAQUETE/04_final/." .
git status
```

Antes del commit final:

1. En GitHub captura la URL pública y la lista de ramas. Puedes abrir el selector de ramas para mostrar `master`, `develop` y las ramas `feature/` ya publicadas.
2. Guarda esa imagen como `evidencias/01_repositorio.png`.
3. Guarda la captura del historial del avance 3 como `evidencias/02_historial.png`. Describe el momento real que muestra; el historial seguirá creciendo al cerrar esta versión.
4. Guarda la captura de la demo y las pruebas como `evidencias/03_ejecucion.png`. Si es necesario, vuelve a ejecutar los dos comandos.
5. Abre el Word **del repositorio**, completa nombre y paralelo y sustituye los dos campos del enlace público por `https://github.com/TU_USUARIO/rescate-adopcion-animal`.
6. Pega las tres capturas reales en el apartado Evidencias. Sustituye cada marcador y sus párrafos vacíos por la imagen correspondiente. Si necesitas espacio, deja que una captura ocupe una página adicional. Debe poder leerse.
7. Sustituye el campo de análisis de la evidencia por una explicación breve de tu ejecución. Actualiza autor y enlace del README.
8. Guarda el Word y exporta el PDF reemplazando `docs/Actividad_1.pdf`. Revisa el PDF: portada, enlace, diagramas y capturas. Cierra Word antes de continuar.

```bash
git add .
git commit -m "docs: completar informe y evidencias reales de Gitflow"
git push -u origin feature/documentacion
git checkout develop
git merge --no-ff feature/documentacion -m "merge: integrar documentacion final en develop"
git push origin develop
```

No basta con copiar cuatro archivos distintos en un solo commit: los pasos anteriores producen avances sucesivos e integraciones verificables. En GitHub puedes abrir `docs/Actividad_1.docx` o `docs/Actividad_1.pdf` y consultar **History** para comprobarlos. Los archivos binarios no muestran diferencias de texto como el código, pero cada commit conserva sus bytes.

## 8 Preparar la release y publicar la entrega estable

```bash
git checkout develop
git checkout -b release/1.0.0
echo "1.0.0" > VERSION.txt
git add VERSION.txt
git commit -m "chore: preparar release 1.0.0"
git push -u origin release/1.0.0
$PY_CMD -m unittest discover -s tests -v
git checkout master
git merge --no-ff release/1.0.0 -m "release: publicar version estable 1.0.0"
git tag -a v1.0.0 -m "Entrega estable de la actividad 1"
git push origin master
git push origin v1.0.0
git checkout develop
git merge --no-ff release/1.0.0 -m "merge: sincronizar release 1.0.0 con develop"
git push origin develop
git checkout master
```

Las ramas de avances se conservan para facilitar la revisión académica. La rama `release/1.0.0` sirve para la preparación de la entrega; después se fusiona en las dos ramas permanentes. No se crea una rama hotfix porque no hay una corrección urgente de una versión ya publicada.

## 9 Comprobación y entrega en el aula

```bash
git status
git branch -a
git --no-pager log --graph --oneline --decorate --all
git tag --list
git ls-remote --heads origin
```

Verifica que `git status` indique que no hay cambios pendientes, que existan las ramas remotas y la etiqueta `v1.0.0`, y que el último contenido esté en `master`.

En GitHub selecciona `master` y abre `docs/Actividad_1.pdf`. El PDF debe tener tus datos, el enlace correcto y tus capturas. Comprueba que el repositorio se puede abrir sin iniciar sesión, por ejemplo en una ventana privada. El enlace público es obligatorio.

Para el aula virtual, usa el PDF final y nómbralo como pide la actividad: **apellido_nombre_actividad1.pdf**. Puedes hacer una copia fuera del repositorio con ese nombre para no generar cambios pendientes. Conserva el Word editable.

## 10 Si cierras Git Bash entre etapas

Las variables `PAQUETE`, `PY_CMD` y `USUARIO_GITHUB` duran solo mientras está abierta esa consola. Si la cierras, vuelve a abrir Git Bash dentro del repositorio y restablece las rutas. Por ejemplo, si conservaste ambas carpetas al mismo nivel:

```bash
PAQUETE="$(cd ../Actividad_DSI_Gitflow && pwd)"
PY_CMD=python
git status
git branch --show-current
```

Usa `PY_CMD=py` si ese es tu comando válido. Comprueba con `ls "$PAQUETE"` que aparecen las carpetas de avances. El remoto y tu identidad ya quedaron guardados en Git.

## 11 Soluciones breves a errores frecuentes

- **remote origin already exists**: revisa `git remote -v`; si la dirección es incorrecta, usa `git remote set-url origin https://github.com/TU_USUARIO/rescate-adopcion-animal.git`.
- **Repository not found**: confirma usuario, nombre exacto del repositorio, existencia y cuenta autenticada.
- **nothing to commit**: usa `git status` y verifica que copiaste el avance correcto en la carpeta del repositorio y guardaste los cambios de Word.
- **Author identity unknown**: ejecuta de nuevo los comandos `git config user.name` y `git config user.email` con tus datos.
- **python no se reconoce**: prueba `py --version`; si funciona, usa `PY_CMD=py`. Si no, revisa la instalación de Python.
- **No module named rescate**: ejecuta `pwd` y `ls`; debes estar en la raíz del repositorio, donde aparece la carpeta `rescate`, y usar el avance 3 o 4.
- **Rama ya existente**: no repitas `checkout -b`; comprueba `git branch` y usa `git checkout NOMBRE_RAMA` para volver a ella.
- **push rechazado porque el remoto tiene otros commits**: no uses `--force`. Comprueba primero `git fetch origin`, `git status` y el historial. El procedimiento supone un remoto vacío al inicio y una sola copia de trabajo; si cambió el remoto, hay que integrar sus cambios antes de publicar.
- **Permission denied al copiar el Word**: cierra Word, el explorador de PDF y las vistas previas del archivo, y vuelve a intentar la copia.

## Referencias del procedimiento

- Guía y tutorial de la asignatura proporcionados con la actividad.
- Driessen, V. (2010). A successful Git branching model. https://nvie.com/posts/a-successful-git-branching-model/
- Git. git-merge. https://git-scm.com/docs/git-merge
- GitHub. Agregar código hospedado localmente a GitHub. https://docs.github.com/es/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github
