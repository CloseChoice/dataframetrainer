<script>
    // import { loadPyodide } from "pyodide";
    import { onMount } from "svelte";
    import {XMLParser} from 'fast-xml-parser'

    const parser = new XMLParser();
    /** @type {import('./$types').PageData} */
    export let data;
    let pyodide;
    let userCode = data.template;

    onMount(async ()=>{
        pyodide = await loadPyodide()

        await pyodide.loadPackage("micropip");
        const micropip = pyodide.pyimport("micropip");
        await micropip.install('hypothesis');
        await micropip.install('pytest')

        pyodide.FS.writeFile("test_.py", data.test, {encoding: "utf8"})
        pyodide.FS.writeFile("solution.py", userCode, {encoding: "utf8"})
    })

    async function testUserCode(){
        pyodide.FS.writeFile("solution.py", userCode, {encoding: "utf8"})
        let exitCode = pyodide.runPython(`from importlib import reload
import pytest
import test_
import solution

reload(solution)
reload(test_)

pytest.main(['--junitxml', 'report.xml'])`)
        console.log("exitcode", exitCode);
        let report = pyodide.FS.readFile('report.xml',  { encoding: "utf8" })
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