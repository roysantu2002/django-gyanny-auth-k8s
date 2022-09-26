"""
"""

import os
import pathlib

import dotenv
from django.core.wsgi import get_wsgi_application

CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
ENV_FILE_PATH = os.path.join(BASE_DIR, ".env")

dotenv.read_dotenv(str(ENV_FILE_PATH))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gyanny_k8s.settings')
application = get_wsgi_application()
