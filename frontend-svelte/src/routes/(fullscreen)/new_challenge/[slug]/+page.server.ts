import { error } from '@sveltejs/kit';

/** @type {import('./$types').PageServerLoad} */
export async function load({ params, fetch }) {
    console.log(params.slug);


    const challengeName = params.slug

    let url = `/backend/get_challenge/${challengeName}`;

    const challengeClass = await fetch(url);
    const intro = await fetch(`/backend/get_intro/${challengeName}`);
    const defaultCode = await fetch(`/backend/get_default/${challengeName}`)
    const challengeTest = await fetch(`/backend/get_challenge_test/${challengeName}`)
    const submission = await fetch(`/backend/get_submission/${challengeName}`)

    if (challengeClass.status != 200) {
        throw error(404, `challenge ${challengeName} no exist you stupiddo. This is the url ${url}`);
    }

    const challengeClassText = await challengeClass.text();
    const introText = await intro.text();
    const defaultCodeText = await defaultCode.text();
    const challengeTestTExt = await challengeTest.text();
    const submissionText = await submission.text();
    console.log("SERVER SIDE: this is the default Code text", defaultCodeText);
    return {
        challenge_class: challengeClassText ,
        intro: introText,
        default_code: defaultCodeText,
        challenge_name: challengeName,
        challenge_test: challengeTestTExt,
        submission: submissionText
    };
}
