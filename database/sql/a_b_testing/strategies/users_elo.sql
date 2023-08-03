CREATE TABLE IF NOT EXISTS users_elo(
    elo FLOAT NOT NULL,
    user_id TEXT NOT NULL,
    "time" TIMESTAMP NOT NULL,
  CONSTRAINT "users_elo_fkey" FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
) TABLESPACE pg_default;