<script lang="ts">
    import { Splitpanes, Pane } from "svelte-splitpanes";
    import CodeMirror from "./CodeMirror.svelte";
    import { isPyodideReady, pyodideState, pyodideWorkerPromise, testResult } from "$lib/stores/pyodide-store";
    import type { PageData } from "./$types";
    import CodeOutput from "./CodeOutput.svelte";

    export let code: string;

    async function handleRun(){
        const worker = await pyodideWorkerPromise
        await worker.runCode(code)
    }

    async function handleTest(){
        const worker = await pyodideWorkerPromise
        $testResult = await worker.testCode(code)
    }
    
</script>
<Splitpanes horizontal={true}>
    <Pane class="position-relative">
        <CodeMirror bind:value={code}/>
        <div class="text-light top-0 end-0 position-absolute d-flex justify-content-end gap-2 p-2 pe-4">
            {#if !$isPyodideReady}
                <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                {$pyodideState}...
            {/if}
            <button disabled='{!$isPyodideReady}' type="button" on:click={handleRun} class="btn btn-primary btn-sm">Run</button>
            <button disabled='{!$isPyodideReady}' type="button" on:click={handleTest} class="btn btn-secondary btn-sm">Test</button>
        </div>
    </Pane>
    <Pane>
        <CodeOutput/>
    </Pane>
</Splitpanes>