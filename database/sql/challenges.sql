-- CREATE TABLE IF NOT EXISTS challenges(
--     id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
--     file_path character varying(80) NOT NULL,
--     CONSTRAINT challenge_pkey PRIMARY KEY (id),
--     CONSTRAINT challenge_path_unique UNIQUE (file_path)
-- ) TABLESPACE pg_default;

-- COPY challenges FROM PROGRAM 'ls ../challenges';