FROM node:12 as build

WORKDIR /home/node/app
COPY package*.json /home/node/app/
RUN echo -n "node "; node -v; \
    echo -n "npm "; npm -v; \
    npm install --production

COPY src /home/node/app/src/
COPY public /home/node/app/public/
RUN npm run build

FROM nginx:alpine

RUN echo "nginx:alpine" > /docker-image-tag && cat /docker-image-tag
COPY --from=build /home/node/app/build /usr/share/nginx/html

WORKDIR /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
