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
