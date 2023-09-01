import {pool} from '$lib/server/db'
import {auth} from '$lib/server/lucia'
import axios from 'axios'

export async function checkUserExists(username: string) {
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


export async function createUser(username: string, password: string){
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
  const res = await axios.post('/backend_server/set_user_group', {
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
  return session
}