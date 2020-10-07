FROM node:14.9.0-buster-slim

WORKDIR /app
COPY package.json .
RUN npm install
ENV PATH /app/node_modules/.bin:$PATH

ENTRYPOINT ["npm", "run"]
CMD ["dev"]
