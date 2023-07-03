CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";


CREATE TYPE public.roles AS ENUM
  ('user', 'admin');

CREATE TABLE IF NOT EXISTS public.users (
  id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
  role roles NOT NULL DEFAULT 'user'::roles,
  email character varying(80) COLLATE pg_catalog."default" NOT NULL,
  password character varying(80) COLLATE pg_catalog."default",
  user_name character varying(20) COLLATE pg_catalog."default" NOT NULL,
  CONSTRAINT users_pkey PRIMARY KEY (id),
  CONSTRAINT users_email_unique UNIQUE (email),
  CONSTRAINT users_uname_unique UNIQUE (user_name)
) TABLESPACE pg_default;

CREATE TABLE IF NOT EXISTS public.sessions (
  id uuid NOT NULL DEFAULT uuid_generate_v4(),
  user_id integer NOT NULL,
  expires timestamp with time zone DEFAULT (CURRENT_TIMESTAMP + '02:00:00'::interval),
  CONSTRAINT sessions_pkey PRIMARY KEY (id),
  CONSTRAINT sessions_user_fkey FOREIGN KEY (user_id)
    REFERENCES public.users (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE
    NOT VALID
) TABLESPACE pg_default;





CREATE OR REPLACE FUNCTION public.authenticate(
	input json,
	OUT response json)
    RETURNS json
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
DECLARE
  input_email varchar(80) := LOWER(TRIM((input->>'email')::varchar));
  input_password varchar(80) := (input->>'password')::varchar;
BEGIN
  IF input_email IS NULL OR input_password IS NULL THEN
    response := json_build_object('statusCode', 400, 'status', 'Please provide an email address and password to authenticate.', 'user', NULL);
	RETURN;
  END IF;

  WITH user_authenticated AS (
    SELECT users.id, role, user_name
    FROM users
    WHERE email = input_email AND password = crypt(input_password, password) LIMIT 1
  )
  SELECT json_build_object(
	'statusCode', CASE WHEN (SELECT COUNT(*) FROM user_authenticated) > 0 THEN 200 ELSE 401 END,
	'status', CASE WHEN (SELECT COUNT(*) FROM user_authenticated) > 0
	  THEN 'Login successful.'
	  ELSE 'Invalid username/password combination.'
	END,
	'user', CASE WHEN (SELECT COUNT(*) FROM user_authenticated) > 0
	  THEN (SELECT json_build_object(
		  'id', user_authenticated.id,
		  'role', user_authenticated.role,
		  'email', input_email,
		  'name', user_authenticated.user_name)
		 FROM user_authenticated)
	  ELSE NULL
	  END,
	'sessionId', (SELECT create_session(user_authenticated.id) FROM user_authenticated)
  ) INTO response;
END;
$BODY$;





CREATE OR REPLACE FUNCTION public.create_session(
	input_user_id integer)
    RETURNS uuid
    LANGUAGE 'sql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
DELETE FROM sessions WHERE user_id = input_user_id;
INSERT INTO sessions(user_id) VALUES (input_user_id) RETURNING sessions.id;
$BODY$;





CREATE OR REPLACE FUNCTION public.get_session(input_session_id uuid)
  RETURNS json
  LANGUAGE 'sql'
AS $BODY$
SELECT json_build_object(
  'id', sessions.user_id,
  'role', users.role,
  'email', users.email,
  'name', users.user_name,
  'expires', sessions.expires
) AS user
FROM sessions
  INNER JOIN users ON sessions.user_id = users.id
WHERE sessions.id = input_session_id AND expires > CURRENT_TIMESTAMP LIMIT 1;
$BODY$;





CREATE OR REPLACE FUNCTION public.register(
	input json,
	OUT user_session json)
    RETURNS json
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
DECLARE
  input_email varchar(80) := LOWER(TRIM((input->>'email')::varchar));
  input_name varchar(20) := TRIM((input->>'name')::varchar);
  input_password varchar(80) := (input->>'password')::varchar;
BEGIN
  PERFORM id FROM users WHERE email = input_email;
  IF NOT FOUND THEN
    INSERT INTO users(role, password, email, user_name)
      VALUES('user', crypt(input_password, gen_salt('bf', 8)), input_email, input_name)
      RETURNING
        json_build_object(
          'sessionId', create_session(users.id),
          'user', json_build_object('id', users.id, 'role', 'user', 'email', input_email, 'name', input_name, 'optOut', false)
        ) INTO user_session;
  ELSE -- user is registering account that already exists so set sessionId and user to null so client can let them know
  	SELECT authenticate(input) INTO user_session;
  END IF;
END;
$BODY$;





CREATE PROCEDURE public.delete_session(input_id integer)
    LANGUAGE sql
    AS $$
DELETE FROM sessions WHERE user_id = input_id;
$$;





CREATE OR REPLACE PROCEDURE public.upsert_user(input json)
LANGUAGE plpgsql
AS $BODY$
DECLARE
  input_id integer := COALESCE((input->>'id')::integer,0);
  input_role roles := COALESCE((input->>'role')::roles, 'user');
  input_email varchar(80) := LOWER(TRIM((input->>'email')::varchar));
  input_password varchar(80) := COALESCE((input->>'password')::varchar, '');
  input_name varchar(20) := TRIM((input->>'name')::varchar);
BEGIN
  IF input_id = 0 THEN
    INSERT INTO users (role, email, password, user_name)
    VALUES (
	  input_role, input_email, crypt(input_password, gen_salt('bf', 8)), input_name);
  ELSE
    UPDATE users SET
	  role = input_role,
	  email = input_email,
	  password = CASE WHEN input_password = ''
		  THEN password -- leave as is (we are updating fields other than the password)
		  ELSE crypt(input_password, gen_salt('bf', 8))
	  END,
	  user_name = input_name
	WHERE id = input_id;
  END IF;
END;
$BODY$;




CREATE OR REPLACE PROCEDURE public.update_user(input_id integer, input json)
LANGUAGE plpgsql
AS $BODY$
DECLARE
  input_email varchar(80) := LOWER(TRIM((input->>'email')::varchar));
  input_password varchar(80) := COALESCE((input->>'password')::varchar, '');
  input_name varchar(20) := TRIM((input->>'name')::varchar);
BEGIN
  UPDATE users SET
    email = input_email,
	password = CASE WHEN input_password = ''
      THEN password -- leave as is (we are updating fields other than the password)
	  ELSE crypt(input_password, gen_salt('bf', 8))
	END,
	user_name = input__name
  WHERE id = input_id;
END;
$BODY$;



CALL public.upsert_user('{"id":0, "role":"user", "email":"exampleuser@gmail.com", "password":"supersecurepassword123", "name":"nicerusername420"}'::json)