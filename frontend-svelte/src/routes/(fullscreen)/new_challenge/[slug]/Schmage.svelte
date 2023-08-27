<script lang="ts">
    export let data: PageData;
    // import {TabContent} from 'sveltes'
    import CodeMirror from "./CodeMirror.svelte";
    import { isPyodideReady, pyodideWorkerPromise, pyodideState } from "$lib/stores/pyodide-store";
    import CodeOutput from "./CodeOutput.svelte";

    import {TabContent, TabPane} from 'sveltestrap'
    import { SplitPane } from '@rich_harris/svelte-split-pane';

    // https://github.com/nathancahill/split/tree/master/packages/splitjs
    import Split from 'split.js'
    import { onMount } from "svelte";
    import TestResults from "$lib/components/TestTab/TestResults.svelte";
    import type { PytestResult } from "$lib/components/TestTab/pytest-result";
    import type { PageData } from "./$types";
    import DescriptionTab from "./DescriptionTab.svelte";


    const description = data.intro;
    let code = data.default_code;

    let didChallengeLoad = false;
    let testResult: PytestResult | null = null;
    let activeTab = 'description'
    async function handleRun(){
        const worker = await pyodideWorkerPromise
        await worker.runCode(code)
    }

    async function handleTest(){
        const worker = await pyodideWorkerPromise
        testResult = await worker.testCode(code)
        activeTab = 'tests'
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
    let staticExample = {}
    pyodideWorkerPromise.then(async worker => {
        console.log('loaded data schmata');
        
        await worker.loadChallenge(data.challenge_class, data.challenge_test)
        didChallengeLoad = true
        // staticExample = worker.getStatic()
    })

</script>

<div class="h-100 d-flex">
        <div bind:this={splitLeft} class="position-relative h-100">
            {#key activeTab}
            <TabContent>
                <TabPane tabId="description" tab="Description" active={activeTab == 'description'}>
                    <DescriptionTab staticExample={staticExample} description={description}/>
                </TabPane>
                <TabPane tabId="tests" tab="Tests" active={activeTab == 'tests'}>
                    <TestResults bind:testResult={testResult}/>
                </TabPane>
                
            </TabContent>
            {/key}
        </div>
        <SplitPane
        type="vertical"
        id="main"
        min="100px"
        max="-100px"
        pos="50%"
        priority="min"
        --color='red'
        --thickness='10px'
        >
        <section slot="a">this is on the left</section>
        <section slot="b">this is on the right</section>
        </SplitPane>
        <!-- <div bind:this={splitRight} class="h-100 col-6 d-flex flex-column" >
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
                <CodeOutput/>
            </div>
        </div> -->
</div>


<style>
    :global(.gutter){
        background-color: var(--bs-border-color);
    }
    :global(.gutter:hover){

        background-color: blue;
    }
</style>