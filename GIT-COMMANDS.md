# GIT - GIT Commands: Cómo volver a un commit anterior

1. Crear repo
2. Hacer varios commits
3. Ver historial
4. Volver a un commit específico (sin romper nada)
5. Volver permanentemente a un commit (reescribir historia)

---

# 🔹 1️⃣ Inicializar repositorio

```bash
git init
```

---

# 🔹 2️⃣ Crear commits de ejemplo

```bash
echo "Version 1" > archivo.txt
git add archivo.txt
git commit -m "Primer commit"

echo "Version 2" >> archivo.txt
git add archivo.txt
git commit -m "Segundo commit"

echo "Version 3" >> archivo.txt
git add archivo.txt
git commit -m "Tercer commit"


git add .
```

---

# 🔹 3️⃣ Ver historial de commits

```bash
git log
```

Versión resumida (muy útil):

```bash
git log --oneline
```

Vas a ver algo así:

```
a1b2c3d Tercer commit
d4e5f6g Segundo commit
h7i8j9k Primer commit
```

---

# 🔹 4️⃣ Ver un commit específico (sin modificar la rama)

Si solo querés "ir" a ese commit para verlo:

```bash
git checkout ID_DEL_COMMIT
```

Ejemplo:

```bash
git checkout d4e5f6g
```

⚠ Esto te deja en **detached HEAD** (modo exploración).

Para volver a tu rama:

```bash
git checkout main
```

---

# 🔹 5️⃣ Volver permanentemente a un commit

Si querés que tu proyecto vuelva a ese estado y borrar lo que vino después:

```bash
git reset --hard ID_DEL_COMMIT
```

Ejemplo:

```bash
git reset --hard d4e5f6g
```

⚠ Esto elimina los commits posteriores (localmente).

---

# 🔹 6️⃣ Alternativa segura (crear una rama desde ese commit)

En vez de borrar historia:

```bash
git checkout -b nueva-rama ID_DEL_COMMIT
```

Ejemplo:

```bash
git checkout -b rama-experimento d4e5f6g
```

Esto es lo más profesional 👌

---

# 📌 Resumen rápido

| Acción                  | Comando                   |
| ----------------------- | ------------------------- |
| Ver historial           | `git log --oneline`       |
| Ver commit específico   | `git checkout ID`         |
| Volver definitivamente  | `git reset --hard ID`     |
| Crear rama desde commit | `git checkout -b rama ID` |

---

Diferencia entre:

- `reset`
- `revert`
- `checkout`
- `switch`
- `restore`

---

# GIT y GitHub: Configuración Inicial

### 1. **Iniciar un Repositorio Local**

En tu terminal, navega a la carpeta de tu proyecto y ejecuta:

```bash
git init
```

Esto inicializa un repositorio Git vacío en tu proyecto.

### 2. **Configurar el Repositorio Remoto en GitHub**

- Ve a tu cuenta de GitHub.
- Crea un nuevo repositorio:
  1.  Haz clic en el botón **New Repository**.
  2.  Asigna un nombre a tu repositorio.
  3.  Configura si será público o privado.
  4.  Haz clic en **Create Repository**.
- Copia la URL del repositorio remoto (HTTPS o SSH).

### 3. **Vincular el Repositorio Local al Remoto**

En tu repositorio local, agrega el remoto con el comando:

```bash
git remote add origin <URL-del-repo>
```

Por ejemplo:

```bash
git remote add origin https://github.com/tuusuario/tu-repo.git
```

Puedes verificar que el remoto se agregó correctamente ejecutando:

```bash
git remote -v
```

### 4. **Añadir Archivos al Repositorio**

Para añadir archivos al área de preparación (staging area), usa:

```bash
git add .
```

O selecciona archivos específicos:

```bash
git add archivo1 archivo2
```

### 5. **Crear un Commit**

Guarda los cambios en tu historial de Git con un mensaje descriptivo:

```bash
git commit -m "Mensaje claro sobre los cambios realizados"
```

### 6. **Subir los Cambios al Repositorio Remoto**

Sube tus commits al repositorio en GitHub (rama principal `main` o la que hayas configurado):

```bash
git push -u origin main
```

> Nota: Si el repositorio remoto no tiene una rama llamada `main`, puedes crearla antes de hacer `push` usando:
>
> ```bash
> git branch -M main
> ```

---

## Operaciones Frecuentes con GIT y GitHub

### 1. **Clonar un Repositorio Remoto**

Si quieres trabajar con un repositorio ya existente en GitHub, usa:

```bash
git clone <URL-del-repo>
```

Esto creará una copia local del repositorio en tu máquina.

### 2. **Actualizar tu Repositorio Local**

Para obtener los últimos cambios desde el repositorio remoto:

```bash
git pull origin main
```

### 3. **Ver el Estado de Tu Repositorio**

Consulta qué archivos han cambiado, cuáles están en `staging`, y cuáles no están rastreados:

```bash
git status
```

### 4. **Ver el Historial de Cambios**

Puedes ver el historial de commits usando:

```bash
git log --oneline
```

### 5. **Crear y Cambiar de Ramas**

- Crear una nueva rama:
  ```bash
  git branch <nombre-de-la-rama>
  ```
- Cambiarte a una rama existente:
  ```bash
  git checkout <nombre-de-la-rama>
  ```
- Crear y cambiar a una nueva rama directamente:
  ```bash
  git checkout -b <nombre-de-la-rama>
  ```

### 6. **Fusionar Ramas**

Para combinar cambios de una rama en la rama actual:

```bash
git merge <nombre-de-la-rama>
```

### 7. **Resolver Conflictos**

- Edita los archivos que tienen conflictos.
- Marca los conflictos como resueltos.
- Añade los archivos resueltos:
  ```bash
  git add <archivo-resuelto>
  ```
- Crea un commit para finalizar:
  ```bash
  git commit
  ```

---

### Buenas Prácticas

1. Usa mensajes de commit claros y descriptivos.
2. Realiza `pull` frecuentemente para evitar conflictos.
3. Trabaja con ramas para mantener la estabilidad en la rama principal.
4. Configura un `.gitignore` para excluir archivos innecesarios o sensibles.
   Ejemplo de un `.gitignore` típico:
   ```
   node_modules/
   .env
   dist/
   ```

---

El **staging area** en Git es el espacio donde se preparan los cambios antes de confirmarlos (hacer un `commit`). Aquí es donde seleccionas qué archivos o cambios quieres incluir en el próximo `commit`.

### Uso del **Staging Area**

Aquí te explico cómo interactuar con el **staging area**:

### 1. **Añadir Archivos al Staging Area**

Cuando realizas cambios en tus archivos y quieres que esos cambios sean parte de tu próximo `commit`, debes agregar esos archivos al staging area usando:

```bash
git add <archivo>
```

Por ejemplo, si modificaste un archivo llamado `index.html`:

```bash
git add index.html
```

Si has hecho cambios en varios archivos y quieres añadir todos al staging area, puedes usar:

```bash
git add .
```

Este comando añade **todos los archivos modificados** (y nuevos) al staging area. Sin embargo, es importante tener cuidado, ya que incluirá todos los archivos que hayan cambiado, incluso si algunos no deseas incluir en el commit.

Si solo quieres incluir ciertos archivos o directorios específicos, puedes agregar esos de manera individual:

```bash
git add src/archivo.js
```

### 2. **Ver el Estado del Staging Area**

Para ver qué archivos están en el staging area y qué cambios están listos para ser confirmados, usa:

```bash
git status
```

Este comando te mostrará algo como esto:

```bash
On branch main
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   index.html
        new file:   src/style.css
```

Aquí, `index.html` ha sido modificado y `src/style.css` es un archivo nuevo que se ha añadido al staging.

### 3. **Deshacer Cambios del Staging Area**

Si agregaste un archivo al staging y luego decides que no quieres incluirlo en el próximo commit, puedes **deshacer** esa acción con el siguiente comando:

```bash
git reset <archivo>
```

Por ejemplo:

```bash
git reset index.html
```

Esto elimina `index.html` del staging, pero **no deshace** los cambios que has hecho en el archivo, solo lo quita de la lista para el próximo commit.

Si deseas deshacer todos los archivos en el staging, usa:

```bash
git reset
```

### 4. **Ver los Cambios en el Staging Area**

Para ver los cambios que has preparado para el próximo commit, puedes usar:

```bash
git diff --staged
```

Esto muestra las diferencias entre lo que está en el staging area y el último commit. Es útil para revisar exactamente qué cambios vas a confirmar.

### 5. **Realizar un Commit**

Una vez que los archivos están en el staging y estás listo para confirmarlos, puedes hacer un `commit`:

```bash
git commit -m "Descripción clara de los cambios realizados"
```

Este comando toma todos los cambios en el staging area y los guarda en el historial del repositorio.

### Resumen de Comandos del Staging Area

- **Añadir archivos al staging area**: `git add <archivo>`
- **Añadir todos los archivos modificados**: `git add .`
- **Ver el estado del staging area**: `git status`
- **Deshacer archivos del staging**: `git reset <archivo>`
- **Ver los cambios listos para commit**: `git diff --staged`
- **Confirmar los cambios**: `git commit -m "mensaje"`

---

### Buenas Prácticas con el Staging Area

- **Commit frecuente**: Es recomendable hacer commits frecuentes, pero solo con los cambios que estén listos. Usa el staging area para preparar solo los cambios que sean coherentes.
- **Commit atómico**: Cada commit debe representar una unidad de trabajo lógica. No hagas un commit con cambios no relacionados.
- **Revisión antes de commit**: Revisa los cambios con `git diff --staged` antes de realizar el commit, para asegurarte de que solo estás incluyendo lo que deseas.

El staging area es una herramienta poderosa en Git, que te permite tener control total sobre qué cambios confirmar en cada commit.

---

# GitFlow GROUP

Es importante asegurarse de que todas las ramas estén actualizadas con la última versión de master antes de comenzar a trabajar en ellas y también de realizar pruebas y revisiones antes de fusionar las ramas en master para asegurarse de que todo funciona correctamente. Además, es recomendable utilizar un flujo de trabajo de ramificación adecuado, como Gitflow, para mantener un control adecuado del flujo de trabajo del repositorio.

Puede hacerse manualmente o utilizando alguna herramienta como GitKraken o Sourcetree, que facilitan la implementación de GitFlow.

1. Crear una rama develop a partir de master:

```bash
git checkout -b develop master
git push -u origin develop
```

Esta rama se utilizará para integrar las características y solucionar los problemas antes de incorporarlos a la rama principal.

2. Crear una rama de característica a partir de develop para desarrollar una nueva función o característica:

```bash
git checkout -b feature/nombre-de-la-caracteristica develop
```

Esta rama se utilizará para desarrollar la característica de forma aislada del resto del código.

3. Desarrollar y probar la característica en la rama de característica.

Una vez que se ha completado la característica, fusionarla en la rama develop:

```bash
git checkout develop
git merge --no-ff feature/nombre-de-la-caracteristica
git push origin develop
```

4. Crear una rama de lanzamiento a partir de develop para preparar la versión para su lanzamiento:

```bash
git checkout -b release/nombre-de-la-version develop
```

En esta rama se pueden realizar pruebas finales y correcciones antes de la liberación.

5. Fusionar la rama de lanzamiento en master y develop y etiquetar la versión:

```bash
git checkout master
git merge --no-ff release/nombre-de-la-version
git tag -a nombre-de-la-version -m "Mensaje del tag"
git push origin master
git checkout develop
git merge --no-ff release/nombre-de-la-version
git push origin develop
```

6. Eliminar la rama de lanzamiento:

```bash
git branch -d release/nombre-de-la-version
git push origin --delete release/nombre-de-la-version
```

7. Crear una rama de corrección a partir de master en caso de encontrar un error en la versión liberada:

```bash
git checkout -b hotfix/nombre-del-error master
git checkout -b hotfix/nombre-del-error main
```

En esta rama se solucionará el error y se fusionará en master y develop.

8. Fusionar la rama de corrección en master y develop y etiquetar la versión corregida:

```bash
git checkout master
git merge --no-ff hotfix/nombre-del-error
git tag -a nombre-de-la-version-corregida -m "Mensaje del tag"
git push origin master
git checkout develop
git merge --no-ff hotfix/nombre-del-error
git push origin develop
```

9. Eliminar la rama de corrección:

```bash
git branch -d hotfix/nombre-del-error
git push origin --delete hotfix/nombre-del-error
```

# STEPS

1. Invitar colaborador
2. Colaborador acepta invitación
3. Colab. aplica clonar repo con:

```bash
git clone <dir/donde se encuentra el repo>
```

3. Colab. crea su rama:

```bash
git branch colab1
```

4. Colab. se para en su rama:

```bash
git checkout colab1
```

5. Job en nuestro code
6. Aplica:

```bash
git status
```

7. Los pasos para pushear:

```bash
git add .
git commit -m "message commit"
```

8. En esta instancia si queremos podemos volver a agragar cambios al code y repetir los pasos:

```bash
git add .
git commit -m "message new commit"
```

9. Ahora si queremos visualizar los commits realizados aplicamos:

```bash
git log
# o de una vista abreviada
git log --oneline
```

10. Podemos si necesitamos checkear las diferencia entre un commit y otro con:

```bash
git diff <codeCommit1> <codeCommit2>
```

11. Realizamos status de nuevo a modo de verificar que para los últimos cambios agregados (con el add) se le ha asignado un commit title

```bash
git status
```

## Steps IMPORTANT

12. Ahora nos pasamos a la rama principal nuestra

```bash
git checkout master
# o de haber asignado otra rama como la principal momentanea como develop, ir allí
git checkout develop
```

13. Previo a subir nuestro cambio realizamos una actualización con:

```bash
git pull origin develop
# en nuestro caso seguiremos como nuestra rama principal provisoria con la rama develop
```

14. Ahora debemos combinar lo que trabajamos en nuestra rama con la rama principal (que en nuestro caso es develop)

```bash
git merge colab1
# Recordar estar parado en la rama que para nosotros es la rama principal y tener actualizados los últimos cambios generales (que vienen de arriba, juju)
```

15. Y finalmente, continuando parados en la rama principal (en nuestro ejemplo la develop)

```bash
git push origin develop
```

## Ahora el otro (u otros) colaborador/es (colab2)

16. Para actualizar los cambios del colab1, debe:
    - Estando en la rama principal

```bash
git checkout develop
```

    - Hacer un pull (una actualización)

```bash
git pull origin develop
```

## CONFLIC \*\*\* Tener en cuenta que, si hacemos los cambios en la misma rama (rama principal) y en un mismo espacio de code

17. Para este caso si colab1 pushea esos cambios y luego intenta pushear el colab2 sin previamente actualizar, va a aparecer un cartel amarillo avisando que no tenemos los últimos cambios. Para ello se aconseja que:
    - colab2 realice
    ```bash
    git pull origin develop
    ```

    - Devuelve una advertencia, pero igualmente allí, ahora hacemos el push de nuevo:
    ```bash
    git push origin develop
    ```

    - Ahora nos dará otra advertencia de que no podemos hacer esa actualización, y para ello debemos resolver el conflicto desde el gitHub con la solución paso a paso de conflictos o desde nuestro propio code de la siguiente manera:
      - Detectando los errores (advertencias) y limpiando y dejando lo considerado correcto
      - Ahora solicitamos status
      ```bash
      git status
      ```

      - Y reiteramos hacer el add y commit desde nuestra rama colab2
      ```bash
      git add .
      git commit -m "refactor code ..."
      ```

      - Nos pasamos a la rama principal
      ```bash
      git checkout develop
      ```

      - Y pushear
      ```bash
      git push origin develop
      ```

---

## EXTRA

### Para el mensaje "develop | merge":

1. Primero, verificar el estado actual del repositorio con el comando:

```bash
git status
```

Si hay un merge en curso, Git indicará cuál es la rama en la que estamos trabajando actualmente y cuál es la rama que se está fusionando. También mostrará los archivos que han sido modificados y que necesitan ser resueltos.

2. Para completar el merge, se puede usar el comando:

```bash
git merge --continue
# o
git commit
```

Son para confirmar los cambios. Este comando completará el merge y creará un nuevo commit con los cambios fusionados.

3. Si por alguna razón el merge no se puede completar, puedes cancelar la operación con el comando:

```bash
git merge --abort.
```

### Para eliminar una rama usamos:

```bash
git branch -D colab1
```
