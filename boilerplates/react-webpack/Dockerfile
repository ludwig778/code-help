FROM node:16.8.0-buster-slim

WORKDIR /app/

ENV PATH=$PATH:./node_modules/.bin/

COPY package.json package-lock.json ./
RUN npm install

COPY . .

CMD ["npm", "run"]
