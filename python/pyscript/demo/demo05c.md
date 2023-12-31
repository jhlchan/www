---
title: Pyscript - Demo 5C
header-includes: |
    <style>
       body { min-width: 90% !important; }
    </style>
include-before: |
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js" type="text/javascript"></script>
    <script src="https://skulpt.org/js/skulpt.min.js" type="text/javascript"></script>
    <script src="https://skulpt.org/js/skulpt-stdlib.js" type="text/javascript"></script>
include-after: |
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css"/>
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo05c.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo05c.html -->
---

# Pyscript - Turtle Graphics by Skulpt

## Definitions{#def}
<textarea id="code" cols="80" rows="10" style="border-style: groove;">
print('Rainbow Benzene')
print('Beautiful!')

import turtle

turtle.Screen().bgcolor('black')

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

def demo():
   t = turtle.Turtle()
   for x in range(360):
       t.pencolor(colors[x%6])
       t.width(x//100 + 1)
       t.forward(x)
       t.left(59)
</textarea>

## Command{#cmd}
<input type="text" id="command" placeholder="use arrow keys to navigate history" autocapitalize="off" class="py-input">\
<button id="runButton" class="py-button" onclick="runit()">Run</button>
<button id="stopButton" class="py-button" onclick="stopit()">Stop</button>

## Output{#out}
```{#output .py-terminal }
```

__Turtle Graphics__

:::{#canvas}
:::


Type your Python code (hover mouse/pointer to bottom right-end for Green arrow to run code):
<py-repl></py-repl>

<!-- can Pyscript turn this into Python code? Not yet! -->
```{=html}
<script type="text/javascript">
// output functions are configurable.  This one just appends some text to a pre element.
function outf(text) {
    var pre = document.getElementById("output");
    pre.innerHTML += text;
}
function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

// set up Sk
Sk.pre = "output";
(Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'canvas';
// This gives PyScript: Sk.TurtleGraphics.target = canvas (before any Run)
// Sk.importMain("stdin", false, true); // initialize Skulpt, no need?
// configuration points to JS functions
var config = {"output":outf, "read":builtinRead};
Sk.configure(config); // this is according to Using Skulpt with HTML
// Sk.configure({}); // this will have output to js console, but Turtle moves.
// Sk.configure({"output":outf}); // this will have output by outf, and Turtle moves!

// Here's everything you need to run a python program in skulpt
// grab the code from your textarea
// get a reference to your pre element for output
// configure the output function
// call Sk.importMainWithBody()
function runit() {
   var prog = document.getElementById("code").value + '\n' +
              document.getElementById("command").value;
   var pre = document.getElementById("output");
   pre.innerHTML = '';
   // configuration points to JS functions
   // Sk.configure({"output":outf, "read":builtinRead});
   // Sk.pre = "output";
   // (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'canvas';

   var promise = Sk.misceval.asyncToPromise(function() {
       return Sk.importMainWithBody("stdin", false, prog, true); // "<stdin>" can be "stdin", just a name
   });
   promise.then(function(mod) {
       console.log('success');
   },
       function(err) {
       console.log(err.toString());
   });
}

// Stopping the turtle
function stopit() {
    Sk.TurtleGraphics.stop()      // JC: next run will start with a reset screen
    // Sk.TurtleGraphics.reset()  // JC: this will remove the Turtle screen
}
</script>
```


<!--
Simple Skulpt
file:///Users/josephchan/jc/www/python/pyscript/skulpt/site/simpleskulpt.html
Avoid ids generated by pandoc for headings, masking the important ids for the script.
Type command: demo()   to run demo() in Definitions.

Skulpt
https://skulpt.org/
Python. Client Side.
Skulpt is an entirely in-browser implementation of Python.

Direct URL to main engine scripts:
https://skulpt.org/js/skulpt.min.js      (main engine)
https://skulpt.org/js/skulpt-stdlib.js   (a virtual file system)

Hopeful: sk = js.Sk  works!

div = Element('output')
div.element.innerHTML

Rainbow Benzene Beautiful! 

div = Element('canvas')
div.element.innerHTML

<canvas width="400" height="400" style="position: relative; display: block; margin-top: 0px; z-index: 1;"></canvas><canvas width="400" height="400" style="position: relative; display: block; margin-top: -400px; z-index: 3;"></canvas><canvas width="400" height="400" style="position: relative; display: block; margin-top: -400px; z-index: 2;"></canvas>

A canvas element.
-->

<!-- pyscript -->
<!--
Online JavaScript to Python Converter
https://www.javainuse.com/js2py
-->
```{=html}
<py-script>
import js
from pyodide.ffi import create_proxy, to_js
from js import document
from js import Sk  # get Skulpt

# how much of Sk is visible in Python?

</py-script>
```
<!--
Browser console:
>> Sk
Object { build: {…}, global: Window, exportSymbol: exportSymbol(a, b), isArrayLike: isArrayLike(a), js_beautify: js_beautify(a), asserts: {…}, bool_check: bool_check(a, b), python2: {…}, python3: {…}, configure: configure(a), … }
with a tree.
Sk.TurtleGraphics 
Object { target: "canvas", width: 400, height: 400, worldWidth: 0, worldHeight: 0, animate: true, bufferSize: 0, allowUndo: true, assets: {}, module: {…}, … }
with a tree.

Python console:
Sk
[object Object]
Sk.TurtleGraphics      (only after RUN, not before RUN)
[object Object]
Sk.TurtleGraphics.raw
Sk.TurtleGraphics.raw.Turtle   function Turtle(e) ...


AttributeError: TurtleGraphics
Problem with Sk.configure. Python curly brackets have different meanings? Trying to_js

pyodide.ffi.JsException: TypeError: Sk.__future__ is not an object or null

Sk.__dir__()

['OpMap', 'ParseTables', 'Parser', 'SYMTAB_CONSTS', '__bool__', '__class__', '__defineGetter__', '__defineSetter__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lookupGetter__', '__lookupSetter__', '__lt__', '__module__', '__ne__', '__new__', '__proto__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_js_type_flags', '_tokenize', 'abstr', 'as_object_map', 'asserts', 'astDump', 'astFromParse', 'astnodes', 'bool_check', 'build', 'builtin', 'builtinFiles', 'builtins', 'compile', 'configure', 'constructor', 'dateSet', 'debugout', 'doOneTimeInitialization', 'dumpSymtab', 'dunderToSkulpt', 'execLimit', 'exportSymbol', 'ffi', 'filesLoaded', 'fixReserved', 'formatting', 'gensymcount', 'getSysArgv', 'global_', 'hasOwnProperty', 'importBuiltinWithBody', 'importMain', 'importMainWithBody', 'importModule', 'importModuleInternal_', 'importSearchPathForName', 'importSetUpPath', 'importStar', 'inBrowser', 'inputfun', 'internalPy', 'isArrayLike', 'isPrototypeOf', 'js_beautify', 'js_id', 'longFromStr', 'mangleName', 'misceval', 'object_entries', 'object_keys', 'object_values', 'output', 'parse', 'parseTreeDump', 'propertyIsEnumerable', 'python2', 'python3', 'read', 'realsyspath', 'resetCompiler', 'setupDunderMethods', 'setupObjects', 'setupOperators', 'setup_method_mappings', 'str2number', 'switch_version', 'symboltable', 'sysargv', 'sysmodules', 'syspath', 'timeoutMsg', 'toLocaleString', 'toString', 'to_py', 'token', 'typeof', 'uncaughtException', 'unfixReserved', 'valueOf', 'yieldLimit']

-->

---

<!-- pandoc -s demo05c.md -o demo05c.html -->