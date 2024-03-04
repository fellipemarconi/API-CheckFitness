# Comands
DOCKER_COMPOSE=docker-compose
PYTHON_MANAGE=python3 manage.py

# Build the containers
build:
	$(DOCKER_COMPOSE) build

# Start the application
up:
	$(DOCKER_COMPOSE) up 

# Stop the application
down:
	$(DOCKER_COMPOSE) down

# Clean in containers and volumes
clean:
	$(DOCKER_COMPOSE) down -v --remove-orphans

# Make migrations in Django
makemigrations:
	$(DOCKER_COMPOSE) run --rm web $(PYTHON_MANAGE) makemigrations

# Migrate in Django
migrate:
	$(DOCKER_COMPOSE) run --rm web $(PYTHON_MANAGE) migrate

# Create a super user in Django
createsuperuser:
	$(DOCKER_COMPOSE) run --rm web $(PYTHON_MANAGE) createsuperuser

# Collect the static files in Django
collectstatic:
	$(DOCKER_COMPOSE) run --rm web $(PYTHON_MANAGE) collectstatic --noinput

help:
	@echo "Usage: make <target>"
	@echo "Available targets:"
	@echo "  help               - Display this help message"
	@echo "  build              - Build Docker images"
	@echo "  up                 - Start the application"
	@echo "  down               - Stop the application"
	@echo "  clean              - Clean up Docker containers and volumes"
	@echo "  makemigrations     - Run Django makemigrations"
	@echo "  migrate            - Run Django migrations"
	@echo "  createsuperuser    - Create Django superuser"
	@echo "  collectstatic      - Collect Django static files"

# Define the commands that not be a name of files
.PHONY: help build up down clean makemigrations migrate createsuperuser collectstatic
