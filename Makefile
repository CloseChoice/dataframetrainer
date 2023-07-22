build:
	cd backend && $(MAKE) build
	cd database && $(MAKE) new

cleanup:
	docker image rm -f dataframetrainer-db-fill-or-update-tables
	docker image rm -f dataframetrainer-backend
	docker volume rm -f dataframetrainer_sql
	
