#!/bin/sh

# stop script if error
set -e

# if [ "$DATABASE" = "postgres" ]
# then
echo "Waiting for postgres..."

# while ! nc -z $DB_HOST; do
#   sleep 0.1
# done

echo "PostgreSQL started"
# fi

cd /app
# pip install --no-cache-dir -r requirements.txt
echo "[docker-entrypoint.sh] run flask db upgrade"
flask db upgrade

echo "[docker-entrypoint.sh] run flask configure-db"
flask configure-db

echo "ENVIRONMENT IS: $FLASK_ENV"
echo "[docker-entrypoint.sh] Start APP"

if [ "$FLASK_ENV" = "prod" ]; then
    python run.py
else
    echo "We are not in prod environment, so don't start the app."
fi

echo "[docker-entrypoint.sh] FINISH container setup"

# echo "[docker-entrypoint.sh] Start APP"

# python run.py

exec "$@"