import { error } from '@sveltejs/kit';
import type { ServerLoad } from '@sveltejs/kit';

/** @type {import('./$types').PageServerLoad} */
export async function load({ params, fetch }) {
    let challenges = await fetch(`/backend_server/get_all_challenges/`);
    let challengesText = await challenges.text();
    challengesText = JSON.parse(challengesText);

    return {
        challenges: challengesText,
    };
}