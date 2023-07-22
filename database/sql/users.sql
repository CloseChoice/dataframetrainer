CREATE TABLE IF NOT EXISTS public.users (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    name character varying,
    email character varying,
    email_verified character varying,
    image character varying,

    CONSTRAINT "users_pk" PRIMARY KEY (id),
    CONSTRAINT "users_unique_email" UNIQUE (email)
);