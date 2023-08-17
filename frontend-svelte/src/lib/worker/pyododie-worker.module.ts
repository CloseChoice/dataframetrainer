import { Observable, Subject } from 'observable-fns'
import * as pyodidePackage from 'pyodide'
const {loadPyodide} = pyodidePackage
import {expose} from 'threads/worker'
import dftCode from './dft.py?raw'
import pyodideLockFileURL from './repodata.json?url'
console.log(pyodideLockFileURL)

const stateSubject = new Subject<PyodideWorkerState>()
const stdoutSubject = new Subject<string>()
const pyodideReadyPromise = loadPyodideAndPackages()

const dependencies = [
    'hypothesis',
    'pandas',
    'numpy',
    'pytest',
    // pytest-json
    'https://files.pythonhosted.org/packages/81/35/d07400c715bf8a88aa0c1ee9c9eb6050ca7fe5b39981f0eea773feeb0681/pytest_json_report-1.5.0-py3-none-any.whl'
]

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
    await micropip.install(dependencies)
    
    await pyodide.FS.writeFile("dft.py", dftCode, { encoding: "utf8" });
    
    console.log('🦆: Pyodidie and Modules were successfully installed')

    stateSubject.next(PyodideWorkerState.IDLE)
    return pyodide
}

const worker = {
    state: ()=> Observable.from(stateSubject),
    stdout: () => Observable.from(stdoutSubject),
    loadChallenge: async (classFile: String, testFile: String) => {
        stateSubject.next(PyodideWorkerState.LOADING_CHALLENGE)
        const pyodide = await pyodideReadyPromise
        await pyodide.FS.writeFile("test_.py", testFile, {encoding: "utf8"})
        await pyodide.FS.writeFile("challenge.py", classFile, {encoding: "utf8"})
        console.log('🦆: A new Challenge was successfully loaded')
        
        stateSubject.next(PyodideWorkerState.IDLE)
    },
    testCode: async (code: String) => {
        stateSubject.next(PyodideWorkerState.TESTING)
        const pyodide = await pyodideReadyPromise
        await pyodide.FS.writeFile("submission.py", code, {encoding: "utf8"})
        const dftModule = await pyodide.pyimport("dft");
        const res = await dftModule.test_code()
        stateSubject.next(PyodideWorkerState.IDLE)
        return res
    },
    runCode: async (code: String) => {
        stateSubject.next(PyodideWorkerState.RUNNING)
        const pyodide = await pyodideReadyPromise
        await pyodide.FS.writeFile("submission.py", code, {encoding: "utf8"})
        const dftModule = await pyodide.pyimport("dft");
        const res = dftModule.run_code()
        stateSubject.next(PyodideWorkerState.IDLE)
        return res
    },
    generateExample: async (): Promise<ChallengeExample> => {
        stateSubject.next(PyodideWorkerState.GENERATING_EXAMPLE)
        const pyodide = await pyodideReadyPromise
        const dftModule = await pyodide.pyimport("dft");
        const res = dftModule.generate_example()
        stateSubject.next(PyodideWorkerState.IDLE)
        return JSON.parse(res)
    }
}

export type PyodideWorker = typeof worker
export enum PyodideWorkerState{
    LOADING_CHALLENGE = 'loading challenge',
    IDLE = 'idle',
    RUNNING = 'running',
    TESTING = 'testing',
    INSTALLING = 'installing pyodidie',
    GENERATING_EXAMPLE = 'generating example'
}
export interface ChallengeExample {
    result: string;
    params: Record<string, string>;
  }
expose(worker)