<script>
    import { onMount } from "svelte";

    // This is initially true to prevent flickering because localStorage is only available after mount
    let isUserInformed = true

    onMount(()=>{
        let cookie_inform = localStorage.getItem('cookie_inform')

        if (cookie_inform){
            isUserInformed = Boolean(JSON.parse(cookie_inform))
        }else{
            isUserInformed = false
        }
    })

    function dismiss(){
        localStorage.setItem('cookie_inform', JSON.stringify(true))
        isUserInformed = true
    }
</script>

{#if !isUserInformed}
    <div style="z-index:1070" class="w-100 position-absolute bottom-0 pb-4  ">
        <div class="container" style="max-width:800px">
            <div class="card">
                <div class="card-header">
                    We use Cookies 🍪
                    <button on:click={dismiss} class="btn btn-primary btn-sm" type="button">Dismiss</button>
                </div>
                <div class="card-body">
                    We use cookies for authentication. If you don't like that feel free to leave 🚪.
                </div>
            </div>
        </div>
    </div>
{/if}