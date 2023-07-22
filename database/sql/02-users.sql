CREATE TABLE public.users (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    name character varying,
    email character varying,
    email_verified character varying,
    image character varying,
);
ALTER TABLE public.users OWNER TO postgres;
ALTER TABLE ONLY public.users
    ADD CONSTRAINT "users_pk" PRIMARY KEY (id);
ALTER TABLE ONLY public.users
    ADD CONSTRAINT "users_unique_email" UNIQUE (email);