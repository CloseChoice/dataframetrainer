<script>
    import { setContext } from 'svelte';
    import { writable } from 'svelte/store';
    import {page} from '$app/stores'
    import { signIn, signOut } from "@auth/sveltekit/client"
</script>

<nav style="z-index:1030" class="w-100 position-fixed zindex-fixed top-0 navbar navbar-expand-md navbar-dark bg-dark">
    <div class="container-fluid">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="">
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
      <!-- <a class="navbar-brand" href="#">Dataframetrainer</a> -->
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
    
    
  </nav>

<!-- The main body is 100 viewport heights to allow for easy full screen pages -->
<!-- If you want to have a full screen page (minus the header) set the height of the outermost div to 100%-->
<main class="vh-100 max-vw-100" role="main">
  <slot/>
</main>

<style>
	main{
		padding-top: 3.5rem;
	}
</style>