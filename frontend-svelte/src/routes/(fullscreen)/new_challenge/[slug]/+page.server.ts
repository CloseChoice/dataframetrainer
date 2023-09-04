import { error, type ServerLoad } from '@sveltejs/kit';

export const load: ServerLoad =  async ({ params, fetch, cookies, locals }) =>{
    console.log(params.slug);

    const session_id = locals?.session?.sessionId
    const requestOptions: RequestInit = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'session_id': session_id // Set any necessary headers
            }) // Add any needed body params
    };

    const challengeName = params.slug
    let url = `http://backend:5000/post_challenge/${challengeName}/`;

    const challengeClass = await fetch(url, requestOptions);
    const intro = await fetch(`http://backend:5000/get_intro/${challengeName}`);
    const defaultCode = await fetch(`http://backend:5000/get_default/${challengeName}`)
    const challengeTest = await fetch(`http://backend:5000/get_challenge_test/${challengeName}`)
    const submission = await fetch(`http://backend:5000/get_submission/${challengeName}`)

    if (challengeClass.status != 200) {
        throw error(404, `challenge ${challengeName} no exist you stupiddo. This is the url ${url}`);
    }

    const challengeClassText = await challengeClass.text();
    const introText = await intro.text();
    const defaultCodeText = await defaultCode.text();
    const challengeTestTExt = await challengeTest.text();
    const submissionText = await submission.text();
    // console.log("SERVER SIDE: this is the default Code text", defaultCodeText);
    return {
        challenge_class: challengeClassText ,
        intro: introText,
        default_code: defaultCodeText,
        challenge_name: challengeName,
        challenge_test: challengeTestTExt,
        submission: submissionText
    };
}
