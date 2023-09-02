import { pool } from '$lib/server/db';
import type { PageServerLoad } from '../new_challenge/[slug]/$types';

export const load: PageServerLoad = async({ params, fetch , locals}) => {
    const userId = locals?.session?.user?.userId || "NULL"
    console.log('usaaaaaaaaaaaaaaaaaaaaaaaaaa id', userId)
    let challenges = await pool.query(`
        SELECT * 
        FROM challenges c
        LEFT JOIN (SELECT * FROM users_challenges_status WHERE user_id = $1) ucs
        ON c.id = ucs.challenge_id;`, [userId])
    console.log(challenges.rows)
    return {
        challenges: challenges.rows,
    };
}