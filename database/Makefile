# needed since the default shell is /bin/sh and this does not implement source
SHELL := /bin/bash

.PHONY : clean_venv clean_container venv update_db run_debug new

clean_venv:
	sudo rm -rf .venv

clean_container:
	docker stop pgsql-test
	docker rm pgsql-test

venv:
	python3 -m venv .venv
	source $(shell pwd)/.venv/bin/activate && python -m pip install -r requirements.txt

update_db:
	./create_container.sh

run_debug:
	docker run -p 5434:5432 --mount src=dftrainer_db,dst=/var/lib/postgresql/data postgres:15.3

clean: clean_venv clean_container venv update_db
new: venv update_db