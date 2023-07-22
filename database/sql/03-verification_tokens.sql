CREATE TABLE public.verification_tokens (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    token character varying NOT NULL,
    identifier character varying NOT NULL,
    expires character varying NOT NULL
);

ALTER TABLE public.verification_tokens OWNER TO postgres;

ALTER TABLE ONLY public.verification_tokens
    ADD CONSTRAINT "verification_tokens_pkey" PRIMARY KEY (id);