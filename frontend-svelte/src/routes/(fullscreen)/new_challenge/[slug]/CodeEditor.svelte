<script lang="ts">
    import { Splitpanes, Pane } from "svelte-splitpanes";
    import CodeMirror from "./CodeMirror.svelte";
    import { isPyodideReady, pyodideState, pyodideWorkerPromise, testResult } from "$lib/stores/pyodide-store";
    import CodeOutput from "./CodeOutput.svelte";
    import axios from "axios";
    import { API_BASE_URL } from "../../../config";
    export let code: string;
    export let challengeName: string;

    import {page} from '$app/stores'
    import {getContext} from 'svelte'

    // const data = getContext('data')

    async function handleRun(){
        const worker = await pyodideWorkerPromise
        await worker.runCode(code)
    }

    async function handleTest(){
        const worker = await pyodideWorkerPromise
        const res = await worker.testCode(code)
        // console.log("THIS IS THE RESULT", challengeName);
        // console.log("This is the user name", $page)
        if (res){
             const outcome = res.tests[0].call?.outcome;
             const userId = $page.data?.session?.user.userId;
             const haveAllTestsPassed = outcome === "passed";
             testResult.set(res)
             axios.post(`${API_BASE_URL}/post_challenge_results/${challengeName}/`, {
                session_id: $page.data?.session?.sessionId || null,
                challenge_result: haveAllTestsPassed,
                challenge_name: challengeName,
                user_id: userId,
         });
        }
    }
</script>
<Splitpanes horizontal={true}>
    <Pane class="position-relative">
        {#key challengeName}
            <CodeMirror bind:value={code}/>
            {/key}
        <div class="text-light top-0 end-0 position-absolute d-flex justify-content-end gap-2 p-2 pe-4">
            <div data-test='pyodide-state' data-state={$pyodideState}>
                {#if !$isPyodideReady}
                    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                    {$pyodideState}...
                {/if}
            </div>
            <button data-test="run-button" disabled='{!$isPyodideReady}' type="button" on:click={handleRun} class="btn btn-primary btn-sm">Run</button>
            <button data-test="test-button" disabled='{!$isPyodideReady}' type="button" on:click={handleTest} class="btn btn-secondary btn-sm" >Test</button>
        </div>
    </Pane>
    <Pane>
        <CodeOutput/>
    </Pane>
</Splitpanes>