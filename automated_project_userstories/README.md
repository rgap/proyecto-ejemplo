## 0. Requisitos

Necesitas tener instalado:

* GitHub CLI (`gh`)
* Python 3 o superior.
* Una cuenta de GitHub
* Un repositorio ya creado en GitHub: Nombrarlo ProyectoDevOps

---

## 1. Instalar `gh`

### En macOS

Abre **Terminal** y ejecuta:

```bash
brew install gh
```

GitHub recomienda Homebrew como instalación oficial en macOS.

Verifica:

```bash
gh --version
```

### En Windows

Abre **PowerShell** y ejecuta:

```powershell
winget install --id GitHub.cli --source winget
```

GitHub recomienda WinGet como instalación oficial en Windows. Después de instalar, abre una **nueva ventana** de Windows Terminal o PowerShell para que funcione el PATH.

Verifica:

```powershell
gh --version
```

---

## 2. Iniciar sesión en GitHub

Ejecuta:

```bash
gh auth login
```

Selecciona una opcione similar a esta:

```txt
Login with browser
```

Luego verifica que la sesión esté activa:

```bash
gh auth status
```
---

## 3. Crear el archivo CSV

Crea un archivo llamado:

```txt
user_stories.csv
```

---

## 4. Explicación de los headers del CSV

| Header                 | Significado                                       |
| ---------------------- | ------------------------------------------------- |
| `titulo`               | Título del Issue en GitHub                        |
| `rol`                  | Usuario o actor de la historia                    |
| `quiero`               | Acción que quiere realizar el usuario             |
| `para`                 | Razón o valor de la historia                      |
| `criterios_aceptacion` | Condiciones para considerar terminada la historia |
| `tareas_tecnicas`      | Tareas de desarrollo necesarias                   |

Ejemplo:

```csv
titulo,rol,quiero,para
"Login de cliente","cliente","iniciar sesión","acceder a mi cuenta"
```

Se convertirá en:

```md
## Historia de usuario

Como cliente,
quiero iniciar sesión,
para acceder a mi cuenta.
```

---

## 5. Crear el script en Python

Crea un archivo llamado:

```txt
import_user_stories.py
```

Crear un entorno virtual de python, si no lo tienes creado, crea uno.

En MacOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

En Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 6. Configurar el repositorio

En el script, cambia esto:

```python
OWNER = "tu_usuario"
REPO = "tu_repositorio"
```

Por los datos reales de tu repositorio.

Por ejemplo, si tu repositorio es:

```txt
https://github.com/rgap/proyecto-ejemplo
```

Entonces debes usar:

```python
OWNER = "rgap"
REPO = "proyecto-ejemplo"
```

---

## 7. Ejecutar el script

### En macOS

```bash
python3 import_user_stories.py
```

### En Windows

```powershell
python import_user_stories.py
```

---

## 8. Resultado esperado

Cada fila del CSV crea un Issue con esta estructura:

```md
## Historia de usuario

Como cliente,
quiero iniciar sesión,
para acceder a mi cuenta.

## Criterios de aceptación

- [ ] El usuario puede ingresar email y contraseña.
- [ ] El sistema valida credenciales incorrectas.
- [ ] El sistema redirige al dashboard si el login es correcto.

## Tareas técnicas

- [ ] Crear formulario de login.
- [ ] Crear endpoint POST /login.
- [ ] Guardar sesión o token.
```

---

## 9. Crear el GitHub Project manualmente

Después de crear los Issues, puedes crear el Project desde GitHub web:

```txt
Repositorio
→ Projects
→ New project
→ Board
```

Luego agregas los issues al Project.

```txt
Project
→ Add item
→ Select from repository
→ Selecciona los Issues
```

Organiza el tablero con columnas:

```txt
Backlog
Ready
In Progress
Review
Done
```

---

## 10. Errores comunes

### Error: `gh: command not found`

Significa que GitHub CLI no está instalado o no está en el PATH.

Verifica con:

```bash
gh --version
```

---

### Error: no estás autenticado

Ejecuta:

```bash
gh auth login
```

---

### Error: repositorio incorrecto

Revisa estas líneas del script:

```python
OWNER = "tu_usuario"
REPO = "tu_repositorio"
```

Deben coincidir con la URL del repositorio:

```txt
https://github.com/OWNER/REPO
```

