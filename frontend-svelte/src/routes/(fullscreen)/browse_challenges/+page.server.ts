import { error } from '@sveltejs/kit';
import type { ServerLoad } from '@sveltejs/kit';

export const load: ServerLoad = async ({ params, fetch })=> {
    let challenges = await fetch(`http://127.0.0.1:5000/get_all_challenges/`);
    let challengesText = await challenges.text();
    challengesText = JSON.parse(challengesText);

    return {
        challenges: challengesText,
    };
}