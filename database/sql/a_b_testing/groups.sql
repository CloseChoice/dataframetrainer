CREATE TABLE IF NOT EXISTS groups(
    id INT NOT NULL,
    description TEXT NOT NULL,
  CONSTRAINT "groups_pkey" PRIMARY KEY ("id")
) TABLESPACE pg_default;

INSERT INTO groups (id, description) VALUES (1, 'elo_group') ON CONFLICT DO NOTHING;