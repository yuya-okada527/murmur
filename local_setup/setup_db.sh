#!/bin/bash

# PSQLの設定を引数から取得
POSTGRES_USER=$1
POSTGRES_PASSWORD=$2
POSTGRES_DB=murmur

# DBコンテナの立ち上げ
docker run -d --rm \
--name local-db \
-v $PWD/initdb:/docker-entrypoint-initdb.d \
-p 5432:5432 \
-e POSTGRES_USER=${POSTGRES_USER} \
-e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
-e POSTGRES_DB=${POSTGRES_DB} \
postgres

