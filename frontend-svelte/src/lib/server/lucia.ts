import { lucia } from "lucia";
import { postgres as postgresAdapter } from "@lucia-auth/adapter-postgresql";
import postgres from "postgres";
import { sveltekit } from "lucia/middleware";
import { dev } from "$app/environment";
import { 
    PG_CONNECTION_STRING,
  } from "$env/static/private";

const sql = postgres(PG_CONNECTION_STRING);

export const auth = lucia({
    middleware: sveltekit(),
    adapter: postgresAdapter(sql, {
        user: "users",
        key: "passwords",
        session: "sessions"
    }),
    env: dev ? "DEV" : "PROD",

    getUserAttributes: (data) => {
		return {
			name: data.name
		};
	}
})