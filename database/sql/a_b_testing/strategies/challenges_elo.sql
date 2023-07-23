CREATE TABLE IF NOT EXISTS challenges_elo(
    elo FLOAT NOT NULL,
    challenge_id TEXT NOT NULL,
    "time" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT challenges_elo_fkey FOREIGN KEY (challenge_id) REFERENCES challenges (id)
) TABLESPACE pg_default;
