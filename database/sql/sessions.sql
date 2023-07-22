CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS "sessions" (
  id uuid NOT NULL DEFAULT uuid_generate_v4(),
  user_id TEXT NOT NULL,
  expires timestamp with time zone DEFAULT (CURRENT_TIMESTAMP + '02:00:00'::interval),
  CONSTRAINT sessions_pkey PRIMARY KEY (id),
  CONSTRAINT sessions_user_fkey FOREIGN KEY (user_id)
    REFERENCES users (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE
    NOT VALID
) TABLESPACE pg_default;
