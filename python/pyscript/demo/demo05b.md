---
title: Pyscript - Demo 5B
header-includes: |
    <style>
       body { min-width: 90% !important; }
    </style>
include-before: |
    <link rel="stylesheet" href="js-turtle/lib/turtle.css" />
    <script defer src="js-turtle/lib/library.js"></script>
include-after: |
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css"/>
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo05b.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo05b.html -->
---

# Pyscript - Turtle Graphics by JS-Turtle

## Definitions{#def}
<textarea id="definitions" class="py-box" rows="30">
// Define helper functions here.
// For example:

function square(side) {
  // repeat NOT implemented
  forward(side);
  right(90);
  forward(side);
  right(90);
  forward(side);
  right(90);
  forward(side);
  right(90);
}

function demo() {
   // these are implemented
   // showGrid(50); // 30 = narrow, 50 = wide, just for the grid
   setSpeed(100); // 100 = fast, 200 = slow
   width(2); // 1 = thin 
   // hideTurtle NOT implemented
   colour(0,0,255,1);
   for (s = 200; s > 0; s -= 10) {
      square(s);
      right(36);
   }
}

</textarea>

## Canvas{#can}
[]{#coords }
[Coordinates has been copied to clipboard]{#message .message-hide }

<canvas id="turtlecanvas" width="700" height="700"></canvas>
<canvas id="imagecanvas" width="700" height="700" style="display:none"></canvas>


## Command{#cmd}
<input type="text" id="command" placeholder="use arrow keys to navigate history" autocapitalize="off" class="py-input">\
<button id="runButton" class="py-button">Run</button>
<button id="resetButton" class="py-button">Reset</button>


Type your Python code (hover mouse/pointer to bottom right-end for Green arrow to run code):
<py-repl></py-repl>

<!--
JavaScript Turtle Graphics
file:///Users/josephchan/jc/www/python/pyscript/js-turtle/turtle.html
This one uses engine: js-turtle/lib/library.js
Expects helper functions in: js-turtle/functions.js (which is empty)
Executes turtle commands in: js-turtle/turtle.js    (list of commands)
Modification:
* put commands in turtle.js in Definitions.
* borrow javascript from bjpop to execute commands on-the-fly.

js-turtle Documentation
https://hanumanum.github.io/js-turtle/index_en.html
js-turtle is an environment to learn/teach programming with JavaScript language. Idea initialy comes from Seymour Papert.
Javascript version of turtle graphycs initialy started by bjpop, than forked and developed by hanumanum.
Still no direct URL to the main engine script: js-turtle/lib/library.js, only from unzip of master.
https://github.com/hanumanum/js-turtle/

js-turtle/examples/
bounce.js          ERROR: wrap is not defined
clock.js           ERROR: hideTurtle is not defined
graphs             has turtle.html  turtle.js
fl.js              static flower
heart.js           big heart shape with a color rim
randstripe.js      ERROR: hideTurtle, redrawOnMove is not defined
sierpinski.js      ERROR: hideTurtle, redrawOnMove is not defined
spiral.js          ERROR: hideTurtle, redrawOnMove is not defined


TODO: cannot import to Pyscript yet.
div = Element('turtlecanvas')
div.element.innerHTML

A canvas element.
-->

<!-- pyscript -->
```{=html}
<py-script>
import js
from pyodide.ffi import create_proxy, to_js

# turtle = js.turtle    # from turtle/turtle.js

</py-script>
```

<!-- javascript -->
```{=html}
<script>
/**
 * main program/script, mostly UI code.
 *
 * this fn is used to encapsulate private stuff that the user shouldn't access
 */
const _main = () => {
   const doc = document;

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

   const cmdBox = /**@type {HTMLInputElement}*/(doc.getElementById('command'));

   cmdBox.addEventListener('keydown', ({ key }) => {
      switch (key) {
         // Moves up and down in command history
         case 'ArrowDown': cmds.incIdx(); break;
         case 'ArrowUp': cmds.decIdx(); break;
         // call `runCmd` when user presses any "Enter" or "Return" keys
         case 'Enter': return runCmd();
         default: return;
      }
      // external fall-through, only executed if `return` isn't touched
      cmdBox.value = cmds.get();
   }, false);

   const def = /**@type {HTMLTextAreaElement}*/(doc.getElementById('definitions'));

   /** Executes program in the command box */
   const runCmd = () => {
      const cmdText = cmdBox.value;
      cmds.set(cmdText);

      const definitionsText = def.value;
      // https://stackoverflow.com/questions/19357978/indirect-eval-call-in-strict-mode
      // "JS never ceases to surprise me" @Rudxain
      try {
         // execute any code in the definitions box
         (0, eval)(definitionsText);
         // execute the code in the command box
         (0, eval)(cmdText);
      } catch (e) {
         alert('Exception thrown:\n' + e);
         throw e;
      } finally {
         // clear the command box
         cmdBox.value = '';
      }
   };

   /** JC: add reset by window.clear in lib/library.js */
   const reset = () => {
       const program = 'clear()'
      try {
         // execute the program
         (0, eval)(program)
      } catch (e) {
         alert('Exception thrown:\n' + e)
         throw e;
      } finally {
         // clear the command box
         cmdBox.value = '';
      }
   }
   /** JC: due to reset() has no window.reset, this JS reset cannot stop the turtle. */

   /**
    * Similar to JQuery
    * @param {string} id HTML element ID
    * @param {(this: HTMLElement, ev: MouseEvent) => unknown} cb callback
    */
   const listenClickById = (id, cb) => doc.getElementById(id).addEventListener('click', cb);
   // call `runCmd` when user presses "Run"
   listenClickById('runButton', runCmd);
   listenClickById('resetButton', reset);

   // reset(); // JC: initial library setup will reset anyway
};

_main();
</script>
```

---

<!-- pandoc -s demo05b.md -o demo05b.html -->