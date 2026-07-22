# Generador de Reporte de Ventas Consolidadas

App de escritorio simple que genera el Excel de **Ventas Consolidadas**
(Bsale + Wivo + Notas de Crédito + Notas de Débito) directamente desde la base
de datos. El usuario solo elige un **rango de fechas** y una **carpeta de
salida**, y la app genera el archivo.

Usa exactamente los mismos modelos, queries y cálculos que el backend original,
por lo que el resultado es idéntico al del sistema principal.

---

## Para el usuario final

El responsable te enviará **2 archivos**:

1. `INSTALAR_Reporte_Ventas.bat` — el instalador (se usa una sola vez).
2. `credenciales_dcic.env` — las credenciales (guárdalo, lo necesitas 1 vez).

### Instalar (una sola vez)

1. **Doble clic** en `INSTALAR_Reporte_Ventas.bat`.
2. Elige la carpeta donde quieres instalar la aplicación.
3. El instalador descarga todo, instala lo necesario y crea un acceso directo
   **"Reporte de Ventas"** en el escritorio.

### Usar (cada vez que quieras un reporte)

1. **Doble clic** en el icono **"Reporte de Ventas"** del escritorio.
2. La **primera vez** te pedirá el archivo de credenciales: selecciona
   `credenciales_dcic.env`. No se te volverá a pedir.
3. Elige el rango de fechas y la carpeta de salida, y pulsa **Generar Excel**.

### Si te envían credenciales nuevas

Si cambia el servidor de la base de datos (o cualquier dato de conexión), pulsa
**"Actualizar credenciales"** en la ventana de la app y selecciona el archivo
nuevo. La app se cerrará; vuelve a abrirla y listo. No hay que reinstalar.

### Si te avisan que hay una versión nueva de la app

Vuelve a ejecutar `INSTALAR_Reporte_Ventas.bat`: detecta la instalación
existente y la actualiza en el mismo lugar. **No** borra tus credenciales ni te
vuelve a pedir la carpeta.

> **Requisito:** tener **Python** instalado (el instalador te avisa y abre la
> página de descarga si falta) y **acceso de red a la base de datos**.

> **Separación de responsabilidades:** `INSTALAR_Reporte_Ventas.bat` solo
> instala; `Ejecutar_Reporte_Ventas.bat` (dentro de la carpeta instalada, y al
> que apunta el acceso directo) es el que abre la app.

---

## Para desarrolladores (ejecución manual)

```bash
# 1. Crear y activar entorno virtual
python -m venv venv
venv\Scripts\Activate.ps1        # Windows PowerShell
# source venv/bin/activate       # macOS / Linux

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar
python main.py
```

La primera ejecución pide el archivo de credenciales y lo guarda como `.env`
en esta carpeta. También puedes crear el `.env` a mano a partir de
`.env.example`.

---

## Uso

1. Selecciona la **Fecha de Inicio** y la **Fecha de Fin**.
2. Pulsa **Examinar...** y elige la carpeta donde guardar el Excel.
3. Pulsa **Generar Excel**.

El archivo se guarda como `Ventas-DD-MM-YYYY_al_DD-MM-YYYY.xlsx`.

---

## Notas técnicas

- La fuente de datos está fijada en `Testing` (los modelos por defecto del
  backend). Para usar `Cyber`, cambia `data_source='Testing'` por `'Cyber'`
  en [`main.py`](main.py).
- Por defecto se exportan **todas** las columnas del reporte.
- Los archivos `.env` y `credenciales_dcic.env` **no se suben al repositorio**
  (contienen credenciales); están en `.gitignore`.

## Estructura del proyecto

```
.
├── INSTALAR_Reporte_Ventas.bat   # Instalador / actualizador (descarga + venv + deps + acceso directo)
├── Ejecutar_Reporte_Ventas.bat   # Lanzador de la app (al que apunta el acceso directo)
├── dcic.ico                      # Icono del acceso directo
├── credenciales_dcic.env         # Credenciales (NO se sube; se envía aparte)
├── main.py                       # App de escritorio (GUI) + first-run + Django
├── reporte.py                    # Queries y generación del Excel
├── config/
│   └── settings.py               # Configuración mínima de Django (lee .env)
├── dcic_operations/
│   ├── apps.py
│   └── models.py                 # Modelos (copia del backend, solo lectura)
├── requirements.txt
├── .env.example
└── README.md
```
