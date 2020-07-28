FROM node:13-buster-slim as build

WORKDIR /my_app
ADD package.json .
RUN npm install

ADD . .

RUN npm run build:${ENV}

FROM nginx:1.16

WORKDIR /usr/share/nginx/html/
COPY nginx/default.conf /etc/nginx/conf.d/
COPY --from=build /my_app/build/html .
