"""

"""
import os
from datetime import timedelta
from pathlib import Path

import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = str(os.environ.get('DEBUG')) == "1"
DEBUG = int(os.environ.get("DEBUG", default=0))

ENV_ALLOWED_HOST = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
# ALLOWED_HOSTS = ['auth-core-app.herokuapp.com', 'localhost', '127.0.0.1']
ALLOWED_HOSTS = []

if ENV_ALLOWED_HOST:
    ALLOWED_HOSTS = ENV_ALLOWED_HOST

print(ALLOWED_HOSTS)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'api',
    'accounts',
    'corsheaders',
    'core'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',

]

ROOT_URLCONF = 'gyanny_k8s.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gyanny_k8s.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}
#
# DB_USERNAME = os.environ.get('POSTGRES_USER')
# DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
# DB_DATABASE = os.environ.get('POSTGRES_DB')
# DB_HOST = os.environ.get('POSTGRES_HOST')
# DB_PORT = os.environ.get('POSTGRES_PORT')
#
# print(DB_DATABASE, DB_HOST, DB_PASSWORD, DB_PORT, DB_USERNAME)
# DB_IS_AVAIL = all([
#     DB_USERNAME,
#     DB_PASSWORD,
#     DB_DATABASE,
#     DB_HOST,
#     DB_PORT
# ])
#
# # POSTGRES_READY = str(os.environ.get('POSTGRES_READY')) == 1
#
# # if DB_IS_AVAIL and POSTGRES_READY:
#
# print(DB_IS_AVAIL)
# if DB_IS_AVAIL:
#      DATABASES = {
#         'default': {
#             'ENGINE': os.environ.get("SQL_ENGINE"),
#             'NAME': DB_DATABASE,
#             'HOST': DB_HOST,
#             'PORT': DB_PORT,
#             'USER': DB_USERNAME,
#             'PASSWORD': DB_PASSWORD
#         }
#     }

# print(os.environ.get('DATABASE_URL'))

if os.environ.get('DATABASE_URL'):

   print('DATABASE_URL')
   DATABASE_URL = os.environ.get('DATABASE_URL')
   db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
   DATABASES['default'].update(db_from_env)
   print('Done')
#     DATABASE_URL = os.environ.get('DATABASE_URL')
#     DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}
#
#     print('connecting external db')
#     # DATABASES['default'] = os.environ.get('DATABASE_URL')
#     DATABASES['default']['CONN_MAX_AGE'] = 500

    # db_from_env = dj_database_url.config()
    # DATABASES['default'].update(db_from_env)
    # DATABASES['default']['CONN_MAX_AGE'] = 500

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 3
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = ['http://127.0.0.1:8000', 'http://localhost:3000', 'http://localhost:8000', 'http://localhost:8081']

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_TMP = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model
AUTH_USER_MODEL = 'accounts.CustomUser'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    # 'USER_ID_FIELD': 'email',
    # 'USER_ID_CLAIM': 'email',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    # 'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    # 'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    # 'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
