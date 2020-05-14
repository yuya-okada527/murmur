## プロジェクト概要

#### 概要

GW 中の課題として、Twitter モック的なアプリを構築する。

#### プロジェクト名

murmur

#### インフラ構築

```bash
# EKSの構築
$ sh scripts/create_cluster.sh

# EKSの削除
$ sh scripts/delete_cluster.sh
```

#### ローカル開発環境

```bash
# コンテナの立ち上げ
sh local_setup/up.sh ${DB_USER} ${DB_PASSWORD}

# コンテナの停止
sh local_setup/down.sh
```
