import { error } from '@sveltejs/kit';

/** @type {import('./$types').PageServerLoad} */
export async function load({ params, fetch }) {
    console.log(params.slug);

    const challengeName = params.slug

<<<<<<< HEAD
    let url = `http://127.0.0.1:8080/${challengeName}/description.md`;

    console.log(`IN load method ${url}`);
    const descriptionRes = await fetch(url);
    console.log(`IN load method`);

    if (descriptionRes.status != 200) {
        throw error(404, `challenge ${challengeName} no exist you stupiddo. This is the url ${url}`);
    }
    console.log(`AFTER error load method`);

    const templateRes = await fetch(`http://127.0.0.1:8080/${challengeName}/template.py`);
    const archivePath = `/files/${challengeName}/archive.zip`
    const testRes = await fetch(`http://127.0.0.1:8080/${challengeName}/test_.py`);
=======
    const descriptionRes = await fetch(`/files/${challengeName}/description.md`);

    if (descriptionRes.status != 200) {
        throw error(404, 'challenge no exist you stupiddo');
    }

    const templateRes = await fetch(`/files/${challengeName}/template.py`);
    const archivePath = `/files/${challengeName}/archive.zip`
    const testRes = await fetch(`/files${challengeName}/test_.py`);
>>>>>>> 1971a6a0ea1ae66944408c364722b2dc33813432

    const descriptionText = await descriptionRes.text();
    const templateText =  await templateRes.text()
    const testText = await testRes.text();
    return {
        description: descriptionText ,
        template: templateText,
        test: testText
    };
<<<<<<< HEAD
}
=======
}
>>>>>>> 1971a6a0ea1ae66944408c364722b2dc33813432
