import * as Comlink from 'comlink'
import { derived, writable, get, readable } from 'svelte/store'
import type { Writable } from 'svelte/store';
import type { PytestResult } from '$lib/components/TestTab/pytest-result';

export let pyodideWorker: null | Comlink.Remote<any> = null



enum PyodideState {
    LOADING = "loading",
    TESTING = "testing",
    RUNNING = "running",
    IDLE = "idle"
}

function stateChangeCallback(state: PyodideState){    
    pyodideState.set(state)
}

// const initialStdout: = []:string[]
export const pyodideStdout: Writable<string[]> = writable([])
export const testResult: Writable<PytestResult | null> = writable(null);

function stdoutCallback(line: string){
    pyodideStdout.update((stdout) => {
        stdout.push(line)
        return stdout
    })

}


export async function initPyodideStore(){
    const worker = new Worker(new URL('../worker/pyodide-worker.ts', import.meta.url))
    pyodideWorker = Comlink.wrap(worker)

    // Make sure to set the callbacks before initializing the web worker
    // pyodideWorker.stateChangeCallback = Comlink.proxy(stateChangeCallback)
    pyodideWorker.on('stateChange', Comlink.proxy(stateChangeCallback))
    pyodideWorker.on('stdout', Comlink.proxy(stdoutCallback))
    pyodideWorker.initialize()
    
    // isPyodideReady.set(true)
}

export const pyodideState = writable(PyodideState.LOADING)

export const isPyodideReady = derived(
    pyodideState,
    ($pyodideState) => {
        return $pyodideState === PyodideState.IDLE
    }
)
