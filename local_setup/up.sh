#!/bin/bash

if [ $# != 2 ]; then
    echo "number of arguments must be 2"
    exit 1
fi

# 引数を取得
DB_USER=$1
DB_PASSWORD=$2

# DBの立ち上げ
sh ./local_setup/setup_db.sh $DB_USER $DB_PASSWORD

# BEの立ち上げ
sh ./local_setup/setup_be.sh $DB_USER $DB_PASSWORD

# FEの立ち上げ
sh ./local_setup/setup_fe.sh
