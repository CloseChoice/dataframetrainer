import { error } from '@sveltejs/kit';

/** @type {import('./$types').PageServerLoad} */
export async function load({ params, fetch }) {
    console.log(params.slug);

    const challengeName = params.slug

    const descriptionRes = await fetch(`/files/${challengeName}/description.md`);

    if (descriptionRes.status != 200) {
        throw error(404, 'challenge no exist you stupiddo');
    }

    const templateRes = await fetch(`/files/${challengeName}/template.py`);
    const archivePath = `/files/${challengeName}/archive.zip`
    const testRes = await fetch(`/files${challengeName}/test_.py`);

    const descriptionText = await descriptionRes.text();
    const templateText =  await templateRes.text()
    const testText = await testRes.text();
    return {
        description: descriptionText ,
        template: templateText,
        test: testText
    };
}