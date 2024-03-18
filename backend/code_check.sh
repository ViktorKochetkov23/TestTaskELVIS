#!/bin/bash
pycodestyle src/ --exclude 'alembic'
pylint src/ --ignore='alembic'
mypy src/ --exclude 'alembic'
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
find . | grep -E "(.mypy_cache)$" | xargs rm -rf

read -p 'Press [Enter] key to continue...'