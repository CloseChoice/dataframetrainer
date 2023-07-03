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

        let mountDir = ".";
        pyodide.FS.mount(pyodide.FS.filesystems.IDBFS, { root: "." }, mountDir);
        pyodide.FS.mkdir('/home/pyodide/challenges');
        pyodide.FS.mkdir('/home/pyodide/userSolutions');
        pyodide.FS.mkdir('/home/pyodide/tests');
        pyodide.FS.syncfs(true, function (err) {
  console.log(err);
  // handle callback
  });
        console.log("Synced folder");
    })

    async function testUserCode(){
        // pyodide.FS.writeFile(userCode, '/mnt/usercode.py');
        pyodide.runPython("import os; print(os.listdir('/home/pyodide/'))");
        pyodide.FS.writeFile('usercode.py', userCode);
        pyodide.runPython("import os; print(os.listdir('.'))");
        pyodide.runPython(userCode);
        console.log("ran usercode", userCode);
        let transform_func = pyodide.globals.get('transform');
        // console.log("THIS IS transform", transform_func);
        // todo: alert if transform is not defined and BONUS: show the defined functions
        if (!pyodide.isPyProxy(transform_func)) {
            alert("transform function is not defined! Please define this function otherwise we can't evaluate the code.");
            console.log("is pyproxy");
        }
        // todo: maybe we need a reload here!
        let transform_code = pyodide.runPython(`
        import inspect
        from usercode import transform

        inspect.getsource(transform)`);
        console.log("transform code", transform_code);

        // the define the class
        pyodide.runPython(data.challenge_class);
        let s = `
import pytest
${data.challenge_class}

${transform_code}

def test_transform():
    ${data.challenge_name}().test_challenge(transform_func=transform)
    print('in main')
`;
        console.log(s);

        pyodide.FS.writeFile(`test_${data.challenge_name}.py`, s);
        pyodide.runPython(`import pytest; pytest.main(['--junitxml', 'report.xml', '-k', 'test_transform', '-x', '/home/pyodide/test_${data.challenge_name}.py'])`);
        pyodide.runPython("import os; print(os.listdir('.'))");
        // let exitCode = pyodide.runPython(`test_${data.challenge_name}.py`);
        // console.log("This is the exitCode", exitCode);
        // pyodide.runPython
        let report = pyodide.FS.readFile('report.xml', { encoding: "utf8" })
        console.log("This is the report", report);
        pyodide.FS.syncfs(true, function (err) {
  console.log(err);
  // handle callback
  });
        console.log("Synced");
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
