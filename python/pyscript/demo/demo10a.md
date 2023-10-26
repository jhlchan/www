---
title: Pyscript - Demo 10A
header-includes: |
    <style>
       body { min-width: 90% !important; }
    </style>
    <style>
       .hide {
          display: none;
       }
    </style>
include-before: |
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js" type="text/javascript"></script>
    <script src="https://skulpt.org/js/skulpt.min.js" type="text/javascript"></script>
    <script src="https://skulpt.org/js/skulpt-stdlib.js" type="text/javascript"></script>
include-after: |
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css"/>
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo10a.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo10a.html -->
---

# Pyscript - Turtle Graphics by Skulpt


A **hypotrochoid** is a type of curve traced by a point attached to a circle of radius $r$ rolling around the inside of a fixed circle of radius $R$, where the point is a distance $d$ from the center of the interior circle.

The parametric equation for a hypotrochoid is:
<!-- $$ ... $$ is a math block, centralized, $ ... $ is inline math --> 
$$
(x(\theta),\ y(\theta)) = (\alpha\ cos\theta\ +\ d\ cos(\beta\theta),\ \alpha\ sin\theta\ -\ d\ sin(\beta\theta))
$$
where $\alpha = (R - r)$, and $\beta = (R - r)/r$.

## Select a program
<select id="choice">
    <option value="code1" selected>Code 1</option>
    <option value="code2">Code 2</option>
</select>


<textarea id="code1" cols="80" rows="10" class="hide">
# Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/
import turtle
from math import cos,sin
from time import sleep

window = turtle.Screen()
window.bgcolor("#FFFFFF")

mySpirograph = turtle.Turtle()
mySpirograph.hideturtle()
mySpirograph.tracer(0)
mySpirograph.speed(0)
mySpirograph.pensize(2)

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.tracer(0)
myPen.speed(0)
myPen.pensize(3)
myPen.color("#AA00AA")

# R = 125
# r = 75.0  # make this a float for Skulpt, otherwise (R-r)/r is an integer.
# d = 125
R = int(input('value of R (default 125)') or '125')
r = float(input('value of r (default 75)') or '75')
d = int(input('value of d (default 125)') or '125')
f = 1 # for r = 75
# f = 8 # for r = 85, how to compute f, the number of repeats for steps?

angle = 0

myPen.penup()
myPen.goto(R-r+d,0)
myPen.pendown()

theta = 0.2
steps = f * int(6*3.14/theta)


for t in range(0,steps):
    mySpirograph.clear()
    mySpirograph.penup()
    mySpirograph.setheading(0)
    mySpirograph.goto(0,-R)
    mySpirograph.color("#999999")
    mySpirograph.pendown()
    mySpirograph.circle(R)
    angle += theta
    
    a, b = (R - r), (R - r)/r

    x = a * cos(angle)
    y = a * sin(angle)
    mySpirograph.penup()
    mySpirograph.goto(x,y-r)
    mySpirograph.color("#222222")
    mySpirograph.pendown()
    mySpirograph.circle(r)
    mySpirograph.penup()
    mySpirograph.goto(x,y)
    mySpirograph.dot(5)
    
    x = a * cos(angle) + d * cos(b * angle)
    y = a * sin(angle) - d * sin(b * angle)
    mySpirograph.pendown()
    mySpirograph.goto(x,y)
    mySpirograph.dot(5)
    myPen.goto(mySpirograph.pos())
    
    mySpirograph.getscreen().update() 
    sleep(0.05)

sleep(0.5)
# Hide Spirograph
mySpirograph.clear()
mySpirograph.getscreen().update()
</textarea>

<textarea id="code2" cols="80" rows="10" class="hide">
# Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/
import turtle
from math import cos,sin
from time import sleep

window = turtle.Screen()
window.bgcolor("#FFFFFF")

mySpirograph = turtle.Turtle()
mySpirograph.hideturtle()
mySpirograph.tracer(0)
mySpirograph.speed(0)
mySpirograph.pensize(2)

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.tracer(0)
myPen.speed(0)
myPen.pensize(3)
myPen.color("#AA00AA")

R = 125
r = 85.0  # make this a float for Skulpt, otherwise (R-r)/r is an integer.
d = 125

angle = 0

myPen.penup()
myPen.goto(R-r+d,0)
myPen.pendown()

theta = 0.2
steps = 8 * int(6*3.14/theta)

for t in range(0,steps):
    mySpirograph.clear()
    mySpirograph.penup()
    mySpirograph.setheading(0)
    mySpirograph.goto(0,-R)
    mySpirograph.color("#999999")
    mySpirograph.pendown()
    mySpirograph.circle(R)
    angle+=theta
    
    x = (R - r) * cos(angle)
    y = (R - r) * sin(angle)
    mySpirograph.penup()
    mySpirograph.goto(x,y-r)
    mySpirograph.color("#222222")
    mySpirograph.pendown()
    mySpirograph.circle(r)
    mySpirograph.penup()
    mySpirograph.goto(x,y)
    mySpirograph.dot(5)
    
    x = (R - r) * cos(angle) + d * cos(((R-r)/r)*angle)
    y = (R - r) * sin(angle) - d * sin(((R-r)/r)*angle)
    mySpirograph.pendown()
    mySpirograph.goto(x,y)
    mySpirograph.dot(5)
    myPen.goto(mySpirograph.pos())
    
    mySpirograph.getscreen().update() 
    sleep(0.05)

sleep(0.02)
# Hide Spirograph
mySpirograph.clear()
mySpirograph.getscreen().update()
</textarea>

## Output{#out}
```{#output .py-terminal}
```
<!-- with Skulpt, Python input in browser becomes a browser input box with prompt in print-area, the output, seen only after input! -->

## Turtle Graphics{#graphics}
<button id="runButton" class="py-button" py-click="runit()" >Run</button>
<button id="stopButton" class="py-button" py-click="stopit()">Stop</button>

:::{#canvas}
:::



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
    # get program
    program = get_program('choice')

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

# get a program from selection
def get_program(label):
    name = Element(label).value
    return Element(name).value

</py-script>
```
<!--
The Pyscript is just the engine to run Skulpt python, which supports turtle graphics.
-->

---

<!-- pandoc -s demo10a.md -o demo10a.html --mathjax  (for better math display) -->
