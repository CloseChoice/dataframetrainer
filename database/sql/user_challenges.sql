CREATE TABLE "user_challenges" (
    "UserId" TEXT NOT NULL,
    "ChallengeId" TEXT,
    "SessionId" TEXT,
    "Timestamp" TIMESTAMP NOT NULL,
    "Successful" BOOLEAN,
    "Score" FLOAT,

    CONSTRAINT "User_fkey" FOREIGN KEY ("UserId") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "Challenge_fkey" FOREIGN KEY ("ChallengeId") REFERENCES "challenges"("id") ON DELETE CASCADE ON UPDATE CASCADE
);
