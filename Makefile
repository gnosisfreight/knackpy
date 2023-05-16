all: install selfcheck build test

install:
	poetry install

selfcheck:
	poetry check

build:
	poetry build

patch:
	poetry version patch

minor:
	poetry version minor

major:
	poetry version major

test:
	@python test.py

.PHONY: install selfcheck build all test