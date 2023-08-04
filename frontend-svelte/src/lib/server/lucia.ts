import { lucia } from "lucia";
import { postgres as postgresAdapter } from "@lucia-auth/adapter-postgresql";
import postgres from "postgres";
import { sveltekit } from "lucia/middleware";
import { dev } from "$app/environment";
import {DB_NAME, DB_USER, HOST, PASSWORD, PORT} from '$env/static/private'
const PG_CONNECTION_STRING = `postgres://${DB_USER}:${PASSWORD}@${HOST}:${PORT}/${DB_NAME}`
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
			name: data.name,
      role: data.role
		};
	}
})