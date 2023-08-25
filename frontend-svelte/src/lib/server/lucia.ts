import { lucia } from "lucia";
import { postgres as postgresAdapter } from "@lucia-auth/adapter-postgresql";
import postgres from "postgres";
import { sveltekit } from "lucia/middleware";
import { dev } from "$app/environment";
import { pool } from "./db";

// export const auth = lucia({
//     middleware: sveltekit(),
//     adapter: postgresAdapter(sql, {
//         user: "users",
//         key: "passwords",
//         session: "sessions"
//     }),
//     env: dev ? "DEV" : "PROD",

//     getUserAttributes: (data) => {
// 		return {
// 			name: data.name,
//       role: data.role
// 		};
// 	}
// })

import { pg } from "@lucia-auth/adapter-postgresql";


export const auth = lucia({
  middleware: sveltekit(),
  adapter: pg(pool, {
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
});