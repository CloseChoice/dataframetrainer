CREATE TABLE IF NOT EXISTS "users_challenges" (
    "user_id" TEXT NOT NULL,
    "challenge_id" TEXT,
    "session_id" TEXT,
    "timestamp" TIMESTAMP NOT NULL,
    "successful" BOOLEAN NULL,
    "score" FLOAT NULL,

    CONSTRAINT "User_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "Challenge_fkey" FOREIGN KEY ("challenge_id") REFERENCES "challenges"("id") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "users_challenges_status" (
    "user_id" TEXT NOT NULL REFERENCES users(id),
    "challenge_id" TEXT NOT NULL REFERENCES challenges(id),
    "status" INTEGER NOT NULL,  
    -- The status values are represented as integer 0 = seen, 1 = tried, 2 = solved
    -- The status will only be updated when a new status is higher than the old one
    CONSTRAINT "combined_primary_key" PRIMARY KEY ("user_id", "challenge_id")
);

CREATE OR REPLACE FUNCTION insert_into_users_challenges_status()
RETURNS TRIGGER AS $$
DECLARE
    old_status INTEGER;
    new_status INTEGER;
BEGIN
    -- Select status value from users_challenges_status table
    SELECT COALESCE(status, 0)
    INTO old_status
    FROM users_challenges_status
    WHERE user_id = NEW.user_id AND challenge_id = NEW.challenge_id;

    -- Set new_status based on NEW.successful
    new_status := CASE
        WHEN NEW.successful IS TRUE THEN 2
        WHEN NEW.successful IS FALSE THEN 1
        ELSE 0
    END;

    -- Insert or update into users_challenges_status table
    -- The new status will be the max of old_status and new_status
    INSERT INTO users_challenges_status (user_id, challenge_id, status)
    VALUES (NEW.user_id, NEW.challenge_id, GREATEST(old_status, new_status))
    ON CONFLICT (user_id, challenge_id) DO UPDATE
    SET status = EXCLUDED.status;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS  users_challenges_trigger on users_challenges;
CREATE TRIGGER users_challenges_trigger
AFTER INSERT OR UPDATE ON users_challenges
FOR EACH ROW
EXECUTE FUNCTION insert_into_users_challenges_status();