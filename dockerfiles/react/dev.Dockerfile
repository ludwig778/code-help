FROM node:13-buster-slim

RUN apt update && \
    apt install -y make && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /my_app
COPY package.json .

RUN npm install

ENV PATH /my_app/node_modules/.bin:$PATH

ENTRYPOINT ["make"]
CMD ["run_dev"]
