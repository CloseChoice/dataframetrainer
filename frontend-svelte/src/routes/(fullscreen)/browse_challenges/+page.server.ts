import { error } from '@sveltejs/kit';
import type { ServerLoad } from '@sveltejs/kit';
import { pool } from '$lib/server/db';
import type { PageServerLoad } from '../new_challenge/[slug]/$types';

export const load: PageServerLoad = async({ params, fetch , locals}) => {

    const userId = locals?.session?.user?.userId || "NULL"
    // let challenges = await pool.query(`
    //     SELECT
    //     *
    //     FROM challenges c
    //     LEFT JOIN (FROM users_challenges_status SELECT challenge_id, status WHERE user_id = $1) ucs
    //     ON c.id = ucs.challenge_id;`, [userId])
    console.log('usaaaaaaaaaaaaaaaaaaaaaaaaaa id', userId)
    let challenges = await pool.query(`
        SELECT * 
        FROM challenges c
        LEFT JOIN (SELECT * FROM users_challenges_status WHERE user_id = $1) ucs
        ON c.id = ucs.challenge_id;`, [userId])
    // let challenges = await fetch(`http://backend:5000/get_all_challenges/`);
    // let challengesText = await challenges.text();
    // challengesText = JSON.parse(challengesText);
    console.log(challenges.rows)
    return {
        challenges: challenges.rows,
    };
}