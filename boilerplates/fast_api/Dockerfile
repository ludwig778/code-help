FROM python:3.9-slim-buster

ENV DEBIAN_FRONTEND noninteractive

RUN apt update -y && \
    apt install -y \
      make \
      curl \
      libpq-dev \
      postgresql-client \
      inotify-tools \
    && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 - && \
    rm -rf /var/lib/apt/lists/

WORKDIR /app

ENV PATH=$PATH:/root/.poetry/bin/

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install

COPY . .

ENTRYPOINT ["make"]
