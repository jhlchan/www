---
title: Pyscript - Demo 10E
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
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo10e.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo10e.html -->
---

# Pyscript - Python3 Help Turtle demos in Skulpt


## Turtle Graphics{#graphics}

:::{#controls .py-input}
Select an example:&nbsp; <select id="choice">
    <option value="tree" selected>Tree</option>
    <option value="dance">Round Dance</option>
    <option value="mixer">Color Mixer</option>
    <option value="design">BYTE Design</option>
    <option value="chaos">Chaos</option>
</select>
&nbsp;&nbsp;&nbsp;
<button id="runButton" class="py-button" py-click="runit()" >Run</button>
&nbsp;&nbsp;&nbsp;
<button id="stopButton" class="py-button" py-click="stopit()">Stop</button>
:::

<!--
From PyScript REPL:


dir(Sk.TurtleGraphics.module)
['Screen', 'Turtle', '__bool__', '__class__', '__defineGetter__', '__defineSetter__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lookupGetter__', '__lookupSetter__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__package__', '__proto__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_js_type_flags', 'as_object_map', 'back', 'backward', 'begin_fill', 'bk', 'bye', 'circle', 'clear', 'clone', 'color', 'colormode', 'constructor', 'degrees', 'delay', 'distance', 'done', 'dot', 'down', 'end_fill', 'fd', 'fill', 'fillcolor', 'forward', 'getpen', 'getscreen', 'getturtle', 'goto_$rw$', 'hasOwnProperty', 'heading', 'hideturtle', 'home', 'ht', 'isPrototypeOf', 'isdown', 'isvisible', 'js_id', 'left', 'lt', 'mainloop', 'object_entries', 'object_keys', 'object_values', 'onclick', 'ondrag', 'onrelease', 'pd', 'pencolor', 'pendown', 'pensize', 'penup', 'pos', 'position', 'propertyIsEnumerable', 'pu', 'radians', 'reset', 'right', 'rt', 'seth', 'setheading', 'setpos', 'setposition', 'setundobuffer', 'setx', 'sety', 'shape', 'showturtle', 'speed', 'st', 'stamp', 'toLocaleString', 'toString', 'to_py', 'towards', 'tracer', 'typeof', 'undo', 'undobufferentries', 'up', 'update', 'valueOf', 'width', 'window_height', 'window_width', 'write', 'xcor', 'ycor']

dir(Sk.TurtleGraphics.module.Turtle)
['$d', '$r', 'GenericGetAttr', 'GenericPythonGetAttr', 'GenericPythonSetAttr', 'GenericSetAttr', 'HashNotImplemented', '__bool__', '__call__', '__class__', '__defineGetter__', '__defineSetter__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lookupGetter__', '__lookupSetter__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__proto__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__vectorcalloffset__', '_js_type_flags', 'apply', 'as_object_map', 'back', 'backward', 'begin_fill', 'bk', 'call', 'circle', 'clear', 'clone', 'color', 'colormode', 'constructor', 'degrees', 'delay', 'distance', 'done', 'dot', 'down', 'end_fill', 'fd', 'fill', 'fillcolor', 'forward', 'getpen', 'getscreen', 'getturtle', 'goto_$rw$', 'hasOwnProperty', 'heading', 'hideturtle', 'home', 'ht', 'isPrototypeOf', 'isdown', 'isvisible', 'js_id', 'left', 'length', 'lt', 'mainloop', 'name', 'new', 'ob$eq', 'ob$ge', 'ob$gt', 'ob$le', 'ob$lt', 'ob$ne', 'ob$type', 'object_entries', 'object_keys', 'object_values', 'onclick', 'ondrag', 'onrelease', 'pd', 'pencolor', 'pendown', 'pensize', 'penup', 'pos', 'position', 'propertyIsEnumerable', 'prototype', 'pu', 'radians', 'reset', 'right', 'rt', 'seth', 'setheading', 'setpos', 'setposition', 'setundobuffer', 'setx', 'sety', 'shape', 'showturtle', 'sk$klass', 'sk$object', 'sk$type', 'speed', 'st', 'stamp', 'toLocaleString', 'toString', 'to_py', 'towards', 'tp$base', 'tp$call', 'tp$descr_set', 'tp$getattr', 'tp$hash', 'tp$mro', 'tp$name', 'tp$setattr', 'tp$str', 'tracer', 'typeof', 'undo', 'undobufferentries', 'up', 'update', 'valueOf', 'width', 'window_height', 'window_width', 'write', 'xcor', 'ycor']

dir(Sk.TurtleGraphics.module.Screen)
['$d', '$r', 'GenericGetAttr', 'GenericPythonGetAttr', 'GenericPythonSetAttr', 'GenericSetAttr', 'HashNotImplemented', '__bool__', '__call__', '__class__', '__defineGetter__', '__defineSetter__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lookupGetter__', '__lookupSetter__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__proto__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__vectorcalloffset__', '_js_type_flags', 'addshape', 'apply', 'as_object_map', 'bgcolor', 'bgpic', 'bye', 'call', 'clear', 'clearscreen', 'constructor', 'delay', 'done', 'exitonclick', 'getshapes', 'hasOwnProperty', 'isPrototypeOf', 'js_id', 'length', 'listen', 'mainloop', 'name', 'new', 'ob$eq', 'ob$ge', 'ob$gt', 'ob$le', 'ob$lt', 'ob$ne', 'ob$type', 'object_entries', 'object_keys', 'object_values', 'onclick', 'onkey', 'onscreenclick', 'ontimer', 'propertyIsEnumerable', 'prototype', 'register_shape', 'reset', 'resetscreen', 'setup', 'setworldcoordinates', 'sk$klass', 'sk$object', 'sk$type', 'toLocaleString', 'toString', 'to_py', 'tp$base', 'tp$call', 'tp$descr_set', 'tp$getattr', 'tp$hash', 'tp$mro', 'tp$name', 'tp$setattr', 'tp$str', 'tracer', 'turtles', 'typeof', 'update', 'valueOf', 'window_height', 'window_width']


-->

<!--
Python programs in <textarea> will have text untouched by markdown.
If program is put in <code> and marked {=html}, markdown will escape '>' as '&gt;' and '<' as '&lt;'
Note <textarea> is retrieved by value, while <code> is retrieved by innerHtml.
-->
<textarea id="tree" class="hide">
#!/usr/bin/env python3
"""      turtle-example-suite:

             tdemo_tree.py

Displays a 'breadth-first-tree' - in contrast
to the classical Logo tree drawing programs,
which use a depth-first-algorithm.

Uses:
(1) a tree-generator, where the drawing is
quasi the side-effect, whereas the generator
always yields None.
(2) Turtle-cloning: At each branching point
the current pen is cloned. So in the end
there are 1024 turtles.
"""

from turtle import Turtle, Screen

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

# use a scale to enlarge or shrink
# scale = 0.6  # JC: apply scale to have whole view in Trinket
scale = float(input('Please set a scale from 0.1 to 2 (default 1.6)') or '1.6')
print('scale = %f' % scale) # Python 2.6 formatting
# for the window above, best scale = 1.6

def tree(plist, l, a, f):
    """ plist is list of pens
    l is length of branch
    a is half of the angle between 2 branches
    f is factor by which branch is shortened
    from level to level."""
    # JC: changing 3 to 4 gives less detail. This is don't draw if length <= 3.
    if l > 3:                                # JC: {=html} will escape this
        lst = []
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        for _ in tree(lst, l*f, a, f):
            yield None

def maketree():
    p = Turtle()
    p.setundobuffer(None)
    p.hideturtle()
    p.speed(0)
    p.getscreen().tracer(30,0)
    p.left(90)
    p.penup()
    p.forward(-210 * scale)                  # JC: apply scale
    p.pendown()
    t = tree([p], 200 * scale, 65, 0.6375)   # JC: apply scale
    for _ in t:
        pass

def main():
    maketree()

main()
</textarea>

<textarea id="dance" class="hide">
"""      turtle-example-suite:

         tdemo_round_dance.py

(Needs version 1.1 of the turtle module that
comes with Python 3.1)

Dancing turtles have a compound shape
consisting of a series of triangles of
decreasing size.

Turtles march along a circle while rotating
pairwise in opposite direction, with one
exception. Does that breaking of symmetry
enhance the attractiveness of the example?

Press any key to stop the animation.

Technically: demonstrates use of compound
shapes, transformation of shapes as well as
cloning turtles. The animation is
controlled through update().
"""

from turtle import *

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

# use a scale to enlarge or shrink
scale = float(input('Please set a scale from 0.1 to 2.5 (default 2)') or '2')
print('scale = %f' % scale) # Python 2.6 formatting
# for the window above, best scale = 2

def stop():
    global running
    running = False

def main():
    global running
    tracer(False)
    shape("triangle")
    f =   0.793402
    phi = 9.064678
    s = 5
    c = 1
    # create compound shape
    # JC: remove compound shape
    """
    sh = Shape("compound")
    for i in range(10):
        shapesize(s)
        p = get_shapepoly()
        s *= f
        c *= f
        tilt(-phi)
        sh.addcomponent(p, (c, 0.25, 1-c), "black")
    register_shape("multitri", sh)
    # create dancers
    shapesize(1)
    shape("multitri")
    """
    pu()
    setpos(0, -200 * scale)
    dancers = []
    for i in range(180):
        fd(7 * scale)
        # tilt(-4)  # Python3
        lt(2)
        update()
        if i % 12 == 0:
            dancers.append(clone())
    home()
    # dance
    running = True
    # onkeypress(stop)  # Python3
    # listen()          # Python3
    # window.onkey(stop)  # JC  -- gives invalid exception object
    # window.listen()     # JC
    # There is no need for this, as the page has RUN and STOP.
    cs = 1
    while running:
        ta = -4
        for dancer in dancers:
            dancer.fd(7 * scale)
            dancer.lt(2)
            # dancer.tilt(ta)  # Python3
            ta = -4 if ta > 0 else 2
        if cs < 180:
            right(4)
            # shapesize(cs)  # Python3
            cs *= 1.005
        update()
    return "DONE!"

main()
</textarea>

<textarea id="mixer" class="hide">
# colormixer

from turtle import Turtle, Screen
import math

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

# use a scale to enlarge or shrink
scale = float(input('Please set a scale from 1 to 4 (default 4)') or '4')
# print('scale = %f' % scale) # Python 2.6 formatting
# for the window above, best scale = 4

class ColorTurtle(Turtle):

    def __init__(self, i, x, y):
        Turtle.__init__(self)
        self.shape("turtle")
        # self.resizemode("user")   # Python3
        # self.shapesize(3,3,5)     # Python3
        # self.pensize(10)          # with setworldcoordinates
        self.pensize(2)             # without setworldcoordinates
        self._color = [0,0,0]       # 3 color bars as a list
        self.idx = i
        self._color[i] = y
        self.color(self._color)
        self.speed(0)
        self.left(90)
        self.pu()
        self.goto(x * 50 * scale, 0)
        self.pd()
        self.sety(1 * 100 * scale)
        self.pu()
        self.sety(y * 100 * scale)
        self.pencolor("gray25")
        self.ondrag(self.shift)

    def shift(self, x, y):
        self.sety(max(0,min(y,1 * 100 * scale)))
        self._color[self.idx] = self.ycor() / (100 * scale)  # keep adjusted fraction in list
        self.fillcolor(self._color)
        setbgcolor()

# Hexadecimal Colors
# #rrggbb, Where rr (red), gg (green) and bb (blue) are hexadecimal integers between 00 and ff, specifying the intensity of the color.
def hex_color(red, blue, green):
    rr = math.ceil(red * 255)
    bb = math.ceil(blue * 255)
    gg = math.ceil(green * 255)
    return '#%02x%02x%02x' % (rr, bb, gg)

def setbgcolor():
    # window.bgcolor(red.ycor(), green.ycor(), blue.ycor())  # Python3
    # color = hex_color(red.ycor() / (100 * scale), green.ycor() / (100 * scale), blue.ycor() / (100 * scale))
    # print(red.ycor(), green.ycor(), blue.ycor(), color)
    # print(red._color, green._color, blue._color)
    color = hex_color(red._color[0], green._color[1], blue._color[2])
    window.bgcolor(color)

def main():
    global window, red, green, blue
    window.delay(0)
    # window.setworldcoordinates(-1, -0.3, 3, 1.3)  # JC: no proper write after setworldcoordinates
    window.bgcolor("yellow")

    red = ColorTurtle(0, -1, .5)
    green = ColorTurtle(1, 0, .5)
    blue = ColorTurtle(2, 1, .5)
    setbgcolor()

    writer = Turtle()
    writer.speed(0)
    writer.ht()
    writer.pu()
    # writer.goto(1,1.15)       # Python3
    writer.goto(0, 105 * scale) # without setworldcoordinates
    # with setworldcoordinates, write does not work in Skulpt
    writer.write("DRAG!",align="center",font=("Arial",30,("bold","italic")))
    return "EVENTLOOP"

main()
</textarea>

<textarea id="design" class="hide">
#!/usr/bin/env python3
"""      turtle-example-suite:

        tdemo_bytedesign.py

An example adapted from the example-suite
of PythonCard's turtle graphics.

It's based on an article in BYTE magazine
Problem Solving with Logo: Using Turtle
Graphics to Redraw a Design
November 1982, p. 118 - 134

-------------------------------------------

Due to the statement

t.delay(0)

in line 152, which sets the animation delay
to 0, this animation runs in "line per line"
mode as fast as possible.
"""

from turtle import Turtle, Screen

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

# use a scale to enlarge or shrink
scale = float(input('Please set a scale from 1 to 5 (default 4)') or '4')
print('scale = %f' % scale) # Python 2.6 formatting
# for the window above, best scale = 4

# wrapper for any additional drawing routines
# that need to know about each other
class Designer(Turtle):

    def design(self, homePos, scale):
        self.up()
        for i in range(5):
            self.forward(64.65 * scale)
            self.down()
            self.wheel(self.position(), scale)
            self.up()
            self.backward(64.65 * scale)
            self.right(72)
        self.up()
        self.goto(homePos)
        self.right(36)
        self.forward(24.5 * scale)
        self.right(198)
        self.down()
        self.centerpiece(46 * scale, 143.4, scale)
        self.getscreen().tracer(True)

    def wheel(self, initpos, scale):
        self.right(54)
        for i in range(4):
            self.pentpiece(initpos, scale)
        self.down()
        self.left(36)
        for i in range(5):
            self.tripiece(initpos, scale)
        self.left(36)
        for i in range(5):
            self.down()
            self.right(72)
            self.forward(28 * scale)
            self.up()
            self.backward(28 * scale)
        self.left(54)
        self.getscreen().update()

    def tripiece(self, initpos, scale):
        oldh = self.heading()
        self.down()
        self.backward(2.5 * scale)
        self.tripolyr(31.5 * scale, scale)
        self.up()
        self.goto(initpos)
        self.setheading(oldh)
        self.down()
        self.backward(2.5 * scale)
        self.tripolyl(31.5 * scale, scale)
        self.up()
        self.goto(initpos)
        self.setheading(oldh)
        self.left(72)
        self.getscreen().update()

    def pentpiece(self, initpos, scale):
        oldh = self.heading()
        self.up()
        self.forward(29 * scale)
        self.down()
        for i in range(5):
            self.forward(18 * scale)
            self.right(72)
        self.pentr(18 * scale, 75, scale)
        self.up()
        self.goto(initpos)
        self.setheading(oldh)
        self.forward(29 * scale)
        self.down()
        for i in range(5):
            self.forward(18 * scale)
            self.right(72)
        self.pentl(18 * scale, 75, scale)
        self.up()
        self.goto(initpos)
        self.setheading(oldh)
        self.left(72)
        self.getscreen().update()

    def pentl(self, side, ang, scale):
        if side < (2 * scale): return
        self.forward(side)
        self.left(ang)
        self.pentl(side - (.38 * scale), ang, scale)

    def pentr(self, side, ang, scale):
        if side < (2 * scale): return
        self.forward(side)
        self.right(ang)
        self.pentr(side - (.38 * scale), ang, scale)

    def tripolyr(self, side, scale):
        if side < (4 * scale): return
        self.forward(side)
        self.right(111)
        self.forward(side / 1.78)
        self.right(111)
        self.forward(side / 1.3)
        self.right(146)
        self.tripolyr(side * .75, scale)

    def tripolyl(self, side, scale):
        if side < (4 * scale): return
        self.forward(side)
        self.left(111)
        self.forward(side / 1.78)
        self.left(111)
        self.forward(side / 1.3)
        self.left(146)
        self.tripolyl(side * .75, scale)

    def centerpiece(self, s, a, scale):
        self.forward(s); self.left(a)
        if s < (7.5 * scale):
            return
        self.centerpiece(s - (1.2 * scale), a, scale)

def main():
    t = Designer()
    t.speed(0)
    t.hideturtle()
    t.getscreen().delay(0)
    t.getscreen().tracer(0)
    t.design(t.position(), scale)      # Python3 set scale = 2

main()
</textarea>

<textarea id="chaos" class="hide">
# File: tdemo_chaos.py
# Author: Gregor Lingl
# Date: 2009-06-24

# A demonstration of chaos

from turtle import *

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

# no scale as this uses setworldcoordinates

N = 80

def f(x):
    return 3.9*x*(1-x)

def g(x):
    return 3.9*(x-x**2)

def h(x):
    return 3.9*x-3.9*x*x

def jumpto(x, y):
    penup(); goto(x,y)

def line(x1, y1, x2, y2):
    jumpto(x1, y1)
    pendown()
    goto(x2, y2)

def coosys():
    line(-1, 0, N+1, 0)
    line(0, -0.1, 0, 1.1)

def plot(fun, start, color):
    pencolor(color)
    x = start
    jumpto(0, x)
    pendown()
    dot(5)
    for i in range(N):
        x=fun(x)
        goto(i+1,x)
        dot(5)

def color_plot(a):
    # reset()   # JC: comment this out to have something appearing
    # setworldcoordinates(-1.0,-0.1, N+1, 1.1)      # Python3
    window.clear()                                  # JC
    window.setworldcoordinates(a,-0.1, N+1, 1.1)    # JC
    window.bgcolor('yellow')                        # JC
    speed(0)
    pensize(2)  # JC: add this, default pensize(1) gives tiny dots
    hideturtle()
    coosys()
    plot(f, 0.35, "blue")
    plot(g, 0.35, "green")
    plot(h, 0.35, "red")

def main():
    color_plot(-1.0)
    # Now zoom in:
    # for s in range(100):     # Python3
    #     # setworldcoordinates(0.5*s,-0.1, N+1, 1.1)   # Python3
    #     window.setworldcoordinates(0.5*s,-0.1, N+1, 1.1) # JC: change this
    #     # but now any setworldcoordinates will clear the plots!
    # Now zoom in:
    for s in range(5):
        color_plot(10*s)  # JC: 5 * 10 = 50 = 0.5 * 100
    return "Done!"

main()
# The zoom in action is different from Python3.
# For this one, any setworldcoordinates will clear the image, not stretching the image.
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

<!-- pandoc -s demo10e.md -o demo10e.html -->
