<script lang="ts">
    import {TabContent, TabPane} from 'sveltestrap'
    import DescriptionTab from './DescriptionTab.svelte';
    import TestResult from "$lib/components/TestTab/TestResults.svelte"
    import { Pane, Splitpanes } from 'svelte-splitpanes';
    import CodeEditor from './CodeEditor.svelte';
    import type { PageData } from './$types';
    import { onMount } from 'svelte';
    import { pyodideWorkerPromise, testResult } from '$lib/stores/pyodide-store';
    import type { ChallengeExample } from '$lib/worker/pyododie-worker.module';
    export let data: PageData;


    enum TabIDs {DESCRIPTION = 'description', TESTS = "tests", EDITOR = "editor"}
    let activeTab: string | number = 'description'


    let windowInnerWidth: number;
    $: displayMobile = windowInnerWidth < 1000;
    // Editor tab is only visible on mobile. When the screen changes from mobile to desktop select description tab
    $: if (!displayMobile && activeTab === TabIDs.EDITOR) {
		activeTab = TabIDs.DESCRIPTION
	}
    // Change to test tab whenever a test finishes
    $: $testResult, activeTab = TabIDs.TESTS

    let code = data.default_code
    let staticExample: ChallengeExample
    onMount(async ()=>{
        const worker = await pyodideWorkerPromise
        await worker.loadChallenge(data.challenge_class, data.challenge_test)
    })
</script>

<svelte:window bind:innerWidth={windowInnerWidth} />

<div class="h-100">
    <Splitpanes>
        <Pane>
            {#key activeTab}
            <TabContent on:tab={(e) => activeTab=e.detail} class="h-100 d-flex flex-column">
                <TabPane class="flex-grow-1 overflow-y-auto"  tabId="description" tab="Description" active={activeTab == TabIDs.DESCRIPTION}>
                    <DescriptionTab description={data.intro} staticExample={staticExample}/>
                </TabPane>
                <TabPane class="flex-grow-1 overflow-y-auto"  tabId="tests" tab="Tests" active={activeTab == TabIDs.TESTS}>
                    <TestResult/>
                </TabPane>
                {#if displayMobile}
                <TabPane class="flex-grow-1" tabId="editor" tab="Editor" active={activeTab == TabIDs.EDITOR}>
                    <CodeEditor bind:code={code}/>
                </TabPane>
                {/if}
            </TabContent>
            {/key}
        </Pane>
        {#if !displayMobile}
        <Pane>
            <CodeEditor bind:code={code}/>
        </Pane>
        {/if}
    </Splitpanes>
            
 
</div>