CREATE TABLE IF NOT EXISTS challenges(
    id TEXT NOT NULL,

    CONSTRAINT "Challenges_pkey" PRIMARY KEY ("id")
) TABLESPACE pg_default;

COPY challenges FROM PROGRAM 'ls /challenges/ | grep "^[[:upper:]]"';
