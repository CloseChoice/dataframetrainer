import { PyodideWorkerState } from '$lib/worker/types'
import type { PytestResult } from '$lib/components/TestTab/pytest-result'
import { Observable, Subject } from 'observable-fns'
import * as pyodidePackage from 'pyodide'
const {loadPyodide} = pyodidePackage
import type { PyodideInterface } from 'pyodide'
import {expose} from 'threads/worker'
import requirements from './requirements/requirements.json'
// get rid of this
// import dftCode from './dft.py?raw'
import pyodideLockFileURL from './requirements/repodata.json?url'

const stateSubject = new Subject<PyodideWorkerState>()
const stdoutSubject = new Subject<string>()
const pyodideReadyPromise = loadPyodideAndPackages()

async function loadPyodideAndPackages(){
    stateSubject.next(PyodideWorkerState.INSTALLING)
    const pyodide = await loadPyodide({
        indexURL: '/pyodide-indexurl',
        // If you change the requirements make sure to update the repodata.json lockfile (e.g by printing micropip.freeze() to console)
        lockFileURL: pyodideLockFileURL,
    })
    pyodide.setStdout({
        batched: (batch) => {
            console.log('print: ', batch)
            stdoutSubject.next(batch)
        }
    })

    await pyodide.loadPackage("micropip");
    const micropip = await pyodide.pyimport("micropip");
    await micropip.install(requirements)

    const mountDir = ".";
    await pyodide.FS.mount(pyodide.FS.filesystems.MEMFS, { root: "." }, mountDir);
    await Promise.all([
        pyodide.FS.mkdir('/home/pyodide/challenges'),
    ])
    
    console.log('🦆: Pyodidie and Modules were successfully installed')

    stateSubject.next(PyodideWorkerState.IDLE)
    return pyodide
}

type WithPyodideCallback<T> = (pyodide: PyodideInterface) => T
async function withPyodide<T>(state: PyodideWorkerState, callback: WithPyodideCallback<T>){
    stateSubject.next(state)
    const pyodide = await pyodideReadyPromise
    const res = await callback(pyodide)
    stateSubject.next(PyodideWorkerState.IDLE)
    return res
}

const worker = {
    state: ()=> Observable.from(stateSubject),
    stdout: () => Observable.from(stdoutSubject),
    loadChallenge: async (className: String, classFile: String, testFile: String) => {
        return withPyodide(PyodideWorkerState.LOADING_CHALLENGE, async (pyodide)=>{
            await pyodide.FS.writeFile(`challenges/${className}/test_${className}.py`, testFile, {encoding: "utf8"})
            await pyodide.FS.writeFile(`challenges/${className}/challenge.py`, classFile, {encoding: "utf8"})
            console.log('🦆: A new Challenge was successfully loaded')
        })
    },
    testCode: (className: String, code: String) => {
        return withPyodide(PyodideWorkerState.TESTING, async pyodide => {
            await pyodide.FS.writeFile(`challenges/${className}/submission.py`, code, {encoding: "utf8"})
            const pytestCode = `
            from importlib import reload
            import challenges.${className}.submission

            reload(challenges.${className}.submission)

            import pytest
            pytest.main(['--json-report', '--json-report-file' ,'challenges/${className}/report.json', '--capture=tee-sys', 'challenges/${className}'])`
            pyodide.runPython(pytestCode)
            // todo: where is the result saved? At best it would be saved in the challenge folder

            const testResult: PytestResult = JSON.parse(`challenges/${className}/report.json`)
            return testResult
        })
    },
    runCode: async (className: String, code: String) => {
        return withPyodide(PyodideWorkerState.RUNNING, async pyodide => {
            await pyodide.FS.writeFile("submission.py", code, {encoding: "utf8"})
            const pythonCode = `
                from importlib import reload
                import challenges.${className}.submission as submission
                from challenges.${className}.${className} import ${className}

                reload(challenges.${className}.submission)

                params_dict = ${className}.create_df_func()
                params = _get_params(params_dict)
                submission.transform(**params)
            `
            await pyodide.runPython(pythonCode)
        })
    },
    generateExample: async () => {
        // todo: get rid of dft here.
        return withPyodide(PyodideWorkerState.GENERATING_EXAMPLE, async pyodide =>{
            const res = await pyodide.pyimport("dft").generate_example()
            const example: ChallengeExample = JSON.parse(res)
            return example
        })
    }
}

export type PyodideWorker = typeof worker

export interface ChallengeExample {
    result: string;
    params: Record<string, string>;
  }
expose(worker)