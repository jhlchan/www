---
title: Pyscript - Demo 12
header-includes: |
    <style>
       body { min-width: 90% !important; }
    </style>
    <style>
        .header {
          text-align: center;
          font-size: 30px;
        }
        .board {
          border: 1px solid black;
          margin: auto;
          width: 80%;
        }
        .picture {
          margin: auto;
          width: 1000px;
          height: 1000px;
        }
        .hide {
            display: none;
        }
        .param {
            background: lightgreen;
        }
        .info {
            background: lavender;
            font-size: 20px;
        }
    </style>
include-before: |
    <script zsrc="https://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js" type="text/javascript"></script>
    <script zsrc="https://skulpt.org/js/skulpt.min.js" src="js/skulpt.min.js" xsrc="js/readable-skulpt.js" type="text/javascript"></script>
    <script zsrc="https://skulpt.org/js/skulpt-stdlib.js" src="js/jc-skulpt-stdlib.js" ysrc="js/skulpt-stdlib.js"  xsrc="js/readable-skulpt-stdlib.js" type="text/javascript"></script>
include-after: |
    <link rel="stylesheet" zhref="https://pyscript.net/latest/pyscript.css" href="js/pyscript.css"/>
    <script defer zsrc="https://pyscript.net/latest/pyscript.js" src="js/pyscript.js"></script>
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo12.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo12.html -->
---

# Pyscript - Windmills by Turtle Graphics in Skulpt


## Turtle Graphics{#graphics}

:::{#controls .py-input}
Select an example:&nbsp; <select id="choice">
    <option value="windmills" selected>Windmills</option>
</select>
&nbsp;&nbsp;&nbsp;
<button id="runButton" class="py-button" py-click="runit()" >Run</button>
&nbsp;&nbsp;&nbsp;
<button id="stopButton" class="py-button" py-click="stopit()">Stop</button>
:::


<!--
Python programs in <textarea> will have text untouched by markdown.
If program is put in <code> and marked {=html}, markdown will escape '>' as '&gt;' and '<' as '&lt;'
Note <textarea> is retrieved by value, while <code> is retrieved by innerHtml.
-->
<textarea id="windmills" class="hide">
from turtle import *
from time import sleep

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

scale = 1.8

# using 4 windmills, each a turtle, appearing in turn.
mills = [Turtle() for i in range(4)]

# initialize the mills
def initMills():
    for t in mills:
        t.hideturtle()
        t.speed(0)

# turtle t to draw a square of side s
def square(t, s):
    for _ in range(4):
        t.rt(90)
        t.fd(s)

# an arm of windmill w = (x, y, z)
def arm(w, y, z):
    w.color('black', 'green')
    w.pd()
    w.begin_fill()
    w.fd(z * scale)
    w.rt(90)
    w.fd(y * scale)
    w.rt(90)
    w.fd(z * scale)
    w.rt(90)
    w.fd(y * scale)
    w.end_fill()
    w.pu()

# the mind of windmill w = (x, y, z)
def mind(w, x, y, z):
    # first the inner square
    w.color('black', 'pink')
    w.begin_fill()
    w.pd()
    square(w, x * scale)
    w.end_fill()
    # then the outer mind
    w.color('red')
    w.pu()
    w.fd(z * scale)
    w.lt(90)
    w.fd(z * scale)
    w.rt(90)
    w.pd()
    size = w.pensize()
    w.pensize(5)
    square(w, (x + 2 * z) * scale)
    w.pensize(size)
    w.pu()

# a windmill, index by j, at position pos, for tuple (x,y,z)
def windmill(j, pos, tuple):
    tuple = (50, 80, 10)
    x, y, z = tuple
    t = mills[j]
    t.pu()
    t.goto(pos)
    t.clear()
    t.setheading(90)
    t.backward(100 * scale)
    t.color('black')
    t.write(str(tuple), font=("Courier", 16, "bold"))
    t.forward(100 * scale)
    for _ in range(4): # 4 sides and 4 arms
        arm(t, y, z)
        t.lt(180)
        t.fd(x * scale)
    # mark the mind in red
    mind(t, x, y, z)

# main program
def main():
    initMills()
    # use the default turtle
    # showturtle()
    # speed(0)
    hideturtle()
    pu()
    setheading(90) # face north
    fd(200 * scale)
    rt(135)  # 135 = 180 - 45
    j = 0
    while True:
        j += 1
        if j > 6: break
        tuple = (j, j+1, j+2)
        # clear() # erase any writing and path
        windmill(j % 4, position(), tuple)
        # sleep(2) # time to see the windmill
        fd(200 * scale)
        rt(90)
    rt(45)
    back(150 * scale)
    pd()
    write('Done!', font=("Courier", 16, "bold"))

try:
    main()
except Exception, e: print e

</textarea>


<!-- For graph output from Skulpt, not PyScript -->
::::{.board}
:::{#canvas .picture}
:::
::::


<!-- For text output from Skulpt, not PyScript -->
## Output{#out}
```{#output .py-terminal}
```

<!-- with Skulpt, Python input in browser becomes a browser input box with prompt in print-area, the output, seen only after input! -->


<!--
Note:
Turtle program is in <textarea>, not in <py-script>.
This is because PyScript will balk at: import turtle
Instead the python program is run by Skulpt, invoked by PyScript.

Python Turtle Spirograph
Posted on February 16, 2018 Posted in Computer Science, Python - Advanced, Python Challenges
https://www.101computing.net/python-turtle-spirograph/

-->

<py-terminal id="debug"></py-terminal>

Type your Python code (hover mouse/pointer to bottom right-end for Green arrow to run code):
<py-repl></py-repl>

<!-- Minimal Javascript to support Pyscript using Skulpt -->
```{=html}
<script>
/* For Python to work, need wrapper of Skuplt functions */

// wrapper for Python call to set up Sk properties
function sk_output(label1, label2) {
    Sk.TurtleGraphics = Sk.TurtleGraphics || {} // default a new dictionary
    Sk.pre = label1
    Sk.TurtleGraphics.target = label2
}

// wrapper for Python call to check if file x is a built-in in Skuplt
function sk_check(x) {
    return Sk.builtinFiles && Sk.builtinFiles["files"][x]
}

// wrapper for Python call to get file[x] from Skuplt built-in
function sk_get(x) {
    return Sk.builtinFiles["files"][x]
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

-->

<!-- pyscript -->
```{=html}
<py-script>
import js
from pyodide.ffi import create_proxy, to_js
from js import document
from js import Sk       # get Skulpt

# logging
# debug = True
debug = False

if not debug: document.getElementById('debug').style = 'display: none'

# set up Sk via Javascript
js.sk_output('output', 'canvas')

# input/output functions are configurable.

# This one is the default (no need to write)
# see: https://github.com/skulpt/skulpt/issues/639
def inf(prompt):
    return js.window.prompt(prompt)

# This one just appends some text to a pre element.
def outf(text):
    pre = Element('output')
    pre.write(text, append=True)

# read a built-in function x
def builtinRead(x):
    if js.sk_check(x):
       return js.sk_get(x)
    else:
       raise "File not found: '" + x + "'"

# See: https://pyodide.org/en/stable/usage/type-conversions.html
# Calling JavaScript functions from Python
# Thus, if you call: f(a=2, b=3)
# then the JavaScript function receives one argument which is a JavaScript object {a : 2, b : 3}.
Sk.configure(output=create_proxy(outf), read=create_proxy(builtinRead), inputfunTakesPrompt = True,) # Yes! this works!
# Sk.configure(output=create_proxy(outf), read=create_proxy(builtinRead), inputfun=create_proxy(inf), inputfunTakesPrompt = True,) # Yes! this works!

# get a program from selection
def get_program(label):
    name = Element(label).value
    return Element(name).value

# run a python program in Skulpt
# by calling Sk.importMainWithBody()
def runit():
    # clear output
    Element('output').element.innerHTML = ''
    # get program
    program = get_program('choice')
    if debug: print(program)

    # run the program
    def fun():
        return Sk.importMainWithBody("stdin", False, program, True)

    # use promise to run
    try:
        promise = Sk.misceval.asyncToPromise(create_proxy(fun))
    except Exception as err: js.console.log(err)

# for the Stop button
def stopit():
    Sk.TurtleGraphics.stop()     # JC: next run will start with a reset screen
    # Sk.TurtleGraphics.reset()  # JC: this will remove the Turtle screen

</py-script>
```
<!--
The Pyscript is just the engine to run Skulpt python, which supports turtle graphics.
-->

---

<!-- pandoc -s demo12.md -o demo12.html -->
