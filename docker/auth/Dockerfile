# docker/backend/Dockerfile

FROM python:3.8.3-alpine

WORKDIR /app
ADD . /app

# ADD ./django-auth/requirements.txt /app/django-auth/
#

RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r django-auth/requirements.txt



# add execute rights
RUN chmod +x /app/docker/auth/wsgi-entrypoint.sh