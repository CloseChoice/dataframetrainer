<div class="wrapper" style="height: {height}; width: {width};">
  <div name="editor" id="CMeditor" bind:this='{CodeMirrorEditor}' >
  </div>
</div>

<style>
  #CMeditor {
    height: 100%;
    width: 100%;
  }
  .wrapper {
    position: absolute;
  }

  :global(.cm-wrap) {
    height: 100%;
  }

  :global(.cm-scroller) { 
    overflow: auto; 
  }
</style>

<script>
  import { onMount } from 'svelte';
  import { createEventDispatcher } from 'svelte';
  import { markdown } from "@codemirror/lang-markdown";
  import { python } from "@codemirror/lang-python";
  import { oneDark } from "@codemirror/theme-one-dark";
  import { highlightSpecialChars, drawSelection, highlightActiveLine, EditorView } from '@codemirror/view';
  import { EditorState } from '@codemirror/state';
  import { indentOnInput } from '@codemirror/language';
  import { history } from '@codemirror/commands';
  import { highlightSelectionMatches } from '@codemirror/search';
  import { autocompletion, closeBrackets } from '@codemirror/autocomplete';
  import { javascript } from '@codemirror/lang-javascript';

  const dispatch = createEventDispatcher();
  
  export let height;
  export let width;
  export let config;
  export let initFinished = false;
  export let defaultCode;

  let CodeMirrorEditor;
  let edState;
  let edView;
  let editorFunctions;
  let currentCursor;

  function fire(name, data) {
    dispatch(name, {
      data: data
    });
  }

  function setValue(text) {
    // 
    // Since we are setting a whole new document, create new editor 
    // states and views.
    // 
    console.log('Setting value: ' + text);
    if(initFinished) {
      console.log("init finished");
      CreateEditorState(text);
    }
  }

  function CreateEditorState(text) {
    // 
    // Clear out the div element in case a previous editor was
    // created.
    //
    CodeMirrorEditor.innerHTML = '';

    //
    // Setup the extensions array.
    //
    const exts = [
      highlightSpecialChars(),
      history(),
      drawSelection(),
      EditorState.allowMultipleSelections.of(true),
      indentOnInput(),
      // Prec.fallback(defaultHighlightStyle),
      // bracketMatching(),
      closeBrackets(),
      autocompletion(),
      // rectangularSelection(),
      highlightSelectionMatches(),
      // keymap.of([
      //     ...closeBracketsKeymap,
      //     ...defaultKeymap,
      //     ...searchKeymap,
      //     ...historyKeymap,
      //     ...completionKeymap,
      //     ...lintKeymap
      // ]),
      oneDark,
      EditorView.updateListener.of(update => {
        if(update.docChanged) {
          fire('textChange', {
            value: getValue(),
            cursor: getCursor(),
            history: {}
          })
        }
      })
    ];

    // 
    // Add extensions based on the configuration.
    // 
    // if(config.lineNumbers) {
    //   exts.push(lineNumbers());
    // }

    switch(config.language) {
      case 'markdown':
        exts.push(markdown());
        break;
      case 'javascript':
        exts.push(javascript());
        break;
      case 'python':
        exts.push(python());
        break;
      default: 
        exts.push(markdown());
        break;
    }

    if(config.lineWrapping) {
      exts.push(EditorView.lineWrapping);
    }

    if(config.lineHighlight) {
      exts.push(highlightActiveLine());
    }
    
    // 
    // Create the editor state.
    //
    console.log("Inner stuff: " + text);
    edState = EditorState.create({
      doc: text,
      extensions: exts
    });

    // 
    // Create the editor View.
    // 
    edView = new EditorView({
      state: edState,
      parent: CodeMirrorEditor
    });
  }

  onMount(() => {
    // 
    // Create the editor.
    // 
    console.log("this is the defualt code", defaultCode);
    // todo: where does the suffx ';' come from? Remove it here till we find out
    CreateEditorState(defaultCode.replace(/\;$/, ""));

    //
    // Create the editor functions object.
    //
    editorFunctions = {
      getSelection: getSelection,
      getValue: getValue,
      replaceSelection: replaceSelection,
      somethingSelected: somethingSelected,
      setCursor: setCursor,
      getCursor: getCursor,
      setValue: setValue,
      getLine: getLine,
      focus: focus
    };
    
    //
    // Debugging: add to the window for testing.
    //
    if(typeof window.edFunctions === 'undefined') window.edFunctions = [];
    window.edFunctions.push(editorFunctions);

    //
    // Give the parent the functions for interacting with the editor.
    //
    fire('editorChange', editorFunctions);

    // 
    // Make sure the editor is focused.
    //
    focus();

    //
    // Return a function to run to clean up after mounting.
    //
    return () => {
      // this function runs when the
      // component is destroyed
    };
  });

  function getLine(pos) {
    if(typeof edView !== 'undefined') {
      var result = "";
      return(result);
    }
    return('');
  }

  function getSelection() {
    if(typeof edView !== 'undefined') {
      return edView.state.sliceDoc(
        edView.state.selection.main.from,
        edView.state.selection.main.to);
    }
  }

  function replaceSelection(newText) {
    if(typeof edView !== 'undefined') {
      let transaction = edView.state.update({changes: [{from: edView.state.selection.main.from, to: edView.state.selection.main.to}, {from: 0, insert: newText}]});
      edView.dispatch(transaction);
    }
  }

  function somethingSelected() {
    if(typeof edView !== 'undefined') {
      return edView.state.selection.ranges.some(r => !r.empty);
    }
  }

  function setCursor(pos) {
    if(typeof edView !== 'undefined') {
      currentCursor = pos;
      edView.dispatch({selection: {anchor: currentCursor}})
    }
  }

  function getCursor() {
    if(typeof edView !== 'undefined') {
      currentCursor = edView.state.selection.main.head;
      return(currentCursor);
    } else {
      return(0);
    }
  }

  export function getValue() {
    if(typeof edView !== 'undefined') {
      return edView.state.doc.toString();
    }
  }

  function focus() {
    if(typeof edView !== 'undefined') {
      edView.focus();
    }
  }
</script>