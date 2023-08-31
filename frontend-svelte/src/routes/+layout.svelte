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


    console.log(data);
    // ...and add it to the context for child components to access    setContext('user', user);

    onMount(initPyodideStore)
    import CookieBanner from '$lib/components/CookieBanner.svelte';

</script>


<CookieBanner/>


<nav style="z-index:1030" class="navbar-expand navbar-dark bg-dark shadow border-bottom w-100 position-fixed top-0 navbar navbar-expand-md">
    <div class="container-fluid">
      <a class="d-none d-md-block navbar-brand" href="#">Dataframetrainer</a>
     
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" class:active={$page.url.pathname === "/"} href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" class:active={$page.url.pathname === "/browse_challenges"} href="/browse_challenges">Browse</a>
        </li>
        <li>
          <!-- <button data-test="new-challenge-button" on:click={handleNewChallenge} type="button" class="btn btn-light">Random Challenge</button> -->
          <a data-test="new-challenge-button" class="nav-link" href="/random_challenge">Random Challenge</a>
        </li>
      </ul>
      
      <div class="text-light">
      <span data-test="username-display" class="navbar-text me-3">
        {#if $page.data.session}
          {$page.data.session.user?.name ?? "User"}
        {/if}
      </span>
      {#if $page.data.session}
      <form class="d-inline" method="POST" action="/authentication?/logout">
        <button class="btn btn-primary">Sign Out</button>
      </form>
      {:else}
      <a href="/authentication" class="btn btn-primary" role="button">Sign In</a>
      {/if}
    </div>

      
    </div>
    
    
  </nav>


<slot></slot>


