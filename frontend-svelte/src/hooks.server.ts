import { auth } from "$lib/server/lucia";
import type { Handle } from "@sveltejs/kit";

export const handle: Handle = async ({ event, resolve }) => {
	// we can pass `event` because we used the SvelteKit middleware
	event.locals.auth = auth.handleRequest(event);
	console.log("event.locals.auth", event.locals.auth)

	const sessionId = event.cookies.get('auth_session')
	if (sessionId){
		try{
		  await auth.validateSession(sessionId)
		  event.locals.session = await auth.getSession(sessionId)
		}catch (error){
		  // Lucia has no function for verifying session ids. If a session is invalid (when a user logged out) the try block will throw AUTH_INVALID_SESSION_ID
		}
	  }

	return await resolve(event);
};
