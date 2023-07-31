CREATE TABLE IF NOT EXISTS public.accounts (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    user_id uuid NOT NULL,
    type character varying NOT NULL,
    provider character varying NOT NULL,
    provider_account_id character varying NOT NULL,
    refresh_token character varying,
    access_token character varying,
    expires_at bigint,
    token_type character varying,
    scope character varying,
    id_token character varying,
    session_state character varying,

    CONSTRAINT "accounts_pkey" PRIMARY KEY (id),
    CONSTRAINT "accounts_fkey" FOREIGN KEY (user_id) REFERENCES public.users(id)
);