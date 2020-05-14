#!/bin/bash

# FEの停止
docker stop fe-app

# BEの停止
docker stop be-app

# DBの停止
docker stop local-db