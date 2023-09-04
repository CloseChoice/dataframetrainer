import { redirect } from "@sveltejs/kit";
import type { PageServerLoad } from "../new_challenge/[slug]/$types";
import axios from 'axios'

// async function handleNewChallenge(){
//     console.log("handleNewChallenge", $page.data);
//     const userId = $page.data.session?.user?.userId;

//     const user_id = userId ?? "";
//     // for some reason this is not working.
//     const res = await axios.post('/backend_server/post_next_challenge', {
//         user_id: user_id
//     });

//     const nextChallenge = res.data.response.next_challenge
//     goto('/new_challenge/' + nextChallenge)
// }

// RESOLVE THE SESSION OBJECT IS SESSION COOKIE IS SET


export const load: PageServerLoad = async (event) =>{
    const res = await event.fetch('http://backend:5000/post_next_challenge', {
        method: "POST",
        body: JSON.stringify({user_id: event.locals?.session?.user.userId || ""}),
        headers: {
            "Content-Type": "application/json",
        },
    })
    const data = await res.json()
    const nextChallenge = data.response.next_challenge
    throw redirect(302, '/new_challenge/' + nextChallenge)
}