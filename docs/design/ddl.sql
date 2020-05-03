-- テーブル定義

CREATE TABLE IF NOT EXISTS murmur (
    id              sequence,
    user_id         char(8),
    user_name       varchar(32),
    message         varchar(128),
    time            timestamp
);
