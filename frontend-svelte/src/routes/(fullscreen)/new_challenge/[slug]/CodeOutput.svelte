<script>
import {pyodideStdout} from '$lib/stores/pyodide-store'
</script>

<div class="max-height-100">
    {#each $pyodideStdout as line}
      <div>{line}</div>
    {/each}
</div>
