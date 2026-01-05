#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Upgrading pip..."
python -m pip install --upgrade pip

echo "Installing requirements..."
pip install -r requirements.txt

echo "Collecting static..."
python manage.py collectstatic --no-input

echo "Migrating..."
python manage.py migrate
