#!/bin.bash

# EKSクラスタの削除
eksctl delete cluster \
--name murmur \
--region ap-northeast-1 \
--wait
