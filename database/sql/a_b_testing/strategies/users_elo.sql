CREATE TABLE IF NOT EXISTS users_elo(
    elo FLOAT NOT NULL,
    user_id uuid NOT NULL,
    "time" TIMESTAMP NOT NULL,
  CONSTRAINT "users_elo_fkey" FOREIGN KEY (user_id) REFERENCES users (id)
) TABLESPACE pg_default;