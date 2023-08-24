<script lang="ts">
    import type { PytestResult } from "./pytest-result";

    export let testResult: PytestResult | null = null
    import sampleReport from "./sample-report.json"
    import SingleTestResult from "./SingleTestResult.svelte";
    // const testResult: PytestResult = sampleReport
    
    console.log(testResult);
    console.log('sheeesh');
    
    
    
</script>
<div class="p-2">
    {#if !testResult}
        You need to run a test to see the result
    {:else}
        {#each testResult.tests as test }
            <SingleTestResult test={test}/>
        {/each}
    {/if}
</div>