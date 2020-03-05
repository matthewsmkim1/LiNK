
FROM node:latest
RUN mkdir -p /usr/src/server
WORKDIR /usr/src/server
COPY server/package.json /usr/src/server/
RUN npm install
COPY server /usr/src/server
EXPOSE 8080
RUN npm install -g nodemon 
CMD ["npm", "run", "dev"]