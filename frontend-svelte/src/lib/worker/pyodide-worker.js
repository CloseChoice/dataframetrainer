// Firefox does not support workers of type module yet
// Until that changes we can't use regular imports in vite development mode so this'll do
importScripts("https://unpkg.com/comlink/dist/umd/comlink.js");
importScripts("https://cdn.jsdelivr.net/pyodide/v0.23.3/full/pyodide.js")


async function loadPyodideAndPackages(){
    const pyodide = await loadPyodide()
    await pyodide.loadPackage("micropip");
    const micropip = await pyodide.pyimport("micropip");

    // Install Dependencies
    await Promise.all([
        micropip.install('hypothesis'),
        micropip.install('pandas'),
        micropip.install('numpy'),
        micropip.install('pytest')
    ])

    const mountDir = ".";
    await pyodide.FS.mount(pyodide.FS.filesystems.IDBFS, { root: "." }, mountDir);
    await Promise.all([
        pyodide.FS.mkdir('/home/pyodide/challenges'),
        pyodide.FS.mkdir('/home/pyodide/userSolutions'),
        pyodide.FS.mkdir('/home/pyodide/tests')
    ])
    await pyodide.FS.syncfs(true, function (err) {
        console.log(err);
        // handle callback
    });
    return pyodide;
}

let pyodideReadyPromise;

async function initialize(){
    pyodideReadyPromise = loadPyodideAndPackages()
    await pyodideReadyPromise
    return true
}

async function executeUserCode(userCode){
    const pyodide = await pyodideReadyPromise
    const resultUserCode = pyodide.runPython(userCode);
    console.log("executing user code: ", userCode);
    console.log("this is resultUserCode", resultUserCode);
    return resultUserCode
// todo: fill!
}

async function testUserCode(userCode, data){
    const pyodide = await pyodideReadyPromise
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

    return report
}


// Export functions to be used in pyodide-store
Comlink.expose({
    initialize,
    executeUserCode,
    testUserCode
})

