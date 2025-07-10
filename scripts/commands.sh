#!/bin/sh

# Encerra o script se qualquer comando falhar
set -e

while ! pg_isready -h $POSTGRES_HOST -p $POSTGRES_PORT -q; do
  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
  sleep 2
done

echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"

# --- ETAPA DE SETUP (como root) ---
# O usuário root tem permissão para escrever na pasta de estáticos.
echo "🚀 Running production setup..."
python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# --- ETAPA DE EXECUÇÃO (como duser) ---
echo "✅ Setup complete. Starting Gunicorn server..."
exec gunicorn project.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --user=duser \
    --group=duser