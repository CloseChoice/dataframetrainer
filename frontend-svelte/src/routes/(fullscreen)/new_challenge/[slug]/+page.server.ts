import { error } from '@sveltejs/kit';
import type { ServerLoad } from '@sveltejs/kit';

export const load: ServerLoad = async ({ params, fetch })=> {
    console.log(params.slug);

    const challengeName = params.slug

    // let url = `http://127.0.0.1:5000/get_challenge/${challengeName}`;

    const challengeClass = await fetch(`http://127.0.0.1:5000/files/challenges/${challengeName}/challenge.py`);
    const intro = await fetch(`http://127.0.0.1:5000/files/challenges/${challengeName}/intro.md`);
    const defaultCode = await fetch(`http://127.0.0.1:5000/files/challenges/${challengeName}/defaultCode.py`)
    const challengeTest = await fetch(`http://127.0.0.1:5000/files/challenges/${challengeName}/test_.py`)

    // if (challengeClass.status != 200) {
    //     throw error(404, `challenge ${challengeName} no exist you stupiddo. This is the url ${url}`);
    // }

    // await pyodidemoped

    const challengeClassText = await challengeClass.text();
    const introText = await intro.text();
    const defaultCodeText = await defaultCode.text();
    const challengeTestTExt = await challengeTest.text()
    // console.log("SERVER SIDE: this is the default Code text", defaultCodeText);
    return {
        challenge_class: challengeClassText ,
        intro: introText,
        default_code: defaultCodeText,
        challenge_name: challengeName,
        challenge_test: challengeTestTExt,
    };
}
