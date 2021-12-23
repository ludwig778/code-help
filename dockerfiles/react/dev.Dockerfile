FROM node:17.2.0-bullseye-slim

RUN mkdir /app && chown -R node:node /app

ENV PATH=$PATH:/app/node_modules/.bin
USER node
WORKDIR /app

COPY --chown=node:node package.json package-lock.json ./
RUN npm install

COPY . .

ENTRYPOINT ["npm", "run"]
