import { writable } from "svelte/store";

export async function load_pyodide() {
        let pyodide_f;

        pyodide_f = await loadPyodide();

        await pyodide_f.loadPackage("micropip");
        const micropip = pyodide_f.pyimport("micropip");
        await micropip.install('hypothesis');
        await micropip.install('pandas');
        await micropip.install('numpy');
        await micropip.install('pytest');

        let mountDir = ".";
        await pyodide_f.FS.mount(pyodide_f.FS.filesystems.IDBFS, { root: "." }, mountDir);
        await pyodide_f.FS.mkdir('/home/pyodide/challenges');
        await pyodide_f.FS.mkdir('/home/pyodide/userSolutions');
        await pyodide_f.FS.mkdir('/home/pyodide/tests');
        await pyodide_f.FS.syncfs(true, function (err) {
  console.log(err);
  // handle callback
  });
return pyodide_f;
}

export const pyodide = writable(null);

load_pyodide()
  .then((pyodide_f) => {
    pyodide.set(pyodide_f);
  })
  .catch((err) => {
    console.log("Error loading pyodide", err);
  });