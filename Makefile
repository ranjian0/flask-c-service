all: services

services:
	@cc -fPIC -shared -o services/sum.so services/sum.c
	@touch app.py  

run:
	gunicorn app:app --reload

.PHONY: services