CREATE TABLE IF NOT EXISTS "users" (
    "id" TEXT NOT NULL,
    "user_name" TEXT,
    "email" TEXT,
    "emailVerified" TIMESTAMP(3),
    "password" TEXT,
    "image" TEXT,
    "isNew" BOOLEAN NOT NULL DEFAULT true,
    "role" roles NOT NULL DEFAULT 'user'::roles,
    CONSTRAINT "users_pkey" PRIMARY KEY ("id"),
    CONSTRAINT users_email_unique UNIQUE (email),
    CONSTRAINT users_uname_unique UNIQUE (user_name)
);