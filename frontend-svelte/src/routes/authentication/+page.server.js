import { error, json, redirect } from '@sveltejs/kit'
import * as bcrypt from 'bcrypt'
import {pool} from '$lib/server/db'
import {signIn} from '@auth/sveltekit/client'
import { auth } from "$lib/server/lucia";

function validateFormData(userData){

    const isValid = {}

    isValid.name = Boolean(userData.name)
    isValid.email = Boolean(userData.email);
    isValid.password = Boolean(userData.password);

    return isValid
}

async function checkUserExists(username) {
    try {
      const query = 'SELECT COUNT(*) AS count FROM users WHERE name = $1';
      const values = [username];
      const result = await pool.query(query, values);
      const count = parseInt(result.rows[0].count);
      return count > 0;
    } catch (err) {
      console.error('Error checking user existence:', err);
      return false;
    }
  }


async function createUser(username, password){
  const user = await auth.createUser({
    key: {
      providerId: "username", // auth method
      providerUserId: username.toLowerCase(), // unique id when using "username" auth method
      password // hashed by Lucia
    },
    attributes: {
      name: username
    }
  });
  const session = await auth.createSession({
    userId: user.userId,
    attributes: {}
  });
  return session
}

/** @type {import('./$types').Actions} */
export const actions = {
    login: async (event) => {

    },
    register: async (event) => {
        const {request, cookies, locals} = event
        const data = await request.formData();

        const userData = {
            name: data.get('name'),
            password: data.get('password')
        }

        const userExists = await checkUserExists(userData.name)

        if (userExists){
            throw new Error('That name is already taken')
        }
        
        const session = await createUser(userData.name, userData.password)
        await locals.auth.setSession(session);
        // cookies.set('session', session.sessionId)
        // signIn('Credentials', {}, {username: userData.name, password: userData.password})

        console.log(userData);

        return {
            success: true,
            session
        }
    },
    logout: async (event) =>{
      const {cookies} = event;
      const sessionId = cookies.get('auth_session')
      if (sessionId){
        auth.invalidateSession(sessionId)
      }

      throw redirect(303, '/');
    }
};