CREATE EXTENSION IF NOT EXISTS "uuid-ossp"; -- This enables the uuid-ossp extension for UUID functions


DO $$ BEGIN
    CREATE TYPE user_role AS ENUM ('user', 'admin');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

CREATE TABLE IF NOT EXISTS public.users (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    name character varying NOT NULL UNIQUE,
    role user_role DEFAULT 'user' NOT NULL
);

CREATE OR REPLACE FUNCTION register_user_with_credentials(
    p_username VARCHAR,
    p_password_hash VARCHAR
) RETURNS VOID AS $$
DECLARE
    v_user_id UUID;
BEGIN
    -- Insert user into the users table
    INSERT INTO users (name) VALUES (p_username) RETURNING id INTO v_user_id;

    -- Insert credentials into the credentials table
    INSERT INTO credentials (user_id, password_hash) VALUES (v_user_id, p_password_hash);
END;
$$ LANGUAGE plpgsql;