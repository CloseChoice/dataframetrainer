import { query } from '$lib/server/db'
import { error, json } from '@sveltejs/kit'



function validateFormData(userData){

    const isValid = {}

    isValid.name = Boolean(userData.name)
    isValid.email = Boolean(userData.email);
    isValid.password = Boolean(userData.password);

    return isValid
}



/** @type {import('./$types').Actions} */
export const actions = {
    register: async (event) => {
        const {request, cookies} = event
        const data = await request.formData();
        const name = data.get('name');
        const email = data.get('email');
        const password = data.get('password');
        


        const userData = {
            name: data.get('name'),
            email: data.get('email'),
            password: data.get('password')
        }

        const validation = validateFormData(userData)

        // console.log(userData);
        const sql = `SELECT register($1) AS "authenticationResult";`
        const result = await query(sql, [JSON.stringify(userData)])
        const { authenticationResult } = result.rows[0]

        console.log(authenticationResult.user);

        cookies.set('session', authenticationResult.sessionId)

        return {
            success: true,
        }
    }
};