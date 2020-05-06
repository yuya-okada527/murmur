#!/bin/bash

# EKSクラスタの構築
eksctl create cluster \
--name murmur \
--region ap-northeast-1 \
--version 1.14 \
--nodegroup-name ng1
