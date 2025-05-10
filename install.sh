#! /bin/bash

echo "[Info] Installing dependencies..."
pip install -r requirements.txt

echo "[Info] Installing Tailwind..."
python manage.py tailwind install
python manage.py tailwind build

echo "[Info] Collecting static files..."
python manage.py collectstatic --noinput

echo "[Info] Applying migrations..."
python manage.py makemigrations && python manage.py migrate

echo "[Info] Ready to go! Superuser not created yet." 