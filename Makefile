build:
	cd backend && $(MAKE) build
	cd database && $(MAKE) new

cleanup:
	docker image rm -f dataframetrainer-db-fill-or-update-tables
	docker image rm -f dataframetrainer-backend
	docker rm dataframetrainer-db-1
	docker volume rm -f dataframetrainer_sql

up:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up

up_test:
	docker compose -f docker-compose.yml up

recreate:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up --force-recreate
