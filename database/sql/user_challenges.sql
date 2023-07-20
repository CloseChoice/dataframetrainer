CREATE TABLE IF NOT EXISTS "user_challenges" (
    "user_id" TEXT NOT NULL,
    "challenge_id" TEXT,
    "session_id" TEXT,
    "timestamp" TIMESTAMP NOT NULL,
    "successful" BOOLEAN,
    "score" FLOAT,

    CONSTRAINT "User_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "Challenge_fkey" FOREIGN KEY ("challenge_id") REFERENCES "challenges"("id") ON DELETE CASCADE ON UPDATE CASCADE
);
