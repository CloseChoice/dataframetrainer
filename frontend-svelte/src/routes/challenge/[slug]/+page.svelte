<script>
    // import { loadPyodide } from "pyodide";
    import { onMount } from "svelte";
    /** @type {import('./$types').PageData} */
    export let data;

    console.log(data);


    let pyodide;

    onMount(async ()=>{
        pyodide = await loadPyodide()

        let mountDir = "/mnt";
        pyodide.FS.mkdir(mountDir);
        pyodide.FS.mount(pyodide.FS.filesystems.IDBFS, { root: "." }, mountDir);
        

        await pyodide.loadPackage("micropip");
        const micropip = pyodide.pyimport("micropip");
        await micropip.install('hypothesis');
        await micropip.install('pytest')

        // pyodide.FS.writeFile("test_.py", data.test, {encoding: "utf8"})

        // extract the folder
        // const response = await fetch(data.archivePath);
        // let buffer = await response.arrayBuffer();
        // await pyodide.unpackArchive(buffer, 'zip');
        // pyodide.pyimport("your_package");

        pyodide.runPython(`import os
print(os.listdir())`)

    })


    let userCode = data.template

    async function testUserCode(){
        console.log(userCode);

        // let mountDir = "/mnt";
        // pyodide.FS.mkdir(mountDir);
        // pyodide.FS.mount(pyodide.FS.filesystems.IDBFS, { root: "." }, mountDir);

        pyodide.FS.writeFile("solution.py", userCode, {encoding: "utf8"})
        pyodide.FS.writeFile("test_.py", data.test, {encoding: "utf8"})

        // let pkg = pyodide.pyimport("pytest");
        // let x = pkg.main();
        // console.log(x);

        pyodide.FS.syncfs()
        pyodide.runPython(`import pytest
pytest.main()
`)
    }
    
</script>

<div>
    <h1>Hier ist die Description</h1>
    {data.description}
</div>

<div>
    <h1>Hier ist der Kot editorr</h1>
    <textarea bind:value={userCode} name="Text1" cols="40" rows="5"></textarea>
    
</div>

<button on:click={testUserCode}>Submit Code</button>