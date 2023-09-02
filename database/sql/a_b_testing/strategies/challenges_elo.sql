CREATE TABLE IF NOT EXISTS challenges_elo(
    elo FLOAT NOT NULL,
    challenge_id TEXT NOT NULL,
    UNIQUE(elo, challenge_id),
  CONSTRAINT challenges_elo_fkey FOREIGN KEY (challenge_id) REFERENCES challenges (id) ON DELETE CASCADE
) TABLESPACE pg_default;
