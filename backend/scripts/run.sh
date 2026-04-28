#!/usr/bin/env bash

# Exit immediately if any command fails
set -e

echo "Applying migrations..."
poetry run alembic upgrade head

echo "Starting development server..."
poetry run uvicorn main:app --reload