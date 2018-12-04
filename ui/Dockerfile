FROM node:8.14.0-stretch as builder
RUN mkdir -p /app
WORKDIR /app
COPY package.json /app
RUN npm install
COPY webpack.config.js /app
COPY src /app/src
ARG API_URL=http://bitrate.goldshtein.org
RUN npm run build -- --define "API_URL='$API_URL'"

FROM nginx:1.15.7-alpine
RUN rm -rf /usr/share/nginx/html/*
COPY index.html /usr/share/nginx/html/index.html
COPY --from=builder /app/bundle.js /usr/share/nginx/html/bundle.js
