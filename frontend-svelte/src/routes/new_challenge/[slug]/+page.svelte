<script>
    import { onMount } from "svelte";
    import { XMLParser } from 'fast-xml-parser';
    // todo: this needs to move in the src/components folder
    import CodeMirror from "./CodeMirror.svelte";



    const parser = new XMLParser();
    /** @type {import('./$types').PageData} */
    export let data;
    let userCode;
    let editor;
    let startState;

    let pyodide;
    async function executeUserCode(){
        console.log("executing user code: ", userCode);
    // todo: fill!
    }

    async function testUserCode(){
        // pyodide.FS.writeFile(userCode, '/mnt/usercode.py');
        // todo: this needs a cleanup!
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

  let loadDone = false;
  let edConfigMD = {
    language: 'python',
    lineNumbers: false,
    lineWrapping: true,
    lineHighlight: true
  };
  let cm;

    onMount(async ()=>{
        loadDone = true;
        pyodide = await loadPyodide();

        await pyodide.loadPackage("micropip");
        const micropip = pyodide.pyimport("micropip");
        await micropip.install('hypothesis');
        await micropip.install('pandas');
        await micropip.install('numpy');
        await micropip.install('pytest');

        userCode = data.default_code;
        let mountDir = ".";
        pyodide.FS.mount(pyodide.FS.filesystems.IDBFS, { root: "." }, mountDir);
        pyodide.FS.mkdir('/home/pyodide/challenges');
        pyodide.FS.mkdir('/home/pyodide/userSolutions');
        pyodide.FS.mkdir('/home/pyodide/tests');
        console.log("this is default_code", data.default_code);
        pyodide.FS.syncfs(true, function (err) {
  console.log(err);
  // handle callback
  });
});
  console.log("Synced folder");

  function textChange(e) {
    userCode = e.detail.data.value;
    console.log("userCode changed", userCode);
  }

  function editorChange(e) {
    cm = e.detail.data;
  }

  function addText(e) {
    if(typeof cm !== 'undefined') {
      userCode += userCode;
      cm.setValue(userCode);
    }
  }
</script>

<div>
    {data.intro}
</div>

<button on:click={testUserCode}>Submit Code</button>
<button on:click={executeUserCode}>Execute Code</button>

Dummy 
<div id="firstEd">
    <CodeMirror
    height="4000px"
    width="1000px"
    config={edConfigMD}
    initFinished={loadDone};
    defaultCode={data.default_code};
    on:textChange={textChange}
    on:editorChange={editorChange}
    />
</div>
After Dummy 