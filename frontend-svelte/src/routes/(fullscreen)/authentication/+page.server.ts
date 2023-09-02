import { redirect, fail, type Actions } from '@sveltejs/kit';
import { auth } from "$lib/server/lucia";
import { createUser, checkUserExists } from '$lib/server/auth';

function validateFormData(userData){
    const isValid = {}

    isValid.name = Boolean(userData.name)
    isValid.email = Boolean(userData.email);
    isValid.password = Boolean(userData.password);

    return isValid
}



export const actions: Actions = {
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
        
        const session = await createUser(userData.name, userData.password, event)
        console.log("after create user");

        await locals.auth.setSession(session);
        console.log("WRITE SESSION TO SESSIONSTORE 3", session);

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