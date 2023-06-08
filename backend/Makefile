# needed since the default shell is /bin/sh and this does not implement source
SHELL := /bin/bash

venv:
	python3 -m venv .venv
	source $(shell pwd)/.venv/bin/activate
	pip install -r requirements.txt

run:
	flask --app server run 