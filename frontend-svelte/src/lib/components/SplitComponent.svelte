<script lang="ts">
    // https://github.com/nathancahill/split/tree/master/packages/splitjs
    import Split from 'split.js'
    import { onMount } from "svelte";
    
    export let options: Split.Options;

    // if(!$$slots.first || !$$slots.second){
    //     throw new Error("Split Component needs exactly two named slots 'first' and 'second'")
    // }

    let splitFirst : HTMLElement;
    let splitSecond: HTMLElement;
    onMount(()=>{
        Split([splitFirst, splitSecond], options)
    })

</script>
<div bind:this={splitFirst}>
    <slot name="first"></slot>
</div>
<div bind:this={splitSecond}>
    <slot  name="second"></slot>
</div>