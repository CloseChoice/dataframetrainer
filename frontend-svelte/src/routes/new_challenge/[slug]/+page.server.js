import { error } from '@sveltejs/kit';

/** @type {import('./$types').PageServerLoad} */
export async function load({ params, fetch }) {
    console.log(params.slug);


    const challengeName = params.slug

    let url = `http://127.0.0.1:5000/get_challenge/${challengeName}`;

    const challengeClass = await fetch(url);
    const intro = await fetch(`http://127.0.0.1:5000/get_intro/${challengeName}`);
    const defaultCode = await fetch(`http://127.0.0.1:5000/get_default/${challengeName}`)

    if (challengeClass.status != 200) {
        throw error(404, `challenge ${challengeName} no exist you stupiddo. This is the url ${url}`);
    }

    const challengeClassText = await challengeClass.text();
    const introText = await intro.text();
    const defaultCodeText = await defaultCode.text();
    return {
        challenge_class: challengeClassText ,
        intro: introText,
        default_code: defaultCodeText,
        challenge_name: challengeName,
    };
}
