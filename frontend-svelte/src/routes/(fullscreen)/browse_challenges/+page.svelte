<script>
    // import { slide } from "svelte/transition";
    export let data;
</script>

<div class="container mt-5" data-sveltekit-preload-data="off">
    {#each data.challenges as challenge}
    <a class="text-decoration-none" href="/new_challenge/{challenge.id}">
        <div data-test="challenge-card" data-challenge-status="{challenge.status}" data-challenge-id="{challenge.id}" class="card mb-3">
            <div class="card-body ">
                <h5 class="me-2 d-inline-block card-title">{challenge.id}</h5>
                {#if challenge.status == 0}
                    <span class="badge rounded-pill bg-dark">visited</span>
                {:else if challenge.status == 1}
                    <span class="badge rounded-pill bg-danger">tried</span>
                {:else if challenge.status == 2}
                    <span class="badge rounded-pill bg-success">succeeded</span>
                {/if}
            </div>
          </div>
    </a>
    {/each}
</div>