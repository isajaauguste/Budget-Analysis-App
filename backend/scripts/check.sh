#!/usr/bin/env bash
set -e

echo "Formatting..."
poetry run black .

echo "Linting..."
poetry run ruff check . --fix

echo "Type checking..."
poetry run mypy .