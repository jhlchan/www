---
title: Pyscript - Demo 10
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
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js" type="text/javascript"></script>
    <script src="https://skulpt.org/js/skulpt.min.js" type="text/javascript"></script>
    <script src="https://skulpt.org/js/skulpt-stdlib.js" type="text/javascript"></script>
include-after: |
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css"/>
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo10.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo10.html -->
---

# Pyscript - Spirograph

## Spirograph{#header .header}

A **hypotrochoid** is a type of curve traced by a point attached to a circle of radius $r$ rolling around the inside of a fixed circle of radius $R$, where the point is a distance $d$ from the center of the interior circle.

The parametric equation for a hypotrochoid is:
<!-- $$ ... $$ is a math block, centralized, $ ... $ is inline math --> 
$$
(x(\theta),\ y(\theta)) = (\alpha\ cos\theta\ +\ d\ cos(\beta\theta),\ \alpha\ sin\theta\ -\ d\ sin(\beta\theta))
$$
where $\alpha = (R - r)$, and $\beta = (R - r)/r$.

The angle $\theta$ starts from $0$. When $\theta = 2\pi$, both $cos\theta$ and $sin\theta$ repeats, but not the other terms $cos(\beta\theta)$ and $sin(\beta\theta)$.
For these terms to repeat after $n$ rounds, we need:
$$
\beta(2n\pi)\ =\ 2k\pi \text{for some integer }k, \text{or }n\beta\ \text{an integer}.
$$
Since $\beta$ is a fraction, $n$ is the denominator of the reduced fraction $\beta = \frac{(R - r)}{r}$.


Let $g = gcd(R - r, r) = gcd(R, r)$, the greatest common divisor of $R$ and $r$. Then $r = gn$, or $n = r/gcd(R, r)$.

From Python 3.5 onwards, there is `math.gcd(x,y)` to compute the `gcd` function for integers `x, y`.

## Spirograph examples with parameters

+-------------------+-------------------+------------------------------+-----------------+
| Spiro radius $R$  | Wheel radius $r$  | Pen from wheel center $d$    |  Pattern        |
+==================:+==================:+=============================:+================:+
|   100             |  30               | 100                          | 10-loop clover  |
+-------------------+-------------------+------------------------------+-----------------+
|   125             |  50               | 100                          | 5-loop clover   |
+-------------------+-------------------+------------------------------+-----------------+
|   125             |  75               | 125                          | 5-point star    |
+-------------------+-------------------+------------------------------+-----------------+
|   125             |  85               | 125                          | 25-point star   |
+-------------------+-------------------+------------------------------+-----------------+
|   100             |  50               | 10                           | ellipse         |
+-------------------+-------------------+------------------------------+-----------------+
|   150             |  50               | 10                           | round triangle  |
+-------------------+-------------------+------------------------------+-----------------+
|   150             |  50               | 109                          | 3-loop clover   |
+-------------------+-------------------+------------------------------+-----------------+


:::{.board .param}
&nbsp;&nbsp;&nbsp;
Big circle radius: <select id="radius-big" class="py-input">
    <option value="100" selected>100</option>
    <option value="125">125</option>
    <option value="150">150</option>
</select>
Small circle radius: <select id="radius-small" class="py-input">
    <option value="30" selected>30</option>
    <option value="50">50</option>
    <option value="75">75</option>
    <option value="85">85</option>
</select>
Pen from small center: <select id="radius-pen" class="py-input">
    <option value="10">10</option>
    <option value="100" selected>100</option>
    <option value="125">125</option>
    <option value="150">150</option>
</select>
<input id="circle" type="checkbox" class="py-input"/>show circles
<input id="scale" type="checkbox" class="py-input" checked/>scale to fit 
<button id="runButton" class="py-button" py-click="runit()">Draw</button>
<button id="stopButton" class="py-button" py-click="stopit()">Stop</button>
:::

::::{.board}
:::{#canvas .picture}
:::
::::

<!-- template of spirograph program, supply R, r, d lines as prefix -->
:::{#code .hide}
```{=html}
# Cycloid by ChatGPT (corrected version)

import turtle
import math
from time import sleep

# Create a turtle screen
window = turtle.Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed to the maximum
t.pensize(3)
t.color("#AA00AA")

# Parameters for the cycloid
# R = 100, Radius of the cycloid
# r = 30,  Radius of the rolling circle
# d = 100, Distance from the center of the rolling circle to the tracing point
# n = 3,   number of rounds. (R - r)/r = 70/30 = 7/3, so n = 3 = 30/10, where 10 = gcd(70,30)
n = r // math.gcd(R, r)   # Skulpt 2.6 Python already has math.gcd(x, y)
# print(f'R = {R}, r = {r}, d = {d}, n = {n}') # Skulpt is not yet Python 3 with f-formating
print('R = %d, r = %d, d = %d, n = %d' % (R, r, d, n))
# other controls
print('scale = %f, show circle flag = %r' % (scale, flag))

# scale the length parameters
# Note: scale a float for Skulpt
R, r, d = scale * R, scale * r, scale * d
a, b = (R - r), (R - r)/r
wait = 0  # 0.01 = fast, 0.05 = slow

# Spirograph drawing with circles
def show_spiro():
    # big circle is fixed
    spiro = turtle.Turtle()
    spiro.speed(0)
    spiro.color('white') # if differ from fillcolor, will leave a gap
    spiro.pensize(2)
    spiro.penup()
    spiro.goto(0, -R)
    spiro.pendown()
    spiro.fillcolor('white')
    spiro.begin_fill()
    spiro.circle(R)
    spiro.end_fill()
    spiro.hideturtle()

    # small circle rotates inside
    wheel = turtle.Turtle()
    wheel.hideturtle()
    wheel.tracer(0)  # if tracer is present, the wheel flickers
    wheel.speed(0)

    # parameters
    # R = 125   # spirograph big radius
    # r = 75    # wheel small radius
    # d = 125   # pen from centre of wheel
    # n = number of rounds = r / gcd(R, r)
    # f = 1 # for r = 75
    # f = 8 # for r = 85, how to compute f, the number of repeats for steps?

    # initial positions
    t.penup()
    t.goto(R - r + d, 0)
    t.pendown()
    t.hideturtle()

    for angle in range(0, n * 360 + 1):  # 0 to n * 360 inclusive
        wheel.clear()
        theta = math.radians(angle)
        
        x = a * math.cos(theta)
        y = a * math.sin(theta)
        wheel.penup()
        wheel.goto(x, y - r)
        wheel.pendown()
        wheel.color('plum') # if differ from fillcolor, will leave a gap
        wheel.pensize(2)
        wheel.fillcolor('plum') # lavender purple = #967BB6
        wheel.begin_fill()
        wheel.circle(r)
        wheel.end_fill()
        wheel.penup()
        wheel.goto(x, y)
        wheel.dot(5)
        
        x = a * math.cos(theta) + d * math.cos(b * theta)
        y = a * math.sin(theta) - d * math.sin(b * theta)
        wheel.pendown()
        wheel.color('lightgreen')
        wheel.pensize(3)
        wheel.goto(x, y)
        wheel.dot(5)
        t.goto(wheel.pos())
        
        wheel.getscreen().update() # show wheel as it has tracer(0)
        sleep(wait)

    # hide Spirograph
    sleep(0.5)
    t.hideturtle()
    spiro.clear()
    wheel.clear()
    wheel.getscreen().update()


# Spirograph drawing by trace
def draw_spiro():
    # put turtle at starting point
    t.penup()
    t.goto(R - r + d, 0)
    t.pendown()
    t.hideturtle()

    # trace the (x,y) by direct computation
    for angle in range(0, n * 360 + 1):  #  to n * 360 inclusive
        theta = math.radians(angle)
        x = a * math.cos(theta) + d * math.cos(b * theta)
        y = a * math.sin(theta) - d * math.sin(b * theta)
        t.goto(x, y)
    # todo: turn head of turtle
    # t.hideturtle()

# Animate the spirograph
show_spiro() if flag else draw_spiro()
```
:::

<!--
To test Skulpt, use:
https://trinket.io/turtle

and restore main.py after changes:

import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(500)

draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)

See also:
Skulpt Turtle API Documentaion
https://python-online.ch/pyonline/progs/doc/skulptturtle.pdf

-->

<!--
Note:
Turtle program is in <code>, not in <py-script>.
This is because PyScript will balk at: import turtle
Instead the python program is run by Skulpt, invoked by PyScript.

Python Turtle Spirograph
Posted on February 16, 2018 Posted in Computer Science, Python - Advanced, Python Challenges
https://www.101computing.net/python-turtle-spirograph/

Spirograph Math
Like a wheel within a wheel
http://www.exo.net/~pauld/activities/spirograph/Spirograph.html
A spirograph can be used to create artistically interesting patterns.
The patterns can be used to show:
* the mathematics of least common multiples,
* of clock arithmetic (aka modular arithmetic)
* and the fundamental theorem of mathematics.

number of repeats = denominator of the reduced fraction (R - r)/r
                  = denominator of reduced fraction R/r
                  = q, where  R = g * p, r = g * q, and g = gcd (R,r)
                  = r/gcd (R, r)

# compute gcd
def gcd(x, y):
    if x == 0: return y
    if y == 0: return x
    if y >= x: return gcd(y, x)
    # x < y
    if x == 1: return 1
    return gcd(y % x, x)

There is already math.gcd(x, y) in Python 3.5

HYPOTROCHOID
https://mathcurve.com/courbes2d.gb/hypotrochoid/hypotrochoid.shtml
From the Greek hupo "under" and trokhos "wheel".
Many examples, but no derivation.

-->

<!-- For output from Skulpt, not PyScript -->
## Output{#out}
```{#output .py-terminal}
```

## Derivation

The locus of the turtle tracing the pattern is given by two rotating vectors:

<svg height="320" width="320" class="info">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" 
            refX="0" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" />
    </marker>
  </defs>
  <circle cx="155" cy="155" r="150" stroke="black" stroke-width="3" fill="lightgrey" />
  <circle cx="205" cy="230" r="60" stroke="black" stroke-width="3" fill="lightgreen" />
  <line x1="145" y1="145" x2="195" y2="220" stroke="black" stroke-width="2" marker-end="url(#arrowhead)" />
  <line x1="206" y1="231" x2="220" y2="210" stroke="black" stroke-width="2" marker-end="url(#arrowhead)" />
  <circle cx="232" cy="190" r="3" stroke="red" stroke-width="3" fill="red" />
</svg>

As indicated in the diagram, there is a vector $v_{1}$ from the center of the spirograph to center of the wheel, and another vector $v_{2}$ from center of the wheel to the pen, represented by the red dot.

Assume vector $v_{1}$, of length $R - r$, has angular velocity $\omega_{1}$, and vector $v_{2}$, of length $d$, has angular velocity $\omega_{2}$. The relationship between the angular velocities can be determined by observing the movement of wheel center from two viewpoints:

* relative to the fixed spirograph center, the wheel center moves $(R - r)(\omega_{1}\ t)$ during time $t$,
* relative to the contact point of the wheel and the spirograph, the center moves $r(\omega_{2}\ t)$ in the _opposite_ direction.

Therefore, $(R - r)(\omega_{1}\ t)\ = -r(\omega_{2}\ t)$, giving $\omega_{2} = - \omega_{1}\ (R - r)/r$.

Let $\theta\ =\ \omega_{1}t$. Then the vector position of the pen is given by vector addition $v_{1} + v_{2}$, which is:
$$
\begin{cases}
x\ =\ (R - r)\ cos\ \theta\ +\ d\ cos\ (\theta\ (R - r) / r)\\
y\ =\ (R - r)\ sin\ \theta\ -\ d\ sin\ (\theta\ (R - r) / r)
\end{cases}
$$

Putting $R = q\ r$, and $d = k\ r$ with $q \gt 1$, the equations become:
$$
\begin{cases}
x/r\ =\ (q - 1)\ cos\ \theta\ +\ k\ cos\ ((q - 1)\ \theta)\\
y/r\ =\ (q - 1)\ sin\ \theta\ -\ k\ sin\ ((q - 1)\ \theta)
\end{cases}
$$
Hence the spirograph patterns depend only on the ratios $q$ and $k$. Indeed, $q - 1\ =\ \lvert \omega_{2}/\omega_{1}\ \rvert$.

When $q = n$, an integer, and $k \lt 1$, the spirograph resembles a rounded version of the regular $n$-sided polygon.

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

/* Not working yet!

// Customizing modules after import
// see: https://skulpt.org/using.html
Sk.onAfterImport = function(library) {
  switch(library) {
    case 'pygal':
      // make charts render instantly
      Highcharts.setOptions({
        plotOptions: {
          series: {
            animation: false
          }
        }
      });
      break;
    case 'turtle':
      // make turtle draw instantly
      Sk.tg.defaults.animate = false;
      Sk.tg.Turtle.prototype.speed = function() {}
      Sk.tg.Turtle.prototype.delay = function() {}
      break;
  }
}
// not really for turtle, need to investigate.
*/
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
Sk.configure(output=create_proxy(outf), read=create_proxy(builtinRead), inputfunTakesPrompt = True,) # Yes! this works, too!
# Sk.configure(output=create_proxy(outf), read=create_proxy(builtinRead), inputfun=create_proxy(inf), inputfunTakesPrompt = True,) # Yes! this works!

# get a program from selection
def get_program():
    R = int(Element('radius-big').value)
    r = int(Element('radius-small').value)
    d = int(Element('radius-pen').value)
    check = document.getElementById('scale').checked
    scale = float(500/(2 * R + 5)) if check else 1.0  # scale = 500/(2 * R + margin), a float
    flag = document.getElementById('circle').checked
    # compose the program
    program = []
    program.append(f'R, r, d, scale, flag = {R}, {r}, {d}, {scale}, {flag}')
    # Note: innerHtml is read-only
    program.append(Element('code').innerHtml)
    return '\n'.join(program)

# run a python program in Skulpt
# by calling Sk.importMainWithBody()
def runit():    
    # clear output
    Element('output').element.innerHTML = ''
    # compose program from parameters
    program = get_program()
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

<!-- pandoc -s demo10.md -o demo10.html --mathjax  (for better math display) -->
