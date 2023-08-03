CREATE EXTENSION IF NOT EXISTS "uuid-ossp"; -- This enables the uuid-ossp extension for UUID functions


DO $$ BEGIN
    CREATE TYPE user_role AS ENUM ('user', 'admin');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

CREATE TABLE IF NOT EXISTS public.users (
    id TEXT PRIMARY KEY,
    name character varying NOT NULL UNIQUE,
    role user_role DEFAULT 'user' NOT NULL
);

CREATE TABLE IF NOT EXISTS public.passwords (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    hashed_password TEXT
);

CREATE TABLE IF NOT EXISTS public.sessions (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    active_expires BIGINT NOT NULL,
    idle_expires BIGINT NOT NULL
);