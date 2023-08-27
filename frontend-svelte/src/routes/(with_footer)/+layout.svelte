<script>
    import Footer from "$lib/components/Footer.svelte";

</script>
  <!-- The main body is 100 viewport heights to allow for easy full screen pages -->
  <!-- If you want to have a full screen page (minus the header) set the height of the outermost div to 100%-->
<main style="padding-bottom:12rem; position:relative; padding-top:3.5rem; min-height:100vh">

    <slot/>
 
    <Footer/>   
</main>
