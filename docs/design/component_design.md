## コンポーネント設計

#### コンポーネント一覧

- フロントエンド APP
- バックエンド APP
- バッチ APP
- データベース

#### フロントエンド APP

- 言語
  - JavaScript
- フレームワーク
  - React
  - Bootstrap
- 配布方法
  - S3 -> CloudFront

#### バックエンド APP

- 言語
  - Python
- フレームワーク
  - FastAPI
  - SQLAlchemy
- 実行基盤
  - EKS on EC2

#### データベース

- エンジン
  - PostgreSQL
- 実行基盤
  - RDS

#### バッチ APP

- 言語
  - Python
  - Go
- 実行基盤
  - EKS on EC2
  - Lambda
