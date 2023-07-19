<script>
    import CodeMirror from "./CodeMirror.svelte";
    import CodeOutput from "./CodeOutput.svelte";
    /** @type {import('./$types').PageData} */
    export let data;

    import {executeUserCode, testUserCode, isPyodideReady} from './python-runner'

    const descritption = data.intro
    let code = data.default_code
    let resultUserCode = "";

    async function handleRun(){
        resultUserCode = await executeUserCode(code)
    }
    async function handleTest(){
        testUserCode(code, data)
    }
</script>


<div class="row ">
    <div class="col">
        {@html descritption}
    </div>
    <div class="col-6" style="height:500px">
        <div class="d-flex justify-content-end gap-2 p-2">
            {#if !$isPyodideReady}
                <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                Loading Pyodide...
            {/if}
            <button disabled='{!$isPyodideReady}' type="button" on:click={handleRun} class="btn btn-primary btn-lg">Run</button>
            <button disabled='{!$isPyodideReady}' type="button" on:click={handleTest} class="btn btn-secondary btn-lg">Test</button>
        </div>
        <CodeMirror bind:value={code}/>
        <CodeOutput resultUserCode={resultUserCode}/>
    </div>
</div>
