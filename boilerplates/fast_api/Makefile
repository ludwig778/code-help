default: run_dev_server

wait_for_db:
	until pg_isready -h ${POSTGRES_HOST}; do sleep 1; done 1>/dev/null

migrate: wait_for_db
	alembic upgrade head

run_dev_server: migrate
	poetry run uvicorn app.main:get_app --host 0.0.0.0 --reload --access-log --factory

st: wait_for_db
	 #PGPASSWORD=${POSTGRES_PASSWORD} psql -h db -U fastapi -c "\dt"
	 PGPASSWORD=${POSTGRES_PASSWORD} psql -h db -U fastapi -c 'select * from "user";'

sh:
	bash

py:
	poetry run ipython

lint:
	poetry run flake8

black:
	black --line-length 125 .

tests: migrate
	pytest -vvss .

clean:
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	find . -name "*.pyc" -o -name "__pycache__"|xargs rm -rf

.PHONY: tests
