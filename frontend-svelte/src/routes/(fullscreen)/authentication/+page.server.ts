import { redirect, fail } from '@sveltejs/kit';
import {pool} from '$lib/server/db';
import { auth } from "$lib/server/lucia";
import { sessionState } from "$lib/stores/pyodide-store";
import axios from 'axios';

function validateFormData(userData){
    const isValid = {}

    isValid.name = Boolean(userData.name)
    isValid.email = Boolean(userData.email);
    isValid.password = Boolean(userData.password);

    return isValid
}

async function checkUserExists(username) {
    console.log("in checkUserExists");
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


async function createUser(username: String, password: String){
  console.log("in createUser");
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
  console.log("Session created", session);

console.log("set user group", user.userId, session.sessionId);
  const res = await axios.post('http://backend:5000/set_user_group', {
    user_id: user.userId,
    session_id: session.sessionId
  })
  // const res = await axios.post('/backend/set_user_group', {
  //     data: {
  //         user_id: user.userId,
  //         session_id: session.sessionId,
  //     }
  // })
  console.log("set user group return", res);
  // write session to store
  console.log("WRITE SESSION TO SESSIONSTORE 1", session);
  sessionState.set(session);
  return session
}

/** @type {import('./$types').Actions} */
export const actions = {
    login: async (event) => {
      const {request, cookies, locals} = event
      const data = await request.formData();

      const password = data.get('password')?.toString()
      const name = data.get('name')?.toString()
      let session = null
      try {
        if (!password || !name){
          throw Error("Invalid Password or Username")
        }
        const key = await auth.useKey("username", name, password);
        session = await auth.createSession({userId: key.userId, attributes: {}});
        console.log("WRITE SESSION TO SESSIONSTORE 2", session);
        sessionState.set(session);
        await locals.auth.setSession(session);
        
      } catch (e) {
        return fail(400, {password: {
          isValid: false,
          feedback: "Invalid Password or Username"
        }})
      }

      return {
        success: true,
        session
      }
      
    },
    register: async (event) => {
        const {request, cookies, locals} = event
        const data = await request.formData();
        console.log("register data", data);

        const userData = {
            name: data.get('name'),
            password: data.get('password')
        }

        const userExists = await checkUserExists(userData.name)
        if (userExists){
          return fail(400, { username: {
            isValid: false,
            feedback: "This username is already taken"
          } });
        }
        console.log("after check if user exists");
        
        const session = await createUser(userData.name, userData.password)
        console.log("after create user");

        await locals.auth.setSession(session);
        console.log("WRITE SESSION TO SESSIONSTORE 3", session);
        sessionState.set(session);

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