"""
Configuración mínima de Django para el generador de Reporte de Ventas.

Solo se necesita lo indispensable para poder leer los modelos de
`dcic_operations` desde la base de datos PostgreSQL. No hay servidor web,
ni migraciones, ni apps extra: es una app de escritorio que lee la BD.
"""
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables de entorno desde .env (en la raíz del proyecto)
load_dotenv(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = os.getenv('SECRET_KEY', 'reporte-ventas-standalone-key-no-secreta')

DEBUG = True

USE_TZ = True
TIME_ZONE = 'UTC'
USE_I18N = True
LANGUAGE_CODE = 'en-us'

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'dcic_operations',
]

# Base de datos: misma que el backend. Se configura vía .env.
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', ''),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
