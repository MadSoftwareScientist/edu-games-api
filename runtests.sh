#!/bin/bash

docker-compose.exe run server sh -c "python manage.py test && flake8"