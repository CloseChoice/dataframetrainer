build:
	cd backend && $(MAKE) build
	cd database && $(MAKE) new

cleanup_prod:
	docker rm -f prod-frontend-prod
	docker image rm -f prod-frontend-prod
	docker rm -f prod-backend
	docker image rm -f prod-backend
	docker rm -f prod-db-fill-or-update-tables
	docker image rm -f prod-db-fill-or-update-tables

cleanup_test:
	docker rm -f test-frontend-prod
	docker image rm -f test-frontend-prod
	docker rm -f test-backend
	docker image rm -f test-backend
	docker rm -f test-db-fill-or-update-tables
	docker image rm -f test-db-fill-or-update-tables

cleanup:
	docker rm -f dataframetrainer-db-fill-or-update-tables-1
	docker rm -f dataframetrainer-frontend-prod-1
	docker rm -f dataframetrainer-db-1
	docker rm -f dataframetrainer-backend-1
	docker rm -f dataframetrainer-adminer-1
	docker rm -f dataframetrainer-frontend-dev-1
	docker image rm -f dataframetrainer-frontend-prod
	docker image rm -f dataframetrainer-db-fill-or-update-tables
	docker image rm -f dataframetrainer-backend
	docker image rm -f dataframetrainer-frontend-dev
	docker rm dataframetrainer-db-1
	docker volume rm -f dataframetrainer_postgres
	docker volume rm -f dataframetrainer_sql


# By giving multiple config files as arguments the later ones override the previous ones
# In this case the dev and prod configs extend the base docker compose config
prod:
	docker compose -f docker-compose.yml -f docker-compose.prod.yml up

prod_detached:
	docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

test:
	docker compose -f docker-compose.yml -f docker-compose.test.yml up

test_detached:
	docker compose -f docker-compose.yml -f docker-compose.test.yml up -d

dev:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up

down:
	docker compose down -v --remove-orphans

up:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up

up_test:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml -f docker-compose.testing.yml up

recreate:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up --force-recreate
