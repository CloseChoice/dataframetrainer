// Firefox does not support workers of type module yet

// Until that changes we can't use regular imports in vite development mode so this'll do
importScripts("https://unpkg.com/comlink/dist/umd/comlink.js");
importScripts("https://cdn.jsdelivr.net/pyodide/v0.23.3/full/pyodide.js")



// Inside your worker script
class EventEmitter {
    constructor() {
      this._eventListeners = {};
      this.index = 0
    }
  
    on(eventName, callback) {
      if (!this._eventListeners[eventName]) {
        this._eventListeners[eventName] = [];
      }
      this._eventListeners[eventName].push(callback);
    }
  
    off(eventName, callback) {
      const listeners = this._eventListeners[eventName];
      if (listeners) {
        this._eventListeners[eventName] = listeners.filter(cb => cb !== callback);
      }
    }
  
    emit(eventName, ...args) {
      const listeners = this._eventListeners[eventName];
      if (listeners) {
        listeners.forEach(callback => callback(...args));
      }
    }
}
  
class MyWorkerClass extends EventEmitter {
    dependencies = [
        'hypothesis',
        'pandas',
        'numpy',
        'pytest',
        // pytest-json
        'https://files.pythonhosted.org/packages/81/35/d07400c715bf8a88aa0c1ee9c9eb6050ca7fe5b39981f0eea773feeb0681/pytest_json_report-1.5.0-py3-none-any.whl'
    ]
    // pyodideReadyPromise = null;

    constructor() {
        super();
        this._state = 'loading';
    }
    set state(value) {
        if (this._state !== value) {
          this._state = value;
          this.emit('stateChange', value);
        }
    }
    
    get state() {
        return this._state;
    }

    async loadPyodideAndPackages(){
        const pyodide = await loadPyodide()
        pyodide.setStdout({
            batched: (batch) => this.emit('stdout', batch)
        })

        await pyodide.loadPackage("micropip");
        const micropip = await pyodide.pyimport("micropip");
    
        // Install Dependencies
        await Promise.all(this.dependencies.map(d => micropip.install(d)))
    
        const mountDir = ".";
        await pyodide.FS.mount(pyodide.FS.filesystems.MEMFS, { root: "." }, mountDir);
        await Promise.all([
            pyodide.FS.mkdir('/home/pyodide/challenges'),
            pyodide.FS.mkdir('/home/pyodide/userSolutions'),
            pyodide.FS.mkdir('/home/pyodide/tests')
        ])
        await pyodide.FS.syncfs(true, function (err) {
            console.log(err);
            // handle callback
        });
        return pyodide;
    }

    async initialize(){
        this.emit('stateChange', 'loading')
        this.pyodideReadyPromise = this.loadPyodideAndPackages()
        await this.pyodideReadyPromise
        this.emit('stateChange', 'idle')
        return true
    }

    async executeUserCode(userCode){
        this.emit('stateChange', 'running')
        const pyodide = await this.pyodideReadyPromise
        const resultUserCode = pyodide.runPython(userCode);
        pyodide.runPython("import os; print(os.listdir('/home/pyodide/'))");
        // pyodide.runPython("import os; print(os.listdir('/home/pyodide/ActuallyWorkingChallenge'))");
        console.log("executing user code: ", userCode);
        console.log("this is resultUserCode", resultUserCode);
        this.emit('stateChange', 'idle')
        return resultUserCode
    // todo: fill!
    }

    async showStuff(path) {
      const pyodide = await this.pyodideReadyPromise;
      console.log("This is the path of which we should print stuff", path);
      pyodide.runPython("import os; print(os.listdir('/home/pyodide/'))");
      pyodide.runPython(`import os; print(os.listdir('${path}'))`);
      return true
    }

    async testUserCode(userCode, data){
        this.emit('stateChange', 'testing')
        // console.log("This is data", data);
        // console.log("This is the challengeName", data.challenge_name);
        // console.log("This is the challengeTest", data.challenge_test);
        const pyodide = await this.pyodideReadyPromise
        // pyodide.FS.writeFile(userCode, '/mnt/usercode.py');
        console.log('root dir', pyodide.FS.readdir('.'));
        
        pyodide.runPython("import os; print(os.listdir('/home/pyodide/'))");
        // await pyodide.FS.mkdir('/home/pyodide/challenges');
        try {
          await pyodide.FS.mkdir(`/home/pyodide/challenges/${data.challenge_name}`);
          console.log(`created file at /home/pyodide/challenges/${data.challenge_name}`);
        } catch (error) {
          console.error(`Failed to create dir with name "/challenges/${data.challenge_name}"`)
        }
        await pyodide.FS.writeFile(`./challenges/${data.challenge_name}/submission.py`, userCode);
        await pyodide.FS.writeFile(`./challenges/${data.challenge_name}/test_${data.challenge_name}.py`, data.challenge_test);
        await pyodide.FS.writeFile(`./challenges/${data.challenge_name}/${data.challenge_name}.py`, data.challenge_class);
        await pyodide.FS.syncfs(true, function (err) {
            console.log(err);
            // handle callback
        });

        console.log('challenge dir', pyodide.FS.readdir(`./challenges/`));
        console.log(`challenge dir ${data.challenge_name}`, pyodide.FS.readdir(`./challenges/${data.challenge_name}`));

        pyodide.runPython(userCode);
        // console.log("ran usercode", userCode);
        let transform_func = pyodide.globals.get('transform');
        // console.log("THIS IS transform", transform_func);
        // todo: alert if transform is not defined and BONUS: show the defined functions
        if (!pyodide.isPyProxy(transform_func)) {
            alert("transform function is not defined! Please define this function otherwise we can't evaluate the code.");
            console.log("is pyproxy");
        }


        const literalShit = `import importlib
from importlib import reload
importlib.invalidate_caches()
import challenges
import challenges.${data.challenge_name}
import challenges.${data.challenge_name}.submission
from challenges.${data.challenge_name}.submission import transform
import challenges.${data.challenge_name}.test_${data.challenge_name}

reload(challenges)
reload(challenges.${data.challenge_name})
reload(challenges.${data.challenge_name}.submission)
reload(challenges.${data.challenge_name}.test_${data.challenge_name})

import pytest
pytest.main(['--json-report', '--json-report-file' ,'report.json', '--capture=tee-sys', 'challenges/${data.challenge_name}'])`
        pyodide.runPython(literalShit)
        // pyodide.runPython(`import pytest; pytest.main(['--json-report', '--json-report-file', 'report.json', '/home/pyodide/challenges/${data.challenge_name}/test_${data.challenge_name}.py'])`);
        // pyodide.runPython("import os; print(os.listdir('.'))");
        // let exitCode = pyodide.runPython(`test_${data.challenge_name}.py`);
        // console.log("This is the exitCode", exitCode);
        // pyodide.runPython
        let report = pyodide.FS.readFile('report.json', { encoding: "utf8" })
        console.log("This is the report", report);

        let submission = pyodide.FS.readFile(`./challenges/${data.challenge_name}/submission.py`, { encoding: "utf8" })
        console.log("This is the submission", submission);
        // pyodide.FS.syncfs(true, function (err) {
        // console.log(err);
        // // handle callback
        // });
        // console.log("Synced");
    
        this.emit('stateChange', 'idle')
        return report
    }
}


// Export functions to be used in pyodide-store

const workerInstance = new MyWorkerClass()

Comlink.expose(workerInstance)

