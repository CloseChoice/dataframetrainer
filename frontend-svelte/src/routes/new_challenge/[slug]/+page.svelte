<script lang="ts">
    import CodeMirror from "./CodeMirror.svelte";
    import { isPyodideReady, pyodideWorker } from "$lib/stores/pyodide-store";
    /** @type {import('./$types').PageData} */
    export let data;
    // https://github.com/nathancahill/split/tree/master/packages/splitjs
    import Split from 'split.js'
    import { onMount } from "svelte";

    const descritption = data.intro
    let code = data.default_code
    let resultUserCode = "";

    async function handleRun(){
        if ($isPyodideReady) {
            resultUserCode = await pyodideWorker.executeUserCode(code)
        }
    }
    async function handleTest(){
        if ($isPyodideReady) {
            await pyodideWorker.testUserCode(code, data)
        }
    }

    let splitEditor;
    let splitConsole;
    let splitLeft;
    let splitRight;

    onMount(async ()=>{
        
        Split([splitEditor, splitConsole], {
            sizes: [75, 25],
            minSize: [200, 200],
            direction: 'vertical',
            snapOffset: 0,
        })

        Split([splitLeft, splitRight], {
            sizes: [50, 50],
            minSize: [200, 200],
            snapOffset: 0,
        })
    })

</script>

<div class="h-100">
    <div class="row gx-0 h-100">
        <div bind:this={splitLeft} class="col-6">
            {@html descritption}
        </div>
        <div bind:this={splitRight} class="h-100 col-6 d-flex flex-column" >
            <!-- min height:0 is necessary to prevent overflow  -->
            <div bind:this={splitEditor} class="flex-grow-1 position-relative" style="min-height:0">

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
            <div bind:this={splitConsole} style="min-height: 200px; background: green" >
                shish
                <!-- <CodeOutput resultUserCode={resultUserCode}/> -->
            </div>
        </div>
    </div>
</div>


<style>
    :global(.gutter){

        background-color: black;
    }
    :global(.gutter:hover){

        background-color: blue;
    }
</style>