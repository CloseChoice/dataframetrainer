<script lang="ts">
    import { pyodideWorkerPromise } from "$lib/stores/pyodide-store";
    import type { ChallengeExample } from "$lib/worker/pyododie-worker.module";

    export let description: string;
    export let staticExample: ChallengeExample;

    let generatedExample: ChallengeExample;
    async function handleGenerateExample(){
        const worker = await pyodideWorkerPromise;
        generatedExample = await worker.generateExample()
    }
</script>

<div style="background:red">
    {@html description}
</div>
<h3>Static Example</h3>
{staticExample}
<h3>Generate Example</h3>
<button on:click={handleGenerateExample}>GENERATE EXAMPLE</button>
{#if generatedExample}
    <h3>Params</h3>
    {#each Object.entries(generatedExample.params) as [param_name, param_val]}
        <h5>{param_name}</h5>
        {@html param_val}
    {/each}
    <h3>Result</h3>
    {@html generatedExample.result}
{/if}