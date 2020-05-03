#!/bin/bash

# DBへの接続情報を引数から取得
DB_USER=$1
DB_PASSWORD=$2

# コンテナのビルド
docker build -t murmur/backend-app ../backend-app

# バックエンドコンテナの立ち上げ
docker run -d --rm \
--name backend-api \
-p 8080:80 \
-e DB_USER=${DB_USER} \
-e DB_PASSWORD=${DB_PASSWORD} \
murmur/backend-app
