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
Input prime: <input id="prime" class="py-input" value="29">
&nbsp;&nbsp;&nbsp;
Select mode:&nbsp; <select id="mode">
    <option value="stepping" selected>Step by step</option>
    <option value="iterating">Iteration</option>
    <option value="hopping">Hopping</option>
</select>
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

scale = 10 # as scale = 1.0 is too small

# input number and mode
# n = 29, mode = 'iterating'
print('n = %d, mode = "%s"' % (n, mode))

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

# the inner square of windmill w = (x, y, z) by turtle t
def core(t, x):
    t.color('black', 'pink')
    t.begin_fill()
    t.pd()
    square(t, x)
    t.end_fill()
    t.pu()

# an arm of windmill w = (x, y, z) by turtle t
def arm(t, y, z):
    t.color('black', 'lavender')
    t.pd()
    t.begin_fill()
    t.fd(z)
    t.rt(90)
    t.fd(y)
    t.rt(90)
    t.fd(z)
    t.rt(90)
    t.fd(y)
    t.end_fill()
    t.pu()

# the mind of windmill w = (x, y, z) by turtle t
# mind (x,y,z) =
# if x < y - z then x + 2 * z else if x < y then 2 * y - x else x
def mind(t, x, y, z):
    if x < y - z:
        s = z
        m = x + 2 * z
    else:
        if x < y:
            s = y - x
            m = 2 * y - x
        else:
            s = 0
            m = x
    # draw the mind
    t.color('red')
    t.fd(s)
    t.lt(90)
    t.fd(s)
    t.rt(90)
    t.pd()
    size = t.pensize()
    t.pensize(5)
    square(t, m)
    t.pensize(size)
    t.pu()

# a windmill turtle w, to be placed at position pos, for triple (x,y,z)
def windmill(t, pos, triple):
    t.pu()
    t.goto(pos)
    t.clear() # erase any writing and path
    t.setheading(90)
    t.backward(10 * scale)
    t.color('black')
    t.write(str(triple), font=("Courier", 16, "bold"))
    t.forward(10 * scale)
    x, y, z = triple
    x, y, z = x * scale, y * scale, z * scale
    # first the inner square
    core(t, x)
    # then the four arms
    for _ in range(4): # 4 sides and 4 arms
        arm(t, y, z)
        t.lt(180)
        t.fd(x)
    # mark the mind in red
    mind(t, x, y, z)

# flip a triple
# flip (x,y,z) = (x,z,y)
def flip(triple):
    x, y, z = triple
    return (x, z, y)

# zagier map of a triple
# zagier (x,y,z) =
# if x < y - z then (x + 2 * z,z,y - z - x)
# else if x < 2 * y then (2 * y - x,y,x + z - y)
# else (x - 2 * y,x + z - y,y)
def zagier(triple):
    x, y, z = triple
    if x < y - z: return (x + 2 * z, z, y - z - x)
    if x < 2 * y: return (2 * y - x, y, x + z - y)
    return (x - 2 * y, x + z - y, y)

# check for zagier fix
def zagier_fix(triple):
    x, y, z = triple
    return x == y

# check for flip fix
def flip_fix(triple):
    x, y, z = triple
    return y == z

# step for hopping
# step c (x,y,z) = (x + c) DIV (2 * z)
def step(c, triple):
    x, y, z = triple
    return (x + c) // (2 * z)

# pop for hopping with known condition
# pop m (x,y,z) = (2 * m * z - x,z,y + m * x - m ** 2 * z)
def pop(m, triple):
    x, y, z = triple
    return (2 * m * z - x, z, y + m * x - m * m * z)

# popping from a triple
# popping c t = pop (step c t) t
def popping(c, triple):
    return pop(step(c, triple), triple)

# mark and tell the two squares from windmill triple
def twoSquares(triple):
    x, y, z = triple
    setheading(0)
    fd(x/2 * scale)
    rt(90)
    fd((x/2 + x + y + z) * 2 * scale)
    lt(90)
    color('green')
    pensize(2)
    pd()
    circle((x + y + z) * 2 * scale)
    pu()
    home()
    setheading(0)
    back(2 * scale)
    s = '%d = %d² + %d²' % (n, x, y + z)
    write(s, font=("Courier", 20, "bold"))

debug = True
# debug = False

# step by step with flip and zagier from zagier-fix
def stepByStep():
    initMills()
    # use the default turtle
    # showturtle()
    # speed(0)
    hideturtle()
    pu()
    setheading(90) # face north
    s = 30 # size of virtual square for 4 diagrams
    fd(s * scale)
    rt(135) # 135 = 180 - 45
    triple = (1, 1, n // 4)
    j = 0
    while True:
        if debug: print('%d: %s' % (j, str(triple)))
        windmill(mills[j % 4], position(), triple)
        # sleep(2) # time to see the windmill
        if flip_fix(triple): break
        # next triple
        triple = flip(triple) if j % 2 == 0 else zagier(triple)
        # next corner
        fd(s * scale)
        rt(90)
        # count escape
        j += 1
        if j > n: break
    # out of loop
    twoSquares(triple)
    rt(90)
    fd(s * scale)
    write('Number of steps = %d' % j, font=("Courier", 20, "bold"))

# iterate by (zagier o flip) from zagier-fix
def iterating():
    initMills()
    # use the default turtle
    # showturtle()
    # speed(0)
    hideturtle()
    pu()
    setheading(90) # face north
    s = 30 # size of virtual square for 4 diagrams
    fd(s * scale)
    rt(135) # 135 = 180 - 45
    triple = (1, 1, n // 4)
    j = 0
    while True:
        if debug: print('%d: %s' % (j, str(triple)))
        windmill(mills[j % 4], position(), triple)
        if flip_fix(triple): break
        sleep(3) # 3s = delay flipping to see the windmill
        # flip triple
        triple = flip(triple)
        windmill(mills[j % 4], position(), triple)
        # next triple
        triple = zagier(triple)
        # next corner
        fd(s * scale)
        rt(90)
        # count escape
        j += 1
        if j > n: break
    # out of loop
    twoSquares(triple)
    rt(90)
    fd(s * scale)
    write('Number of steps = %d' % j, font=("Courier", 20, "bold"))

# hopping by (zagier o flip) from flip of zagier-fix
def hopping():
    initMills()
    # use the default turtle
    # showturtle()
    # speed(0)
    hideturtle()
    pu()
    setheading(90) # face north
    s = 30 # size of virtual square for 4 diagrams
    fd(s * scale)
    rt(135) # 135 = 180 - 45
    triple = (1, n // 4, 1)
    c = int(n ** 0.5) # c = sqrt(n)
    j = 0
    while True:
        if debug: print('%d: %s' % (j, str(triple)))
        windmill(mills[j % 4], position(), triple)
        # sleep(3) # 3s = time to see the windmill
        if flip_fix(triple): break
        # next triple
        triple = popping(c, triple)
        # next corner
        fd(s * scale)
        rt(90)
        # count escape
        j += 1
        if j > n: break
    # out of loop
    twoSquares(triple)
    rt(90)
    fd(s * scale)
    write('Number of steps = %d' % j, font=("Courier", 20, "bold"))

# main program
def main():
    # choose based on mode
    if mode == 'stepping': stepByStep()
    if mode == 'iterating': iterating()
    if mode == 'hopping': hopping()

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

# run a python program in Skulpt
# by calling Sk.importMainWithBody()
def runit():
    # clear output
    Element('output').element.innerHTML = ''
    # get prime and mode
    prime = int(Element('prime').value)
    mode = Element('mode').value
    if debug: print('prime: %d, mode: "%s"' % (prime, mode))
    # get program
    program = ('n, mode = %d, "%s"' % (prime, mode)) + '\n' + Element('windmills').value
    print(program)
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
