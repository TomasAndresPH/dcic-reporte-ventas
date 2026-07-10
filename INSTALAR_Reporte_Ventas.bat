@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul
title Instalador - Reporte de Ventas DCIC

REM ============================================================
REM   CONFIGURACION
REM ============================================================
set "REPO_URL=https://github.com/TomasAndresPH/dcic-reporte-ventas.git"
set "BRANCH=main"
set "APP_DIR_NAME=dcic-reporte-ventas"
set "CFG_DIR=%LOCALAPPDATA%\DcicReporteVentas"
set "CFG_FILE=%CFG_DIR%\ruta_instalacion.txt"
REM ============================================================

echo(
echo ============================================
echo    Reporte de Ventas DCIC - Instalador
echo ============================================
echo(

REM ------------------------------------------------------------
REM  1. Verificar Python
REM ------------------------------------------------------------
echo [1/5] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo(
    echo    ERROR: Python no esta instalado o no esta en el PATH.
    echo    Descargalo desde https://www.python.org/downloads/
    echo    IMPORTANTE: marca "Add Python to PATH" al instalar.
    echo(
    start "" https://www.python.org/downloads/
    pause
    exit /b 1
)
for /f "delims=" %%v in ('python --version') do echo    OK - %%v

REM ------------------------------------------------------------
REM  2. Determinar carpeta de instalacion
REM     (si ya se instalo antes, se reutiliza sin preguntar)
REM ------------------------------------------------------------
echo [2/5] Ubicacion de la aplicacion...
set "APP_DIR="

if exist "%CFG_FILE%" (
    set /p SAVED_DIR=<"%CFG_FILE%"
    if exist "!SAVED_DIR!\main.py" (
        set "APP_DIR=!SAVED_DIR!"
        echo    Usando instalacion existente:
        echo    !APP_DIR!
    )
)

if not defined APP_DIR (
    echo    Selecciona la carpeta donde instalar la aplicacion...
    for /f "usebackq delims=" %%d in (`powershell -NoProfile -Command "Add-Type -AssemblyName System.Windows.Forms; $f=New-Object System.Windows.Forms.FolderBrowserDialog; $f.Description='Elige donde instalar el Reporte de Ventas'; if($f.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK){$f.SelectedPath}"`) do set "BASE_DEST=%%d"
    if not defined BASE_DEST (
        echo    Cancelado por el usuario.
        pause
        exit /b 1
    )
    set "APP_DIR=!BASE_DEST!\%APP_DIR_NAME%"
    echo    Carpeta: !APP_DIR!
)

REM ------------------------------------------------------------
REM  3. Descargar / actualizar el repositorio
REM ------------------------------------------------------------
echo [3/5] Obteniendo la aplicacion...
if exist "%APP_DIR%\main.py" (
    echo    Ya existe. Se conserva la instalacion actual.
) else (
    where git >nul 2>&1
    if !errorlevel! == 0 (
        echo    Descargando con git...
        git clone -b %BRANCH% "%REPO_URL%" "%APP_DIR%"
    ) else (
        echo    git no encontrado. Descargando ZIP...
        set "ZIP_URL=%REPO_URL:.git=%/archive/refs/heads/%BRANCH%.zip"
        set "ZIP_TMP=%TEMP%\dcic_app.zip"
        set "EXT_TMP=%TEMP%\dcic_app_extract"
        if exist "!EXT_TMP!" rmdir /s /q "!EXT_TMP!"
        powershell -NoProfile -Command "try { Invoke-WebRequest -Uri '!ZIP_URL!' -OutFile '!ZIP_TMP!'; Expand-Archive -Path '!ZIP_TMP!' -DestinationPath '!EXT_TMP!' -Force } catch { exit 1 }"
        if errorlevel 1 (
            echo    ERROR al descargar el ZIP. Revisa tu conexion.
            pause
            exit /b 1
        )
        powershell -NoProfile -Command "$s=Get-ChildItem -Directory '!EXT_TMP!' | Select-Object -First 1; New-Item -ItemType Directory -Force -Path (Split-Path '%APP_DIR%') | Out-Null; Move-Item -Force $s.FullName '%APP_DIR%'"
        del "!ZIP_TMP!" >nul 2>&1
    )
)

if not exist "%APP_DIR%\main.py" (
    echo(
    echo    ERROR: no se pudo descargar la aplicacion.
    echo    Posibles causas:
    echo      - Sin conexion a internet.
    echo      - El repositorio no es accesible (debe ser publico).
    echo    Avisa al responsable si el problema persiste.
    echo(
    pause
    exit /b 1
)

REM Guardar la ruta para no volver a preguntar la proxima vez
if not exist "%CFG_DIR%" mkdir "%CFG_DIR%"
> "%CFG_FILE%" echo %APP_DIR%

REM ------------------------------------------------------------
REM  4. Entorno virtual + dependencias
REM ------------------------------------------------------------
cd /d "%APP_DIR%"
echo [4/5] Preparando dependencias...
if not exist "venv\Scripts\python.exe" (
    echo    Creando entorno virtual...
    python -m venv venv
)

if exist ".deps_ok" (
    echo    Dependencias ya instaladas.
) else (
    echo    Instalando dependencias (solo la primera vez, puede tardar)...
    "venv\Scripts\python.exe" -m pip install --upgrade pip >nul
    "venv\Scripts\python.exe" -m pip install -r requirements.txt
    if errorlevel 1 (
        echo    ERROR instalando dependencias.
        pause
        exit /b 1
    )
    > ".deps_ok" echo ok
)

REM ------------------------------------------------------------
REM  5. Crear acceso directo en el escritorio
REM ------------------------------------------------------------
echo [5/5] Creando acceso directo en el escritorio...
set "LAUNCHER=%APP_DIR%\Ejecutar_Reporte_Ventas.bat"
set "ICONO=%APP_DIR%\dcic.ico"
if exist "%ICONO%" (
    set "ICON_LINE=$s.IconLocation='%ICONO%';"
) else (
    set "ICON_LINE="
)
powershell -NoProfile -Command "$s=(New-Object -ComObject WScript.Shell).CreateShortcut([Environment]::GetFolderPath('Desktop')+'\Reporte de Ventas.lnk'); $s.TargetPath='%LAUNCHER%'; $s.WorkingDirectory='%APP_DIR%'; !ICON_LINE! $s.Save()"

echo(
echo ============================================
echo    Instalacion completa.
echo(
echo    Abre la aplicacion con el icono del escritorio:
echo       "Reporte de Ventas"
echo(
echo    (La primera vez te pedira el archivo de
echo     credenciales; solo esa vez.)
echo ============================================
echo(
pause

endlocal
