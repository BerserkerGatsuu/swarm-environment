FROM nodered/node-red:latest

RUN npm install @meowwolf/node-red-contrib-amqp 
RUN npm install node-red-contrib-minio-all
RUN npm install ws
RUN npm install uuid

COPY settings.js /data/settings.js
COPY flows_cred.json /data/flows_cred.json

COPY flows.json /data/flows.json

