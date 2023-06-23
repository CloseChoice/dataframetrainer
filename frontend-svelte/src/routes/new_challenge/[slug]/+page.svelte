<script>
    import { onMount } from "svelte";
    import { XMLParser } from 'fast-xml-parser'

    const parser = new XMLParser();
    /** @type {import('./$types').PageData} */
    export let data;
    let userCode;

    let pyodide;
    onMount(async ()=>{
        pyodide = await loadPyodide();

        await pyodide.loadPackage("micropip");
        const micropip = pyodide.pyimport("micropip");
        await micropip.install('hypothesis');
        await micropip.install('pandas');
        await micropip.install('numpy');
        await micropip.install('pytest');
    })

    async function testUserCode(){
        pyodide.runPython(userCode);
        console.log("ran usercode", userCode);
        let transform_func = pyodide.globals.get('transform');
        // console.log("THIS IS transform", transform_func);
        // todo: alert if transform is not defined and BONUS: show the defined functions
        if (!pyodide.isPyProxy(transform_func)) {
            alert("transform function is not defined! Please define this function otherwise we can't evaluate the code.");
            console.log("is pyproxy");
        }

        // the define the class
        pyodide.runPython(data.challenge_class);
        // todo: we need to find a better solution to extract the result of the test_challenge function
        // here runs the testing stuff
        // let exitCode = pyodide.runPython(`${data.challenge_name}().test_challenge(transform_func=transform)`);
        // this also works, maybe this can help us to use a pytest plugin in order to capture the std/sterr
        let exitCode = pyodide.runPython(`
        import pytest

        def test_transform():
            ${data.challenge_name}().test_challenge(transform_func=transform)

        if __name__ == "__main__":
            pytest.main(['--junitxml', 'report.xml'])`
            );
        console.log("exitcode", exitCode);
        let report = pyodide.FS.readFile('report.xml',  { encoding: "utf8" })
    }
</script>

<div>
    <h1>Hier ist die Description</h1>
    {data.intro}
</div>

<div>
    <h1>So sieht die Startzelle für die Challenge aus</h1>
    <textarea value={data.default_code} name="Text1" cols="60" rows="10"></textarea>
    <h1>Hier kann man mal temporär eine Lösung reinschreiben</h1>
    <h4>Später sollte man keine zwei Zellen brauchen, sondern am Anfang sieht sie so aus wie oben, später dann wie unten</h4>
    <textarea bind:value={userCode} name="Text2" cols="40" rows="5"></textarea>
</div>

<button on:click={testUserCode}>Submit Code</button>
