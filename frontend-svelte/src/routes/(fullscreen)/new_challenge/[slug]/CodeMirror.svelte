<script lang="ts">
    import {EditorState} from "@codemirror/state"
    import {EditorView, keymap} from "@codemirror/view"
    import {defaultKeymap} from "@codemirror/commands"
    import { onMount } from 'svelte';
    import { oneDark } from "@codemirror/theme-one-dark"
    import { history } from "@codemirror/commands";
    import { highlightSpecialChars } from "@codemirror/view";
    import { drawSelection } from "@codemirror/view";
    import { indentOnInput } from "@codemirror/language";
    import { autocompletion, closeBrackets } from '@codemirror/autocomplete';
    import { highlightSelectionMatches } from "@codemirror/search";
    import { python } from "@codemirror/lang-python";

    let codeMirrorRef: HTMLElement;

    export let value = ""

    const extensions = [
        keymap.of(defaultKeymap),
        // Listen to changes of the code editor and update value
        EditorView.updateListener.of(function(e) {
            value = e.state.doc.toString();
        }),
        oneDark,
        history(),
        highlightSpecialChars(),
      drawSelection(),
      EditorState.allowMultipleSelections.of(true),
      indentOnInput(),
      closeBrackets(),
      autocompletion(),
      highlightSelectionMatches(),
      python()
    ] 
    
    let editorState: EditorState;
    let editorView: EditorView;
    onMount(()=>{
        editorState = EditorState.create({
            doc: value,
            extensions: extensions
        })

        editorView = new EditorView({
            state: editorState,
            parent: codeMirrorRef
        })
    })    
</script>


<div data-test="code-mirror-root" class="CodeMirror" bind:this={codeMirrorRef}></div>

<style>
    .CodeMirror {
        height: 100%;
        max-height: 100%;
    }
    :global(.cm-editor){
        height: 100%;
    }
</style>