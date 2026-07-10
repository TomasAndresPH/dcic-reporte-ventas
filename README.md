# Generador de Reporte de Ventas Consolidadas

App de escritorio simple que genera el Excel de **Ventas Consolidadas**
(Bsale + Wivo + Notas de Crédito + Notas de Débito) directamente desde la base
de datos. El usuario solo elige un **rango de fechas** y una **carpeta de
salida**, y la app genera el archivo.

Usa exactamente los mismos modelos, queries y cálculos que el backend original,
por lo que el resultado es idéntico al del sistema principal.

---

## Para el usuario final (instalación en 2 pasos)

El responsable te enviará **2 archivos**:

1. `INSTALAR_Reporte_Ventas.bat` — el instalador.
2. `credenciales_dcic.env` — las credenciales (guárdalo, lo necesitas 1 vez).

Pasos:

1. **Doble clic** en `INSTALAR_Reporte_Ventas.bat`.
2. Elige la carpeta donde quieres instalar la aplicación.
3. El instalador descarga todo, instala lo necesario y abre la app.
4. La **primera vez**, la app te pedirá el archivo de credenciales:
   selecciona `credenciales_dcic.env`. No se te volverá a pedir.

A partir de ahí, cada vez que quieras generar un reporte solo vuelve a
ejecutar `INSTALAR_Reporte_Ventas.bat`: detecta que ya está todo instalado,
no vuelve a preguntar nada y abre la app directamente.

> **Requisito:** tener **Python** instalado (el instalador te avisa y abre la
> página de descarga si falta) y **acceso de red a la base de datos**.

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
├── INSTALAR_Reporte_Ventas.bat   # Instalador todo-en-uno (para usuarios)
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
