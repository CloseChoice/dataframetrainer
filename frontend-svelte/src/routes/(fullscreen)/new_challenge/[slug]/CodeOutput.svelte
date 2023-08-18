<script>
import {pyodideStdout} from '$lib/stores/pyodide-store'
</script>

<div class="h-100 overflow-y-auto">
    {#each $pyodideStdout as line}
      <div>{line}</div>
    {/each}
</div>
