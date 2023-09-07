<script>
import {pyodideStdout} from '$lib/stores/pyodide-store'
import {pyodideStderr} from '$lib/stores/pyodide-store'
</script>

<div class="h-100 overflow-auto">
  {#if $pyodideStderr}
    <p class="text-danger">{$pyodideStderr.message}</p>
  {:else}
    {#each $pyodideStdout as line}
      <div>{line}</div>
    {/each}

  {/if}
    
</div>
