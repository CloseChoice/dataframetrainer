import { derived, writable, get, readable } from 'svelte/store'
import type { Writable } from 'svelte/store';
import type {  PyodideWorker } from '$lib/worker/pyododie-worker.module';
import MyWorker from '$lib/worker/pyododie-worker.module?worker'
import { spawn, Worker, type ModuleThread} from 'threads'
import { PyodideWorkerState } from '$lib/worker/types';

let resolvePyodideReadyPromise: (worker: ModuleThread<PyodideWorker>) => void
let rejectPyodideReadyPromise
export let pyodideWorkerPromise: Promise<ModuleThread<PyodideWorker>> = new Promise((resolve, reject) => {
    resolvePyodideReadyPromise = resolve
})

export const pyodideStdout: Writable<string[]> = writable([])

export const pyodideState = writable('loading')

export const isPyodideReady = derived(
    pyodideState,
    ($pyodideState) => {
        return $pyodideState === 'idle'
    }
)

export async function initPyodideStore(){
    const worker = await spawn<PyodideWorker>(new MyWorker())

    worker.stdout().subscribe(newLine => {
        pyodideStdout.update(lines => {
            lines.push(newLine)
            return lines
        })
    })

    worker.state().subscribe(state => {
        pyodideState.set(state)
        const statesThatResetConsole = [
            PyodideWorkerState.RUNNING, 
            PyodideWorkerState.LOADING_CHALLENGE, 
            PyodideWorkerState.TESTING
        ]
        if (statesThatResetConsole.includes(state)){
            pyodideStdout.set([])
        }
    })

    resolvePyodideReadyPromise(worker)
}