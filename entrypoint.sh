#!/bin/sh

echo "Waiting for PostgreSQL to start..."

# Ожидание доступности БД
until nc -z -v -w30 db 5432
do
  echo "Waiting for database connection..."
  sleep 5
done

echo "Database is up, running migrations..."

if [ ! -d "migrations" ]; then
    flask db init
    flask db migrate -m "Initial migration"
fi

flask db upgrade

exec python app.py
