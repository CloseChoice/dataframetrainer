CREATE TABLE public.sessions (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    session_token character varying NOT NULL,
    user_id uuid NOT NULL,
    expires character varying NOT NULL
);
ALTER TABLE public.sessions OWNER TO postgres;
ALTER TABLE ONLY public.sessions
    ADD CONSTRAINT "sessions_pkey" PRIMARY KEY (id);
ALTER TABLE ONLY public.sessions
    ADD CONSTRAINT "sessions_unique_session_token" UNIQUE (session_token);
ALTER TABLE ONLY public.sessions
    ADD CONSTRAINT "sessions_fkey" FOREIGN KEY (user_id) REFERENCES public.users(id);