# needed since the default shell is /bin/sh and this does not implement source
SHELL := /bin/bash

clean_venv:
	sudo rm -rf .venv

clean_container:
	sudo docker stop pgsql-dev
	sudo docker rm pgsql-dev
	sudo rm -rf pgsql-dev

venv:
	python3 -m venv .venv
	source $(shell pwd)/.venv/bin/activate
	pip install -r requirements.txt

# TODO: maybe we should clean the whole container first!
update_db:
	source .venv/bin/activate
	sudo docker restart pgsql-dev
	python write_all_challenges_to_db.py
