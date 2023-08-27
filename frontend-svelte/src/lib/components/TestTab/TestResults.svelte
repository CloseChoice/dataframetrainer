<script lang="ts">
    import type { PytestResult } from "./pytest-result";
    import {testResult} from "$lib/stores/pyodide-store"
    // import sampleReport from "./sample-report.json"
    import SingleTestResult from "./SingleTestResult.svelte";
</script>
<div class="p-2">
    {#if !$testResult}
        You need to run a test to see the result
    {:else}
        {#each $testResult.tests as test }
            <SingleTestResult test={test}/>
        {/each}
    {/if}
</div>