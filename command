docker-compose run django django-admin startproject core .
docker exec -it postgres psql -U postgres

docker-compose up / down

Postgres
==========

docker exec -it gyanny-pgdb psql -U postgres
\c <database_name>
\d
\d+ <table_name>
\q


==========
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'pgdb',
        'PORT': 5432,
    }
}