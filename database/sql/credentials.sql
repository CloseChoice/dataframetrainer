CREATE TABLE IF NOT EXISTS credentials(
    user_id UUID NOT NULL,
    password_hash VARCHAR(72) NOT NULL,

    CONSTRAINT "user_id_primary_key" PRIMARY KEY ("user_id"),
    CONSTRAINT "User_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE
);