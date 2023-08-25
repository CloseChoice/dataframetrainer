import { auth } from "$lib/server/lucia";
import type { LayoutServerLoad } from "./$types";

export const load: LayoutServerLoad = async (event) => {
  const {cookies} = event
  const sessionId = cookies.get('auth_session')

  let session = null
  if (sessionId){
    try{
      await auth.validateSession(sessionId)
      session = await auth.getSession(sessionId)
    }catch (error){
      // Lucia has no function for verifying session ids. If a session is invalid (when a user logged out) the try block will throw AUTH_INVALID_SESSION_ID
    }
  }

  return {
    session
  }
};