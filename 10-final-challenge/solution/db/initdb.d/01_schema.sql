CREATE TABLE IF NOT EXISTS jobs (
    id      TEXT PRIMARY KEY,
    payload JSONB NOT NULL,
    status  TEXT NOT NULL DEFAULT 'pending',
    result  TEXT
);
