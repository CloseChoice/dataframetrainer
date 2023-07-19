CREATE TABLE IF NOT EXISTS challenge_elo(
    elo FLOAT NOT NULL,
    challenge_id TEXT NOT NULL,
  CONSTRAINT challenges_elo_fkey FOREIGN KEY (challenge_id) REFERENCES challenges (id)
) TABLESPACE pg_default;