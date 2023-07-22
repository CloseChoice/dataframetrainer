import { writable } from 'svelte/store';

const timer = ms => new Promise(res => setTimeout(res, ms))
// Since pyodide is included via CDN we can't just use it right away, it might not have been loaded yet
// This function loads pyodide as soon as the loadPyodide function is available
async function ensurePyodide(){
    while (typeof loadPyodide === 'undefined'){
        await timer(30)
    }
    const py = await loadPyodide()
    return py
}

async function initPyodide(){
    const py = await ensurePyodide()
    await py.loadPackage("micropip");
    const micropip = await py.pyimport("micropip");

    // Install Dependencies
    await Promise.all([
        micropip.install('hypothesis'),
        micropip.install('pandas'),
        micropip.install('numpy'),
        micropip.install('pytest')
    ])

    const mountDir = ".";
    await py.FS.mount(py.FS.filesystems.IDBFS, { root: "." }, mountDir);
    await Promise.all([
        py.FS.mkdir('/home/pyodide/challenges'),
        py.FS.mkdir('/home/pyodide/userSolutions'),
        py.FS.mkdir('/home/pyodide/tests')
    ])
    await py.FS.syncfs(true, function (err) {
        console.log(err);
        // handle callback
    });
    isPyodideReady.set(true)
    return py;
}

// All functions which use pyodide have to resolve this promise to get the pyodide object
// The Code inside the promise (loading an initializing pyodide) only runs once
const pyodidePromise = initPyodide()
// isPyodideReady will be true after initPyodide successfully ran
export const isPyodideReady = writable(false);

export async function testPyodide(){
    const py = await pyodidePromise
    console.log(py);
}

export async function executeUserCode(userCode:String){
    const pyodide = await pyodidePromise
    const resultUserCode = pyodide.runPython(userCode);
    console.log("executing user code: ", userCode);
    console.log("this is resultUserCode", resultUserCode);
    return resultUserCode
// todo: fill!
}

export async function testUserCode(userCode:String, data){
    const pyodide = await pyodidePromise
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