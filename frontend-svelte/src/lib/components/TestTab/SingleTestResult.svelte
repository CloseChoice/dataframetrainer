<script lang="ts">
    import type {PyTest} from './pytest-result'
    export let test: PyTest;

    $: hasPassed = test.outcome.includes('passed')
    $: color = hasPassed ? 'success' : 'danger';
</script>

<div class="card mb-3 border-1 border-{color}" id="testResultContainer">
    <div class="card-header border-0  bg-{color} bg-opacity-25">
        <span data-test="testResultIcon">{hasPassed? "✅" : "❌"}</span>
        <span>{test.nodeid}</span>
    </div>
    {#if !hasPassed}
    <div class="card-body border-top border-{color}">
        <h3>Error Message</h3>
        {test.call?.crash?.message}
        {#if test.call?.stdout}
        <h3>stdout</h3>
            {#each test.call.stdout.split('\n') as line}
                <div>{line}</div>
            {/each}
        {/if}
        </div>
        
    {/if}
</div>