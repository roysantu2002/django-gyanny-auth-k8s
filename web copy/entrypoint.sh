#!/bin/sh

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"gyanny@gyanny.com"}
cd /app/

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# run gunicorn
gunicorn gyanny_k8s.wsgi:application --bind 0.0.0.0:$PORT


# python manage.py flush --no-input
# python manage.py migrate

# python manage.py wait_for_db
# python manage.py migrate
# python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true

exec "$@"