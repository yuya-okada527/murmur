#!/bin/bash

# コンテナのビルド
docker build -t murmur/fe-app ./frontend-app

# フロントエンドコンテナの立ち上げ
docker run -d --rm \
--name fe-app \
-p 8888:80 \
murmur/fe-app