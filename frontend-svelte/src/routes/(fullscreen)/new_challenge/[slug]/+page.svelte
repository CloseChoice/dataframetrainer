<script lang="ts">
    /** @type {import('./$types').PageData} */
    export let data;

    import { goto } from '$app/navigation';
    import {page} from '$app/stores'
    import axios from 'axios'
    import CodeMirror from "../../new_challenge/[slug]/CodeMirror.svelte";
    import { isPyodideReady, pyodideWorker } from "$lib/stores/pyodide-store";
    import CodeOutput from "../../new_challenge/[slug]/CodeOutput.svelte";

    // https://github.com/nathancahill/split/tree/master/packages/splitjs
    import Split from 'split.js'
    import { onMount } from "svelte";
    import TestResults from "$lib/components/TestTab/TestResults.svelte";
    import type { PytestResult } from "$lib/components/TestTab/pytest-result";


    const description = data.intro;
    let code = data.default_code;
    let test_challenge = data.test_challenge;
    let resultUserCode = "";
    let challengeName = data.challengeName;
    let submission = data.submission;

    let testResult: PytestResult | null = null;

    async function handleRun(){
        pyodideWorker.showStuff('/home/pyodide');
        resultUserCode = await pyodideWorker.executeUserCode(code)
    }
    async function handleTest(){
        pyodideWorker.showStuff('/home/pyodide');
        const testResultString = await pyodideWorker.testUserCode(code, data)
        testResult = JSON.parse(testResultString)
    }

    async function handleNewChallenge(){
        const userId = $page.data.session?.user?.id

        if (! userId) {
            alert("yer gotta be signed in for datt")
        }

        const res = await axios.post('/backend/get_next_challenge', {
            data: {
                user_id: userId
            }
        })
        const nextChallenge = res.data.next_challenge
        goto('/new_challenge/' + nextChallenge)

        
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
                            Loading Pyodide...
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