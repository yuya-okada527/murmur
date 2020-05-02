#!/bin/bash

# DBへの接続情報を引数から取得
DB_USER=$1
DB_PASSWORD=$2
DB_NAME=murmur
DB_HOST=localhost

DB_URL=postgresql://${DB_HOST}:5432/${DB_NAME}

echo ${DB_URL}

# バックエンドコンテナの立ち上げ
docker run -d --rm \
--name backend-api \
-p 8080:80 \
-e DB_USER=${DB_USER} \
-e DB_PASSWORD=${DB_PASSWORD} \
-e DB_URL=${DB_URL} \
murmur/backend-app
