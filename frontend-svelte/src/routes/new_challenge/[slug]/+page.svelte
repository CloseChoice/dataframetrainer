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

<div class="h-100">
    <div class="row gx-0 h-100">
        <div class="col-6">
            {@html descritption}
        </div>
        <div class="h-100 col-6 d-flex flex-column" >
            <!-- min height:0 is necessary to prevent overflow  -->
            <div class="flex-grow-1 position-relative" style="min-height:0">

                    <CodeMirror bind:value={code}/>
                    <div class="text-light top-0 end-0 position-absolute d-flex justify-content-end gap-2 p-2">
                        {#if !$isPyodideReady}
                            <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                            Loading Pyodide...
                        {/if}
                        <button disabled='{!$isPyodideReady}' type="button" on:click={handleRun} class="btn btn-primary btn-sm">Run</button>
                        <button disabled='{!$isPyodideReady}' type="button" on:click={handleTest} class="btn btn-secondary btn-sm">Test</button>
                    </div>
            </div>
            <div style="min-height: 200px; background: green" >
                shish
                <!-- <CodeOutput resultUserCode={resultUserCode}/> -->
            </div>
        </div>
    </div>
</div>