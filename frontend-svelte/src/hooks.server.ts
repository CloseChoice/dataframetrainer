import { auth } from "$lib/server/lucia";
import type { Handle } from "@sveltejs/kit";

export const handle: Handle = async ({ event, resolve }) => {
	// we can pass `event` because we used the SvelteKit middleware
	event.locals.auth = auth.handleRequest(event);
	return await resolve(event);
};


// export const handle = SvelteKitAuth({
//   secret: AUTH_SECRET,
//   adapter: TypeORMAdapter(connection),
//   providers: [
//     GitHub({ clientId: GITHUB_CLIENT_ID, clientSecret: GITHUB_CLIENT_SECRET }),
//     Google({clientId: GOOGLE_CLIENT_ID, clientSecret: GOOGLE_CLIENT_SECRET})
//   ],
//   trustHost: true,
// });

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
