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
