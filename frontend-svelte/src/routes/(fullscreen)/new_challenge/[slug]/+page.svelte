<script lang="ts">
    export let data: PageData;

    import CodeMirror from "./CodeMirror.svelte";
    import { isPyodideReady, pyodideWorkerPromise, pyodideState } from "$lib/stores/pyodide-store";
    import CodeOutput from "./CodeOutput.svelte";

    // https://github.com/nathancahill/split/tree/master/packages/splitjs
    import Split from 'split.js'
    import { onMount } from "svelte";
    import TestResults from "$lib/components/TestResult/index.svelte";
    import type { PytestResult } from "$lib/components/TestResult/pytest-result";
    import type { PageData } from "./$types";


    const description = data.intro;
    let code = data.default_code;
    let resultUserCode = "";

    let didChallengeLoad = false;
    let testResult: PytestResult | null = null;

    async function handleRun(){
        const worker = await pyodideWorkerPromise
        resultUserCode = await worker.runCode(code)
        console.log(resultUserCode);
    }

    async function handleTest(){
        const worker = await pyodideWorkerPromise
        const testResultString = await worker.testCode(code)
        testResult = JSON.parse(testResultString)
    }

    let splitEditor : HTMLElement;
    let splitConsole: HTMLElement;
    let splitLeft : HTMLElement;
    let splitRight : HTMLElement;
    onMount(()=>{
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
    // console.log('pyodideWorkerschmorker', pyodideWorkerPromise)
    pyodideWorkerPromise.then(async worker => {
        await worker.loadChallenge(data.challenge_class, data.challenge_test)
        didChallengeLoad = true
        // staticExample = worker.getStatic()
    })


    // Get static example

</script>

<div class="h-100 d-flex">
        <div bind:this={splitLeft} class="position-relative h-100 pt-5">

            <ul style="z-index:100" class="position-absolute top-0 nav nav-tabs w-100 bg-dark" id="myTab" role="tablist">
                <li class="nav-item" role="presentation">
                  <button class="nav-link " id="description-tab" data-bs-toggle="tab" data-bs-target="#description" type="button" role="tab" aria-controls="description" aria-selected="false">Description</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link" id="examples-tab" data-bs-toggle="tab" data-bs-target="#examples" type="button" role="tab" aria-controls="examples" aria-selected="false">Examples</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link active" id="tests-tab" data-bs-toggle="tab" data-bs-target="#tests" type="button" role="tab" aria-controls="tests" aria-selected="true">Test</button>
                </li>
              </ul>
              <div class="tab-content h-100 overflow-y-auto" id="myTabContent">
                <div class="tab-pane " id="description" role="tabpanel" aria-labelledby="description-tab">
                    {@html description}
                </div>
                <div class="tab-pane" id="examples" role="tabpanel" aria-labelledby="examples-tab">
                    random params plus expected output here
                </div>
                <div class="tab-pane show active" id="tests" role="tabpanel" aria-labelledby="tests-tab">
                    <TestResults bind:testResult={testResult}>

                    </TestResults>
                </div>
              </div>
        </div>
        <div bind:this={splitRight} class="h-100 col-6 d-flex flex-column" >
            <!-- min height:0 is necessary to prevent overflow  -->
            <div bind:this={splitEditor} class="flex-grow-1 position-relative" style="min-height:0">

                    <CodeMirror bind:value={code}/>
                    <div class="text-light top-0 end-0 position-absolute d-flex justify-content-end gap-2 p-2">
                        {#if !$isPyodideReady}
                            <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                            {$pyodideState}...
                        {/if}
                        <button disabled='{!$isPyodideReady}' type="button" on:click={handleRun} class="btn btn-primary btn-sm">Run</button>
                        <button disabled='{!$isPyodideReady}' type="button" on:click={handleTest} class="btn btn-secondary btn-sm">Test</button>
                    </div>
            </div>
            <div bind:this={splitConsole} style="min-height: 200px; background: green" >
                <CodeOutput resultUserCode={resultUserCode}/>
            </div>
        </div>
</div>


<style>
    :global(.gutter){
        background-color: var(--bs-border-color);
    }
    :global(.gutter:hover){

        background-color: blue;
    }
</style>