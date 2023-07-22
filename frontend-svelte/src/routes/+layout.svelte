<script>
    import { setContext } from 'svelte';
    import { writable } from 'svelte/store';
    import {page} from '$app/stores'
    import { signIn, signOut } from "@auth/sveltekit/client"
</script>


<nav class="navbar navbar-expand-md navbar-dark text-light bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Dataframetrainer</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" class:active={$page.url.pathname === "/"} href="/">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" class:active={$page.url.pathname === "/browse_challenges"} href="/browse_challenges">Browse</a>
          </li>
        </ul>
      </div>
    </div>
    <div class="container-fluid justify-content-end">
      <span class="navbar-text me-3">
        {#if $page.data.session}
          {$page.data.session.user?.name ?? "User"}
        {/if}
      </span>
      {#if $page.data.session}
      <button class="btn btn-primary" on:click={()=> signOut()}>Sign Out</button>
      {:else}
      <button class="btn btn-primary" on:click={()=> signIn()}>Sign In</button>
      {/if}
    </div>
  </nav>

<slot />