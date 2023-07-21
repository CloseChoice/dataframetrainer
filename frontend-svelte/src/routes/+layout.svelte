<script>
    import { setContext } from 'svelte';
    import { writable } from 'svelte/store';
    import {page} from '$app/stores'
    /** @type {import('./$types').LayoutData} */
    export let data;
    // Create a store and update it when necessary...    
    const user = writable(null);
    $: user.set(data.user);


    console.log(data);
    // ...and add it to the context for child components to access    setContext('user', user);
</script>

<nav class="w-100 position-fixed top-0 navbar navbar-expand-md navbar-dark bg-dark">
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
            <a class="nav-link" class:active={$page.url.pathname === "/login"} href="/login">Login</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" class:active={$page.url.pathname === "/register"} href="/register">Register</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" class:active={$page.url.pathname === "/logout"} href="/logout">Logout</a>
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