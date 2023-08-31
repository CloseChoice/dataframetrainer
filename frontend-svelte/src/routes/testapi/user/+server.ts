

import { error } from '@sveltejs/kit';
import type { RequestHandler } from '@sveltejs/kit';
import { createUser } from '$lib/server/auth';

export const POST: RequestHandler = async (event)=> {
    const body = await event.request.json()
    const {username, password} = body;
    if (! (username && password)){
        throw error(404, {message: "you need to provide 'username' and 'password' parameters"})
    }
    let session = null

    session = await createUser(username, password)
    await event.locals.auth.setSession(session);
    return new Response(JSON.stringify(session))
}