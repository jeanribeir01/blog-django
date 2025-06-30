#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

while ! pg_isready -h $POSTGRES_HOST -p $POSTGRES_PORT -q; do
  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
  sleep 2
done

echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"

python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
gunicorn project.wsgi --bind 0.0.0.0:8000