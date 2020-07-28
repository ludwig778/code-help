FROM python:3.8-slim-buster

RUN mkdir -p /usr/share/man/man1 && \
    mkdir -p /usr/share/man/man7 && \
    apt-get update && \
    apt-get install --yes --no-install-recommends \
    	make postgresql-client && \
    rm -rf /var/lib/apt/lists/*

RUN adduser --system --uid 1000 --disabled-password --gecos '' my_user
USER my_user

RUN mkdir /my_app/
WORKDIR /my_app/

ENV PATH=/usr/local/bin:/usr/bin:/home/my_user/.local/bin:/bin

COPY requirements.txt /tmp/
RUN pip install --no-cache --user --requirement /tmp/requirements.txt

COPY --chown=my_user:nogroup . .

ENTRYPOINT ["make"]
CMD ["run_dev"]
