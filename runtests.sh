#!/bin/bash

docker-compose.exe run --rm server sh -c "python manage.py test && flake8"
