# needed since the default shell is /bin/sh and this does not implement source
SHELL := /bin/bash

venv:
	python3 -m venv .venv
	source $(shell pwd)/.venv/bin/activate && pip install -r requirements.txt && pip install -r requirements.dev.txt

run:
	flask --app server run

build:
	docker build . -t dftrainer-backend

# this does not yet work, the mounted files are recognized as directories if called from makefile
# if executed in the shell, everything works fine
run_container_debug:
	docker run -v $(shell pwd)/blueprint.py:/app/blueprint.py -v $(shell pwd)/server.py:/app/server.py -it dftrainer-backend bash
