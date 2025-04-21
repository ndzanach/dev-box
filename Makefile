# Variables
DC = docker compose

# Build all agents
build:
	$(DC) build
	$(DC) up -d 

# Run all agents
up:
	$(DC) up -d

# Stop all agents
down:
	$(DC) down

# Show logs for all
logs:
	$(DC) logs -f --tail=100

# Rebuild and restart all
restart: down build up

