CREATE TABLE IF NOT EXISTS challenges(
    elo FLOAT NOT NULL,
    challenge_id TEXT NOT NULL,
  CONSTRAINT challenges_elo_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenges (id)
) TABLESPACE pg_default;