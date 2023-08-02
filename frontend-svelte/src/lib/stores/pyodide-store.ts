import * as Comlink from 'comlink'
import { writable } from 'svelte/store'

export let pyodideWorker: null | Comlink.Remote<any> = null

export async function initPyodideStore(){
    const worker = new Worker(new URL('../worker/pyodide-worker.js', import.meta.url))
    pyodideWorker = Comlink.wrap(worker)
    
    await pyodideWorker.initialize()
    isPyodideReady.set(true)
}


export const isPyodideReady = writable(false)


