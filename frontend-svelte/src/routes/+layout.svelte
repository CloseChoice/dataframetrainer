<script>
    import { onMount, setContext } from 'svelte';
    import { writable } from 'svelte/store';
    import {page} from '$app/stores'

    import '@fortawesome/fontawesome-free/js/all'
    import '@fortawesome/fontawesome-free/css/all.css'

    import {initPyodideStore} from '$lib/stores/pyodide-store'
    /** @type {import('./$types').LayoutData} */
    export let data;
    // Create a store and update it when necessary...    
    const user = writable(null);
    // $: user.set(data.user);


    console.log(data);
    // ...and add it to the context for child components to access    setContext('user', user);

    onMount(initPyodideStore)
    import { signIn, signOut } from "@auth/sveltekit/client"
    import CookieBanner from '$lib/components/CookieBanner.svelte';
</script>


<CookieBanner/>


<nav style="z-index:1030" class="bg-dark shadow border-bottom w-100 position-fixed zindex-fixed top-0 navbar navbar-expand-md">
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


<slot></slot>


