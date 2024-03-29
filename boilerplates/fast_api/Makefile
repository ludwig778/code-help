ARGS = $(filter-out $@,$(MAKECMDGOALS))


default: run_dev_server

wait_for_db:
	until pg_isready -h ${POSTGRES_HOST}; do sleep 1; done 1>/dev/null

migrate: wait_for_db
	alembic upgrade head

run_dev_server: migrate
	poetry run uvicorn app.main:get_app --host 0.0.0.0 --reload --access-log --factory

run_prod_server: migrate
	poetry run uvicorn app.main:get_app --host 0.0.0.0 --factory ${ARGS}

sh:
	bash

py:
	poetry run ipython

lint:
	poetry run flake8

isort:
	poetry run isort hartware_lib/ tests/

black:
	black .

mypy:
	poetry run mypy app/

tests:
	pytest

test_on:
	pytest ${ARGS}

sure: tests lint mypy isort black

clean:
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	find . -name "*.pyc" -o -name "__pycache__"|xargs rm -rf

.PHONY: tests
