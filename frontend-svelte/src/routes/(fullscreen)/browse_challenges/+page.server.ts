import { pool } from '$lib/server/db';
import type { PageServerLoad } from '../new_challenge/[slug]/$types';

export const load: PageServerLoad = async({ params, fetch , locals}) => {
    const userId = locals?.session?.user?.userId || "NULL"
    let challenges = await pool.query(`
        SELECT * 
        FROM challenges c
        LEFT JOIN (SELECT * FROM users_challenges_status WHERE user_id = $1) ucs
        ON c.id = ucs.challenge_id;`, [userId])
    return {
        challenges: challenges.rows,
    };
}