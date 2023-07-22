<style>
 pre {
    color: purple;
    font-family: 'Comic Sans MS', cursive;
    font-size: 2em;
  }

  .codeOutput {
    border: solid 1px red;
  }
</style>
<script>
export let resultUserCode;
</script>

<div class="codeOutput">
    {#if resultUserCode !== undefined}
    <pre>
        {resultUserCode}
    </pre>
    {/if}
</div>
