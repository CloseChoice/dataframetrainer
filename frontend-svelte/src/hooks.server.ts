import type { Handle, RequestEvent} from '@sveltejs/kit';
import { SvelteKitAuth } from "@auth/sveltekit";
import GitHub from "@auth/core/providers/github";
import Google from "@auth/core/providers/google"
import { 
  GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET,
  GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET,
  AUTH_SECRET,
  PGPASSWORD, PGPORT, PGUSER, PGHOST
} from "$env/static/private";
import { SnakeNamingStrategy } from 'typeorm-naming-strategies'
import type { PostgresConnectionOptions } from 'typeorm/driver/postgres/PostgresConnectionOptions';
import { TypeORMAdapter } from '@auth/typeorm-adapter';

const connection: PostgresConnectionOptions = {
    type: "postgres",
    host: PGHOST,
    port: PGPORT,
    username: PGUSER,
    password: PGPASSWORD,
    database: "postgres",
    namingStrategy: new SnakeNamingStrategy()
}

export const handle = SvelteKitAuth({
  secret: AUTH_SECRET,
  adapter: TypeORMAdapter(connection),
  providers: [
    GitHub({ clientId: GITHUB_CLIENT_ID, clientSecret: GITHUB_CLIENT_SECRET }),
    Google({clientId: GOOGLE_CLIENT_ID, clientSecret: GOOGLE_CLIENT_SECRET})
  ],
  callbacks: {
    // Attach the user ID to the Session Object
    async session({ session, user, token }) {
      if (session?.user){
        session.user.id = user.id
      }
      return session
    },
  }
});

// export const handle: Handle = async ({ resolve, event }) => {

//   // Apply CORS header for API routes
//   if (event.url.pathname.startsWith('/api')) {
//     // Required for CORS to work
//     if(event.request.method === 'OPTIONS') {
//       return new Response(null, {
//         headers: {
//           'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
//           'Access-Control-Allow-Origin': '*',
//           'Access-Control-Allow-Headers': '*',
//         }
//       });
//     }

//   }

//   const response = await resolve(event);
//   if (event.url.pathname.startsWith('/api')) {
//     response.headers.append('Access-Control-Allow-Origin', `*`);
//   }
//   return response;
// };
