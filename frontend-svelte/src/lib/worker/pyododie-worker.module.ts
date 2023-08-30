import { PyodideWorkerState } from '$lib/worker/types'
import type { PytestResult } from '$lib/components/TestTab/pytest-result'
import { Observable, Subject } from 'observable-fns'
import * as pyodidePackage from 'pyodide'
const {loadPyodide} = pyodidePackage
import type { PyodideInterface } from 'pyodide'
import {expose} from 'threads/worker'
import requirements from './requirements/requirements.json'
import dftCode from './dft.py?raw'
import pyodideLockFileURL from './requirements/repodata.json?url'

const stateSubject = new Subject<PyodideWorkerState>()
const stdoutSubject = new Subject<string>()
const stderrSubject = new Subject<Error>()

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
    
    await pyodide.FS.writeFile("dft.py", dftCode, { encoding: "utf8" });
    
    console.log('🦆: Pyodidie and Modules were successfully installed')

    pyodide.FS.mkdir('challenges'),
    pyodide.FS.mkdir('userSolutions'),
    pyodide.FS.mkdir('tests')


    stateSubject.next(PyodideWorkerState.IDLE)
    return pyodide
}

const pyodideReadyPromise = loadPyodideAndPackages()

type WithPyodideCallback<T> = (pyodide: PyodideInterface) => T
async function withPyodide<T>(state: PyodideWorkerState, callback: WithPyodideCallback<T>){
    stateSubject.next(state)
    const pyodide = await pyodideReadyPromise
    try {
        const res = await callback(pyodide)
        stateSubject.next(PyodideWorkerState.IDLE)
        return res
    } catch (error) {
        // Here we would like to check if the error is a PythonError but since pyodide only exports the type and not the class this is not possible right away
        if (error instanceof Error) {
            console.error(error)
            stderrSubject.next(error)
            stateSubject.next(PyodideWorkerState.IDLE)
            return false
        }
        
    }
}

let challengeName: string;

const worker = {
    state: ()=> Observable.from(stateSubject),
    stdout: () => Observable.from(stdoutSubject),
    stderr: () => Observable.from(stderrSubject),
    loadChallenge: async (classFile: string, testFile: string, name: string) => {
        challengeName = name;
        return withPyodide(PyodideWorkerState.LOADING_CHALLENGE, async (pyodide)=>{
            if (!pyodide.FS.readdir('challenges').includes(name)){
                await pyodide.FS.mkdir(`challenges/${name}`)
            }
            await pyodide.FS.writeFile(`./challenges/${name}/test_${name}.py`, testFile);
            await pyodide.FS.writeFile(`./challenges/${name}/${name}.py`, classFile);
            console.log('🦆: A new Challenge was successfully loaded')
        })
    },
    testCode: (code: string) => {
        return withPyodide(PyodideWorkerState.TESTING, async pyodide=>{

            // await pyodide.FS.writeFile("submission.py", code, {encoding: "utf8"})
            await pyodide.FS.writeFile(`./challenges/${challengeName}/submission.py`, code);
            console.log(pyodide.FS.readdir(`challenges/${challengeName}`))
            const res = await pyodide.pyimport("dft").test_code(challengeName)
            const testResult: PytestResult = JSON.parse(res)
            return testResult
        })
    },
    runCode: async (code: string) => {
        return withPyodide(PyodideWorkerState.RUNNING, async pyodide => {
            await pyodide.FS.writeFile(`./challenges/${challengeName}/submission.py`, code);
            await pyodide.pyimport("dft").run_code(challengeName)
        })
    },
    generateExample: async () => {
        return withPyodide(PyodideWorkerState.GENERATING_EXAMPLE, async pyodide =>{
            const res = await pyodide.pyimport("dft").generate_example(challengeName)
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