CREATE TABLE IF NOT EXISTS public.sessions (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    session_token character varying NOT NULL,
    user_id uuid NOT NULL,
    expires character varying NOT NULL,

    CONSTRAINT "sessions_pkey" PRIMARY KEY (id),
    CONSTRAINT "sessions_unique_session_token" UNIQUE (session_token),
    CONSTRAINT "sessions_fkey" FOREIGN KEY (user_id) REFERENCES public.users(id)
);