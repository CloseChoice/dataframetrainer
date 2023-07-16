<script>
    import { slide } from "svelte/transition";

    export let data;
</script>

<ul class="list">
    {#each data.challenges as challenge}
        <div transition:slide>
        <li class="list-item">
            <a href={`/new_challenge/${challenge}`}>{challenge}</a>
        </li>
        </div>
    {/each}
</ul>
<style>
    .list {
      list-style-type: none; /* Sets the bullet style */
      padding-left: 1.5em; /* Adds left indentation */
    }
    
    .list-item {
      border:1px solid #000;
      width: 50%;
    }
</style>
  