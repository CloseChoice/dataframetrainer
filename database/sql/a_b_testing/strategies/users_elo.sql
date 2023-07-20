CREATE TABLE IF NOT EXISTS users_elo(
    elo FLOAT NOT NULL,
    user_id TEXT NOT NULL,
  CONSTRAINT "users_groups_fkey" FOREIGN KEY (user_id) REFERENCES users (id)
) TABLESPACE pg_default;