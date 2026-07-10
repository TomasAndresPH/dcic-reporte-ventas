@echo off
chcp 65001 >nul
title Reporte de Ventas DCIC
cd /d "%~dp0"

if not exist "venv\Scripts\python.exe" (
    echo(
    echo    No se encontro la instalacion.
    echo    Ejecuta primero INSTALAR_Reporte_Ventas.bat
    echo(
    pause
    exit /b 1
)

"venv\Scripts\python.exe" main.py
set "APP_EXIT=%errorlevel%"
if not "%APP_EXIT%"=="0" (
    echo(
    echo ============================================
    echo    La aplicacion se cerro con un error.
    echo    Revisa el mensaje de arriba y toma una captura.
    echo ============================================
    echo(
    pause
)
