build:
	cd backend && $(MAKE) build
	cd database && $(MAKE) new

cleanup:
	docker rm dataframetrainer-db-1
	docker rm dataframetrainer-backend-1
	docker rm dataframetrainer-adminer-1
	docker rm dataframetrainer-db-fill-or-update-tables-1  
	docker image rm -f dataframetrainer-db-fill-or-update-tables
	docker image rm -f dataframetrainer-backend
	docker volume rm -f dataframetrainer_sql

# By giving multiple config files as arguments the later ones override the previous ones
# In this case the dev and prod configs extend the base docker compose config
prod:
	docker compose -f docker-compose.yml -f docker-compose.prod.yml up

dev:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up

down:
	docker compose down -v --remove-orphans