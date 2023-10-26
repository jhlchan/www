---
title: Pyscript - Demo 6
header-includes: |
    <style>
       body { min-width: 90% !important; }
    </style>
include-after: |
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css"/>
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo06.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo06.html -->
---

# Pyscript - Running Python

## Input{#def}
<textarea id="code" cols="80" rows="10" style="border-style: groove;">
import math

def primes_to(n):
    primes = []
    primes.append(2) # the only even prime
    for num in range(3,n + 1,2): # all odd primes <= n, from 3, step 2
        if all (num%j != 0 for j in range(3,int(math.sqrt(num))+1,2)):
            primes.append(num) # pick up the odd prime

    return primes
</textarea>

## Command{#cmd}
<input type="text" id="command" placeholder="use arrow keys to navigate history" autocapitalize="off" class="py-input">\
<button id="runButton" class="py-button" py-click="runit()" >Run</button>

## Output{#out}
<py-terminal id="output">
</py-terminal>

## Debugger{#debug}
Type your Python code (hover mouse/pointer to bottom right-end for Green arrow to run code):
<py-repl id="board">
</py-repl>

<!-- Javascript -->
```{=html}
<script>
/* to play with JS/Python round trip */

var dummy = {}
dummy.one = 1
dummy.two = 2

/**
* check if `x` is `-0`, using only operators.
* to ensure correctness in ALL circumstances, it doesn't use `Object.is`, because it's mutable.
* this means this fn is 100% [pure](https://en.wikipedia.org/wiki/Pure_function).
* @param {*} x
*/
const isNegZero = x => x === 0 && 1 / x == -Infinity;

/**
* check if `x` matches the description of the `Uint32` namepath.
* this fn is pure, by using only operators (and a fn call).
* @param {*} x
*/
const isUint32 = x => typeof x == 'number' && x == x >>> 0 && !isNegZero(x);

/**
* String Queue (FIFO) to manage a history or log.
* @param {Uint32} [maxSize=2**16] maximum chars to keep in memory.
*/
const Hist = class {
  // a 16bit address-space seems like a sensible default
  constructor(maxSize = 1 << 0x10) {
     // runtime type safety
     if ( !isUint32(maxSize) )
        throw new RangeError('expected `maxSize` to be `Uint32`, but got ' + maxSize);
     // just-in-case
     if (maxSize < 2)
        console.warn('Max History size set to 0 or 1. This seems like an accident');

     /**
      * max CUs to store, until at least 1 string is cleared from the queue.
      * @type {Uint32}
      */
     this._maxSize = maxSize;

     /**
      * total size in memory.
      * measured in **code-units** (16b or 2B), not bytes (8b or 1B).
      * @type {Uint32}
      */
     this._size = 0;

     /**
      * pointer to currently selected entry.
      * @type {Uint32}
      */
     this._index = 0;

     /**@type {string[]}*/
     this._entries = [];
  }

  /** returns entry at current `index`, defaults to empty `string` */
  get() { return this._entries[this._index] || ''; }

  // both are unused, but may be handy in the future
  /** get latest entry, defaults to empty `string` */
  newest() { return this._entries[this._entries.length - 1] || ''; }
  /** get earliest entry, defaults to empty `string` */
  oldest() { return this._entries[0] || ''; }

  /**
   * append/push, with auto-flush
   * @param {string} s
   */
  set(s) {
     // enqueue, then set index to newest entry
     this._index = this._entries.push(s);
     // ensure it's up-to-date, to avoid memory leaks
     this._size += s.length;

     // flush old entries
     while (this._size > this._maxSize) {
        // dequeue, then update size
        this._size -= /**@type {string}*/(this._entries.shift()).length;
        this._index--; // index correction
     }
  }

  /**
   * increment `index` by 1, clamped to `entries.length`, then return its value.
   * @return {Uint32}
   */
  incIdx() {
     return this._index = Math.min(this._index + 1, this._entries.length);
  }

  /**
   * decrement `index` by 1, clamped to 0 (keeps it unsigned), then return its value.
   * @return {Uint32}
   */
  decIdx() {
     return this._index = Math.max(this._index - 1, 0);
  }

  // also unused, but good to have available
  /**
   * set `maxSize` to a new value
   * @param {Uint32} n
  */
  setMaxSize(n) {
     if ( !isUint32(n) )
        throw new RangeError('expected `n` to be `Uint32`, but got ' + n);
     this._maxSize = n;
  }
  // maybe we should add a button to clear the history?
};

const cmds = new Hist(1 << 20); // is this size "balanced"?

const cmdBox = /**@type {HTMLInputElement}*/(document.getElementById('command'));

cmdBox.addEventListener('keydown', ({ key }) => {
  switch (key) {
     // Moves up and down in command history
     case 'ArrowDown': cmds.incIdx(); break;
     case 'ArrowUp': cmds.decIdx(); break;
     // call `runCmd` when user presses any "Enter" or "Return" keys
     // case 'Enter': return runCmd();
     default: return;
  }
  // external fall-through, only executed if `return` isn't touched
  cmdBox.value = cmds.get();
}, false);

</script>
```

<!-- pyscript -->
```{=html}
<py-script>
# import whole js for debug
import js
from js import document

# import whole pyodide for debug
import pyodide
from pyodide.code import eval_code
from pyodide.ffi import create_proxy, to_js

def runit():
    # combine code and command into a program
    pycode = Element('code').value + '\n' + Element('command').value
    # Element('output').element.innerHTML = ''
    
    # just use the Python built-in eval()
    # eval(expression, globals, locals)
    # no good
    # try:
    #     result = eval(pycode)
    # except Exception as err: js.console.log(err)

    # use pyodide directly
    # see John Hanley example 5
    # pyodide.runPython(pycode)
    # This doesn't work, but the next works.
    # see https://pyodide.org/en/stable/usage/api/python-api/code.html#pyodide.code.eval_code
    result = eval_code(pycode)
    print(result)  # This prints to both py-terminal and console.log by stdio.ts, a plugin.
    # Element('output').write(result, append=True), this is HTML write, not py-terminal print

</py-script>
```
---

<!--

Python Debugger (py-repl):
type(js.dummy)          : <class 'pyodide.ffi.JsProxy'>
py_dummy = js.dummy.to_py()
type(py_dummy)          : <class 'dict'>
py_dummy.one            : no attribute one
py_dummy['one']         : 1
py_dummy['two']         : 2
py_dummy['three']       : KeyError: 'three'
py_dummy['three'] = 3
py_dummy['three']       : 3
dummy = to_js(py_dummy)        (no use)
js.dummy = to_js(py_dummy)     (no use)
js.dummy = js.Object.fromEntries(to_js(py_dummy))   *, using hint: from js import Object

Browser console (in FireFox):
typeof(dummy)     = "object" 
dummy.one         = 1
dummy.two         = 2
dummy.three       : undefined
(with python assignment)
dummy.three       : undefined
(after dummy = to_js(py_dummy))
dummy.three       : undefined
dummy.get('three')  TypeError: dummy.get is not a function
with *
dummy             : Object { one: 1, two: 2, three: 3 }
dummy.three       : 3       (finally!)

For demo05, at the very beginning, from Browser console:

>> Sk
Object { build: {…}, global: Window, exportSymbol: exportSymbol(a, b), isArrayLike: isArrayLike(a), js_beautify: js_beautify(a), asserts: {…}, bool_check: bool_check(a, b), python2: {…}, python3: {…}, configure: configure(a), … }

The ... indicates more.

Sk.build
Object { githash: "4b86a6f1f3cf684f7e5ca17042fc5d6bd302df60", date: "2020-09-22T14:43:51.634Z" }

Since Sk is a deep and complex Object, this kind of round-trip for just updating two keys is not worthwhile.
Better call a JS function to update the keys, as shown in demo05.
-->
<!-- pandoc -s demo06.md -o demo06.html -->