<script>
    // import { loadPyodide } from "pyodide";
    import { onMount } from "svelte";
    /** @type {import('./$types').PageData} */
    export let data;

    console.log(data);


    let pyodide;

    onMount(async ()=>{
        pyodide = await loadPyodide()

        await pyodide.loadPackage("micropip");
        const micropip = pyodide.pyimport("micropip");
        await micropip.install('hypothesis');
        await micropip.install('pytest')
        await micropip.install('pytest-xdist')

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
        // console.log(userCode);


        pyodide.FS.writeFile("solution.py", userCode, {encoding: "utf8"})
        pyodide.FS.writeFile("test_.py", data.test, {encoding: "utf8"})

//         pyodide.runPythonAsync(`
// with open("solution.py") as f:
//     print(f.readlines())`)

        pyodide.code.eval(`import pytest
pytest.main()`)
        // let pkg = pyodide.pyimport("test_");
        // let x = pkg.test();
        // console.log(x);

        // pyodide.runPython(data.test)
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