# bin/sh

echo "Running migrations..."
poetry run alembic upgrade head
echo "Starting server..."
poetry run litestar --app src.main:app run --host 0.0.0.0 --port 8000
