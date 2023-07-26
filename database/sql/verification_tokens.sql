CREATE TABLE IF NOT EXISTS public.verification_tokens (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    token character varying NOT NULL,
    identifier character varying NOT NULL,
    expires character varying NOT NULL,
    CONSTRAINT "verification_tokens_pkey" PRIMARY KEY (id)
);