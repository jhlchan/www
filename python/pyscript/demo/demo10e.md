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
    <script zsrc="https://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js" type="text/javascript"></script>
    <script zsrc="https://skulpt.org/js/skulpt.min.js" src="js/skulpt.min.js" xsrc="js/readable-skulpt.js" type="text/javascript"></script>
    <script zsrc="https://skulpt.org/js/skulpt-stdlib.js" src="js/jc-skulpt-stdlib.js" ysrc="js/skulpt-stdlib.js"  xsrc="js/readable-skulpt-stdlib.js" type="text/javascript"></script>
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
    <option value="test" selected>Test</option>
    <option value="tree">Tree</option>
    <option value="dance">Round Dance</option>
    <option value="mixer">Color Mixer</option>
    <option value="design">BYTE Design</option>
    <option value="chaos">Chaos</option>
    <option value="clock">Clock</option>
    <option value="sorts">Sorting</option>
    <option value="paint">Paint</option>
    <option value="kolam">Lindenmayer</option>
    <option value="penrose">Penrose Tiling</option>
    <option value="peace">Peace Flag Symbol</option>
    <option value="rosette">Rosette</option>
    <option value="nim">Nim Game</option>
    <option value="ying">YinYang</option>
    <option value="fractal">Fractal Curves</option>
    <option value="gravity">Sun, Earth and Moon</option>
    <option value="forest">Forest</option>
    <option value="mirror">Two Turtles</option>
    <option value="hanoi">Tower of Hanoi</option>
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

dir(Sk.builtin)
['AssertionError', 'AttributeError', 'BaseException', 'Exception', 'ExternalError', 'IOError', 'ImportError', 'IndentationError', 'IndexError', 'KeyError', 'LookupError', 'NameError', 'NegativePowerError', 'NotImplemented', 'NotImplementedError', 'OperationError', 'OverflowError', 'PyType_IsSubtype', 'RuntimeError', 'StopIteration', 'SuspensionError', 'SyntaxError', 'SystemError', 'SystemExit', 'TimeLimitError', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'ValueError', 'ZeroDivisionError', '__bool__', '__class__', '__defineGetter__', '__defineSetter__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__import__', '__init__', '__init_subclass__', '__le__', '__lookupGetter__', '__lookupSetter__', '__lt__', '__module__', '__ne__', '__new__', '__proto__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '_js_type_flags', '_tryGetSubscript', 'abs', 'all', 'any', 'apply_', 'as_object_map', 'ascii', 'asnum$', 'asnum$nofloat', 'assk$', 'biginteger', 'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'bytes_iter_', 'callable', 'checkBool', 'checkBytes', 'checkCallable', 'checkClass', 'checkComplex', 'checkFloat', 'checkFunction', 'checkInt', 'checkIterable', 'checkNone', 'checkNumber', 'checkSequence', 'checkString', 'chr', 'coerce', 'complex', 'constructor', 'create_dict_iter_', 'delattr', 'dict', 'dict_iter_', 'dictview', 'dir', 'divmod', 'enumerate', 'eval_', 'execfile', 'fabs', 'file', 'filter', 'filter_', 'float_', 'format', 'frozenset', 'func', 'generator', 'getExcInfo', 'getattr', 'globals', 'hasOwnProperty', 'hasattr', 'hash', 'hashCount', 'help', 'hex', 'id', 'idCount', 'input', 'int2str_', 'int_', 'intern', 'interned', 'isPrototypeOf', 'isinstance', 'issubclass', 'iter', 'iterator', 'js_id', 'jseval', 'jsmillis', 'len', 'list', 'listSlice', 'list_iter_', 'lng', 'locals', 'makeGenerator', 'make_structseq', 'map', 'map_', 'max', 'memoryview', 'method', 'min', 'module', 'next_', 'nmber', 'none', 'numtype', 'object', 'object_entries', 'object_keys', 'object_values', 'oct', 'open', 'ord', 'pow', 'print', 'propertyIsEnumerable', 'pyCheckArgs', 'pyCheckArgsLen', 'pyCheckType', 'quit', 'range', 'range_', 'raw_input', 'reduce', 'reload', 'repr', 'reversed', 'round', 'seqtype', 'set', 'set_iter_', 'setattr', 'slice', 'slice$start', 'slice$step', 'slice$stop', 'sorted', 'str', 'str_iter_', 'structseq_types', 'sum', 'super_', 'timSort', 'toLocaleString', 'toString', 'to_py', 'tuple', 'tuple_iter_', 'type', 'type_is_subtype_base_chain', 'typeof', 'unichr', 'valueOf', 'vars', 'xrange', 'zip', 'zip_']

-->

<!--
Python programs in <textarea> will have text untouched by markdown.
If program is put in <code> and marked {=html}, markdown will escape '>' as '&gt;' and '<' as '&lt;'
Note <textarea> is retrieved by value, while <code> is retrieved by innerHtml.
-->
<textarea id="test" class="hide">
from turtle import *

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

# color of turtle
t = Turtle()
print(t.color())
# ('black', 'black')  , first is color, second is fillcolor.
t.color('yellow', 'red')
print(t.color())
# ('yellow', 'red')
print(t.fillcolor())
# red,  Need to recheck some examples using color(p, q)

t.color(0.5, 0.5, 0.5)
print(t.color())
# ((127, 127, 127), (127, 127, 127))

# print(window.color())   invalid exception object
print(window.bgcolor())
# yellow
window.bgcolor(0.1, 0.2, 0.3)
print(window.bgcolor())
# (25, 51, 76)
# Thus there should be no need for hex_color(r, b, g)

window.bgcolor('yellow')
# How to register shapes?
print(window.getshapes())
# ['arrow', 'square', 'triangle', 'classic', 'turtle', 'circle']

# screen.register_shape("triangle", ((5,-3), (0,5), (-5,-3)))

print(type(t))                # <class 'turtle.Turtle'>

"""
try:
    import inspect            # No module named inspect
    print(dir(inspect))
except Exception, e: print(e)


make_hand_shape("second_hand", 125, 25)
((-18.75,0.00), (125.00,0.00), (125.00,-12.50), (146.65,-0.00), (125.00,12.50), (125.00,0.00))
make_hand_shape("minute_hand",  130, 25)
((-19.50,0.00), (130.00,0.00), (130.00,-12.50), (151.65,-0.00), (130.00,12.50), (130.00,0.00))
make_hand_shape("hour_hand", 90, 25)
((-13.50,0.00), (90.00,0.00), (90.00,-12.50), (111.65,-0.00), (90.00,12.50), (90.00,0.00))

"""

# line = builtin.to_py([[0,0], [1,1]])
# line = [(0,0), (1,1)]  # seems to wok
# line = ((0,0), (1,1))    # also works
line = ((-18.75,0.00), (125.00,0.00), (125.00,-12.50), (146.65,-0.00), (125.00,12.50), (125.00,0.00))
print(line)
try:
    window.addshape("linear", line)  # ok with jc-skulpt-stdlib.js
    print('shape registered!')
    t.shape("linear")
    print('shape change')
    t.pensize(10)
    t.rt(90)
    t.fd(100)
    print('see turtle?')
except Exception, e: print(e)


# get poly a triangle with side s
def triangle(s):
    poly = []
    poly.append(pos())
    for _ in range(3):
        fd(s)
        lt(120)  # interior 60, exterior 120
        poly.append(pos())
    return poly

# get poly of a pentagram star with side s
def pentagram(s):
    poly = []
    poly.append(pos())
    for _ in range(5):
        fd(s)
        rt(-144)  # interior 36, exterior = 180 - 36 = 144, clockwise
        poly.append(pos())
    return poly

try:
    print('HERE')
    reset()
    showturtle()
    poly = pentagram(50)
    print(poly)
    window.register_shape("pentagram", poly)
    shape("pentagram")
    fd(100)
    print('DONE')
except Exception, e: print(e)

try:
    row = [100.23, 200.45, 300.67]
    print([i/100 for i in row])
except Exception, e: print(e)

try:
    from random import choice
    COLORS = ["orange", "blue", "green", "purple", "dark blue"]

    hideturtle()
    speed('fastest')

    setundobuffer(100) # need this in Skulpt
    for _ in range(20):
        pencolor(choice(COLORS))
        circle(50)
        left(20)

    tracer(20)  # value unrelated to either 20 above
    print(undobufferentries()) # just a zero, 0.
    while undobufferentries() > 1:
        undo()  # undo everything but hideturtle()
    tracer(1)
except Exception, e: print e


# Oriental Daily 東方日報  8/11 娛樂
</textarea>

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

# get poly of a pentagram star with side s
def pentagram(s):
    poly = []
    poly.append(pos())
    for _ in range(5):
        fd(s)
        rt(-144)  # interior 36, exterior = 180 - 36 = 144, clockwise
        poly.append(pos())
    return poly

def stop():
    global running
    running = False

def main():
    global running
    # tracer(False)   # Python3, works with later update() but slower
    tracer(0)         # JC, with later update(). Much faster!
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
    # JC: try to make a 'compound' shape
    poly = pentagram(50)
    window.register_shape("pentagram", poly)
    shape("pentagram")
    reset()    # remove the pentagram star, then home()
    # end JC
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

# Note: Python3 demo example has compound shape.
# For simple register_shape, the turtle shape is always filled, so no components.
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
    # Method 1
    # color = hex_color(red._color[0], green._color[1], blue._color[2])
    # window.bgcolor(color)
    # Method 2
    window.bgcolor(red._color[0], green._color[1], blue._color[2]) # JC: this works!

def main():
    global red, green, blue                         # global for setbgcolor()
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

<textarea id="clock" class="hide">
# debugger     # invokes browser debugger
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
"""       turtle-example-suite:

             tdemo_clock.py

Enhanced clock-program, showing date
and time
  ------------------------------------
   Press STOP to exit the program!
  ------------------------------------
"""
from turtle import *
from datetime import datetime

def jump(distanz, winkel=0):
    penup()
    right(winkel)
    forward(distanz)
    left(winkel)
    pendown()

def hand(laenge, spitze):
    form = []            # JC: simulate begin_poly() and end_poly() by form
    form.append(pos())
    fd(laenge*1.15)
    form.append(pos())
    rt(90)
    fd(spitze/2.0)
    form.append(pos())
    lt(120)
    fd(spitze)
    form.append(pos())
    lt(120)
    fd(spitze)
    form.append(pos())
    lt(120)
    fd(spitze/2.0)
    form.append(pos())
    return form

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

# use a scale to enlarge or shrink
scale = float(input('Please set a scale from 1 to 2 (default 1.8)') or '1.8')
print('scale = %f' % scale) # Python 2.6 formatting
# for the window above, best scale = 1.8

def make_hand_shape(name, laenge, spitze):
    reset()
    speed(0)     # JC, not required for Python3
    jump(-laenge*0.15)
    # begin_poly()    # Python3
    # hand(laenge, spitze)
    # end_poly()      # Python3
    # hand_form = get_poly()  # Python3
    # hand_form = ((0,0), (1,1))  # This Skulpt version uses ((x,y), ...)
    hand_form = hand(laenge, spitze)
    print(hand_form)
    # register_shape(name, hand_form) # Python3
    window.register_shape(name, hand_form) # JC  invalid exception object! cannot resolve this.

"""
make_hand_shape("second_hand", 125, 25)
((-18.75,0.00), (125.00,0.00), (125.00,-12.50), (146.65,-0.00), (125.00,12.50), (125.00,0.00))
make_hand_shape("minute_hand",  130, 25)
((-19.50,0.00), (130.00,0.00), (130.00,-12.50), (151.65,-0.00), (130.00,12.50), (130.00,0.00))
make_hand_shape("hour_hand", 90, 25)
((-13.50,0.00), (90.00,0.00), (90.00,-12.50), (111.65,-0.00), (90.00,12.50), (90.00,0.00))
"""
"""
scale = 1.0000000
[(-18.75, 0.0), (125.0, 0.0), (125.0, -12.5), (146.650635095, 0.0), (125.0, 12.5), (125.0, 0.0)]
((-18.75, 0.0), (125.0, 0.0), (125.0, -12.5), (146.65, -0.0), (125.0, 12.5), (125.0, 0.0))
[(-19.5, 0.0), (130.0, 0.0), (130.0, -12.5), (151.650635095, 0.0), (130.0, 12.5), (130.0, 0.0)]
((-18.75, 0.0), (125.0, 0.0), (125.0, -12.5), (146.65, -0.0), (125.0, 12.5), (125.0, 0.0))
[(-13.5, 0.0), (90.0, 0.0), (90.0, -12.5), (111.650635095, 0.0), (90.0, 12.5), (90.0, 0.0)]
((-18.75, 0.0), (125.0, 0.0), (125.0, -12.5), (146.65, -0.0), (125.0, 12.5), (125.0, 0.0))

scale = 1.8000000
[(-33.75, 0.0), (225.0, 0.0), (225.0, -12.5), (246.650635095, 0.0), (225.0, 12.5), (225.0, 0.0)]
[(-35.1, 0.0), (234.0, 0.0), (234.0, -12.5), (255.650635095, 0.0), (234.0, 12.5), (234.0, 0.0)]
[(-24.3, 0.0), (162.0, 0.0), (162.0, -12.5), (183.650635095, 0.0), (162.0, 12.5), (162.0, 0.0)]
"""

def clockface(radius):
    reset()
    speed(0)     # JC, not required for Python3
    pensize(7)
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            fd(25)
            jump(-radius-25)
        else:
            dot(3)
            jump(-radius)
        rt(6)

def setup():
    global second_hand, minute_hand, hour_hand, writer
    # mode("logo")    # Python3
    make_hand_shape("second_hand", 125 * scale, 25)
    make_hand_shape("minute_hand",  130 * scale, 25)
    make_hand_shape("hour_hand", 90 * scale, 25)
    clockface(160 * scale)
    second_hand = Turtle()
    second_hand.shape("second_hand")
    second_hand.color("gray20", "gray80")
    minute_hand = Turtle()
    minute_hand.shape("minute_hand")
    minute_hand.color("blue1", "red1")
    hour_hand = Turtle()
    hour_hand.shape("hour_hand")
    hour_hand.color("blue3", "red3")
    for hand in second_hand, minute_hand, hour_hand:
        # hand.resizemode("user")  # Python3
        # hand.shapesize(1, 1, 3)  # Python3
        hand.speed(0)
    ht()
    writer = Turtle()
    # writer.mode("logo")
    writer.ht()
    writer.pu()
    # writer.bk(85) # for logo mode, no need
    writer.speed(0) # JC: to prevent flickers

def wochentag(t):
    wochentag = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    return wochentag[t.weekday()]

def datum(z):
    monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
             "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
    j = z.year
    m = monat[z.month - 1]
    t = z.day
    return "%s %d %d" % (m, t, j)

def tick():
    t = datetime.today()
    sekunde = t.second + t.microsecond*0.000001
    minute = t.minute + sekunde/60.0
    stunde = t.hour + minute/60.0
    sekunde = - sekunde  # JC: negate for clockwise, now not in logo mode
    try:
        # tracer(False)  # Terminator can occur here
        writer.clear()
        writer.home()
        writer.lt(90)  # JC: logo mode heads north
        writer.forward(65 * scale)
        # weekday on top
        writer.write(wochentag(t),
                     align="center", font=("Courier", 14, "bold"))
        writer.back(150 * scale)
        # date on bottom
        writer.write(datum(t),
                     align="center", font=("Courier", 14, "bold"))
        writer.forward(85 * scale)
        second_hand.setheading(6*sekunde)
        minute_hand.setheading(6*minute)
        hour_hand.setheading(30*stunde)
        # tracer(True)
        # ontimer(tick, 100)   # Python3
        window.ontimer(tick, 100)  # JC
        update()  # JC: replaces tracer(True) and tracer(False)
    except Terminator:
        pass  # turtledemo user pressed STOP

def main():
    tracer(0)  # JC: this is much better, later with update()
    # tracer(False)   # JC: remove
    setup()
    # tracer(True)    # JC: remove
    tick()
    return "EVENTLOOP"

main()

"""
 turtle.mode(mode=None)

    Parameters

        mode – one of the strings “standard”, “logo” or “world”

    Set turtle mode (“standard”, “logo” or “world”) and perform reset. If mode is not given, current mode is returned.

    Mode “standard” is compatible with old turtle.
    Mode “logo” is compatible with most Logo turtle graphics.
    Mode “world” uses user-defined “world coordinates”. Attention: in this mode angles appear distorted if x/y unit-ratio doesn’t equal 1.

    Mode           Initial turtle heading    positive angles
    -----------    ----------------------    ---------------
    “standard”     to the right (east)       counterclockwise
    “logo”         upward (north)            clockwise

Skulpt has "standard" (default) and "world" modes.
"""
# Cannot make register_shape to work. Due to missing co_varnames for register_shape in standard library. Fixed in js-skulpt-stdlib.js.
# Final info display is still one single line. Due to lacking "logo" mode. Need turtle facing north at start for proper writing.
# After fixing register_shape, and recording the hand positions,
# this now works -- except that the hand goes anticlockwise, and date and weekday flickers.
# Looks like the clock is upside-down!  Due to original logo mode? Yes!
# In setheading, use opposite angles. Remove flickering by tracer(0) then update().
</textarea>

<textarea id="sorts" class="hide">
#!/usr/bin/env python3
"""

         sorting_animation.py

A minimal sorting algorithm animation:
Sorts a shelf of 10 blocks using insertion
sort, selection sort and quicksort.

Shelfs are implemented using builtin lists.

Blocks are turtles with shape "square", but
stretched to rectangles by shapesize()
 ---------------------------------------
       To exit press space button
 ---------------------------------------
"""
from turtle import *
import random

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

class Block(Turtle):

    def __init__(self, size):
        self.size = size
        # Turtle.__init__(self, shape="square", visible=False)  # Python3
        Turtle.__init__(self)  # JC: add this        
        self.shape("square")   # JC
        self.hideturtle()      # JC
        self.pu()
        # self.shapesize(size * 1.5, 1.5, 2) # square to rectangle  # Python3
        self.fillcolor("black")
        self.st()
        # JC: change the square to rectangle, see Shelf.push() for height and width
        name = 'block' + str(size)
        poly = [(0,0), (size * 10, 0), (size * 10, 32), (0, 32)]
        window.register_shape(name, poly)
        self.shape(name)

    def glow(self):
        self.fillcolor("red")

    def unglow(self):
        self.fillcolor("black")

    def __repr__(self):
        # return "Block size: {0}".format(self.size)
        return "Block size: %d" % self.size


class Shelf(list):

    # JC: only one call of Shelf(-200)
    # def __init__(self, y):
    #     "create a shelf. y is y-position of first block"
    #     self.y = y
    #     self.x = -150

    def __init__(self):
        self.y = -200
        self.x = -150

    def push(self, d):
        # width, _, _ = d.shapesize()   # Python3
        width = d.size                  # JC: use this
        # align blocks by the bottom edge
        # y_offset = width / 2 * 20    # Skulpt has integer divison
        y_offset = width * 10          # JC: modify
        d.sety(self.y + y_offset)
        d.setx(self.x + 34 * len(self))
        self.append(d)

    def _close_gap_from_i(self, i):
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos - 34)

    def _open_gap_from_i(self, i):
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos + 34)

    def pop(self, key):
        b = list.pop(self, key)
        b.glow()
        b.sety(200)
        self._close_gap_from_i(key)
        return b

    def insert(self, key, b):
        self._open_gap_from_i(key)
        list.insert(self, key, b)
        b.setx(self.x + 34 * key)
        # width, _, _ = b.shapesize()  # Python3
        width = b.size                 # JC
        # align blocks by the bottom edge
        # y_offset = width / 2 * 20    # Skulpt has integer divison
        y_offset = width * 10          # JC: modify
        b.sety(self.y + y_offset)
        b.unglow()

def isort(shelf):
    length = len(shelf)
    for i in range(1, length):
        hole = i
        while hole > 0 and shelf[i].size < shelf[hole - 1].size:
            hole = hole - 1
        shelf.insert(hole, shelf.pop(i))
    return

def ssort(shelf):
    length = len(shelf)
    for j in range(0, length - 1):
        imin = j
        for i in range(j + 1, length):
            if shelf[i].size < shelf[imin].size:
                imin = i
        if imin != j:
            shelf.insert(j, shelf.pop(imin))

def partition(shelf, left, right, pivot_index):
    pivot = shelf[pivot_index]
    shelf.insert(right, shelf.pop(pivot_index))
    store_index = left
    for i in range(left, right): # range is non-inclusive of ending value
        if shelf[i].size < pivot.size:
            shelf.insert(store_index, shelf.pop(i))
            store_index = store_index + 1
    shelf.insert(store_index, shelf.pop(right)) # move pivot to correct position
    return store_index

def qsort(shelf, left, right):
    if left < right:
        pivot_index = left
        pivot_new_index = partition(shelf, left, right, pivot_index)
        qsort(shelf, left, pivot_new_index - 1)
        qsort(shelf, pivot_new_index + 1, right)

def randomize():
    disable_keys()
    clear()
    target = list(range(10))
    random.shuffle(target)
    for i, t in enumerate(target):
        for j in range(i, len(s)):
            if s[j].size == t + 1:
                s.insert(i, s.pop(j))
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def show_text(text, line=0):
    line = 20 * line
    goto(0,-250 - line)
    write(text, align="center", font=("Courier", 16, "bold"))

def start_ssort():
    disable_keys()
    clear()
    show_text("Selection Sort")
    ssort(s)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def start_isort():
    disable_keys()
    clear()
    show_text("Insertion Sort")
    isort(s)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def start_qsort():
    disable_keys()
    clear()
    show_text("Quicksort")
    qsort(s, 0, len(s) - 1)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def init_shelf():
    global s
    # s = Shelf(-200)    # Python3
    s = Shelf()          # JC: using the new __init__
    vals = (4, 2, 8, 9, 1, 5, 10, 3, 7, 6)
    for i in vals:
        s.push(Block(i))

def disable_keys():
    window.onkey(None, "s")
    window.onkey(None, "i")
    window.onkey(None, "q")
    window.onkey(None, "r")

def enable_keys():
    window.onkey(start_isort, "i")
    window.onkey(start_ssort, "s")
    window.onkey(start_qsort, "q")
    window.onkey(randomize, "r")
    window.onkey(bye, "space")

def main():
    ht()
    penup()
    init_shelf()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()
    window.listen()
    return "EVENTLOOP"

instructions1 = "press i for insertion sort, s for selection sort, q for quicksort"
instructions2 = "spacebar to quit, r to randomize"

main()
# Python3 version has shapesize() to change the 'square' turtle to 'rectangular' turtle.
</textarea>

<textarea id="paint" class="hide">
#!/usr/bin/env python3
"""       turtle-example-suite:

            tdemo_paint.py

A simple  event-driven paint program

- left mouse button moves turtle
- middle mouse button changes color
- right mouse button toggles between pen up
(no line drawn when the turtle moves) and
pen down (line is drawn). If pen up follows
at least two pen-down moves, the polygon that
includes the starting point is filled.
 -------------------------------------------
 Play around by clicking into the canvas
 using all three mouse buttons.
 -------------------------------------------
          To exit press STOP button
 -------------------------------------------
"""
from turtle import *

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
# window.bgcolor("yellow")  # white background

# Global colors
colors=["red", "green", "blue", "yellow"]

def switchupdown():
    # if pen()["pendown"]:  # Python3
    if isdown():            # JC: use this
        end_fill()
        up()
        shape("circle")
    else:
        down()
        shape("triangle")
        begin_fill()

def changecolor():
    global colors
    colors = colors[1:]+colors[:1]
    color(colors[0])
    fillcolor(colors[0])

def main():
    speed(0)  # JC
    # shape("circle")
    # resizemode("user")   # Python3
    # shapesize(.5)        # Python3
    width(3)
    color(colors[0])
    fillcolor(colors[0])
    switchupdown()
    # onscreenclick(goto,1)             # Python3
    # onscreenclick(changecolor,2)      # Python3
    # onscreenclick(switchupdown,3)     # Python3
    # Skulpt onscreenclick = mousedown, ignores button
    # JC: use click as 1, key c to change color, key x for up/down, key z to clear.
    window.onscreenclick(goto,1)
    window.onkey(changecolor, "c")
    window.onkey(switchupdown, "x")
    window.onkey(reset, "z")
    window.listen()
    return "EVENTLOOP"

main()
# Note: must first click on canvas to listen, which also moves the turtle.
</textarea>

<textarea id="kolam" class="hide">
#!/usr/bin/env python3
"""       turtle-example-suite:

        xtx_lindenmayer_indian.py

Each morning women in Tamil Nadu, in southern
India, place designs, created by using rice
flour and known as kolam on the thresholds of
their homes.

These can be described by Lindenmayer systems,
which can easily be implemented with turtle
graphics and Python.

Two examples are shown here:
(1) the snake kolam
(2) anklets of Krishna

Taken from Marcia Ascher: Mathematics
Elsewhere, An Exploration of Ideas Across
Cultures

"""
################################
# Mini Lindenmayer tool
###############################

from turtle import *
from time import sleep
from math import sqrt

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

# use a scale to enlarge or shrink
scale = float(input('Please set a scale from 1 to 2 (default 1.8)') or '1.8')
print('scale = %f' % scale) # Python 2.6 formatting
# for the window above, best scale = 1.8

def replace( seq, replacementRules, n ):
    for i in range(n):
        newseq = ""
        for element in seq:
            newseq = newseq + replacementRules.get(element,element)
        seq = newseq
    return seq

def draw( commands, rules ):
    for b in commands:
        try:
            rules[b]()
        except TypeError:
            try:
                draw(rules[b], rules)
            except:
                pass

def example1():
    ################################
    # Example 1: Snake kolam
    ################################


    def r():
        right(45)

    def l():
        left(45)

    def f():
        forward(7.5 * scale)

    snake_rules = {"-":r, "+":l, "f":f, "b":"f+f+f--f--f+f+f"}
    snake_replacementRules = {"b": "b+f+b--f--b+f+b"}
    snake_start = "b--f--b--f"

    drawing = replace(snake_start, snake_replacementRules, 3)

    reset()
    speed(3)
    tracer(1,0)
    ht()
    up()
    backward(195 * scale)
    down()
    draw(drawing, snake_rules)

def example2():
    ################################
    # Example 2: Anklets of Krishna
    ################################

    def A():
        color("red")
        circle(10,90)

    def B():
        color("black")
        l = 5/sqrt(2)
        forward(l * scale)
        circle(l, 270)
        forward(l * scale)

    def F():
        color("green")
        forward(10 * scale)

    krishna_rules = {"a":A, "b":B, "f":F}
    krishna_replacementRules = {"a" : "afbfa", "b" : "afbfbfbfa" }
    krishna_start = "fbfbfbfb"

    reset()
    speed(0)
    tracer(3,0)
    ht()
    left(45)
    drawing = replace(krishna_start, krishna_replacementRules, 3)
    draw(drawing, krishna_rules)
    tracer(1)


def main():
    example1()
    sleep(3)
    example2()
    return "Done!"

main()
</textarea>

<textarea id="penrose" class="hide">
#!/usr/bin/env python3
"""       xturtle-example-suite:

          xtx_kites_and_darts.py

Constructs two aperiodic penrose-tilings,
consisting of kites and darts, by the method
of inflation in six steps.

Starting points are the patterns "sun"
consisting of five kites and "star"
consisting of five darts.

For more information see:
 http://en.wikipedia.org/wiki/Penrose_tiling
 -------------------------------------------
"""
from turtle import *
from math import cos, pi, sqrt
from time import sleep

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

# No need to scale for tiling.

f = (sqrt(5)-1)/2.0   # golden ratio
d = 2 * cos(3*pi/10)

# JC: return poly path of kite
def kite(l):
    poly = []
    poly.append(pos())
    fl = f * l
    lt(36)
    fd(l)
    poly.append(pos())
    rt(108)
    fd(fl)
    poly.append(pos())
    rt(36)
    fd(fl)
    poly.append(pos())
    rt(108)
    fd(l)
    poly.append(pos())
    rt(144)
    return poly

# JC: return poly path of dart
def dart(l):
    poly = []
    poly.append(pos())
    fl = f * l
    lt(36)
    fd(l)
    poly.append(pos())
    rt(144)
    fd(fl)
    poly.append(pos())
    lt(36)
    fd(fl)
    poly.append(pos())
    rt(144)
    fd(l)
    poly.append(pos())
    rt(144)
    return poly

# global constants
kite_poly = None
dart_poly = None

# multiply a tuple by n
def multiply(pair, n):
    x, y = pair
    return (1.0 * x * n, 1.0 * y * n)  # ensure floats in Skulpt

# mimic Python3 shapesize
def shapesize(a, b, th):
    global kite_poly, dart_poly
    # this program has only two shapes: kite and dart
    # and the only call has a = b, so ignore b and th
    # just stretch each shape by a factor a.
    poly = [multiply(i,a) for i in kite_poly]
    window.register_shape("kite", poly)
    poly = [multiply(i,a) for i in dart_poly]
    window.register_shape("dart", poly)

def inflatekite(l, n):
    if n == 0:
        px, py = pos()
        h, x, y = int(heading()), round(px,3), round(py,3)
        tiledict[(h,x,y)] = True
        return
    fl = f * l
    lt(36)
    inflatedart(fl, n-1)
    fd(l)
    rt(144)
    inflatekite(fl, n-1)
    lt(18)
    fd(l*d)
    rt(162)
    inflatekite(fl, n-1)
    lt(36)
    fd(l)
    rt(180)
    inflatedart(fl, n-1)
    lt(36)

def inflatedart(l, n):
    if n == 0:
        px, py = pos()
        h, x, y = int(heading()), round(px,3), round(py,3)
        tiledict[(h,x,y)] = False
        return
    fl = f * l
    inflatekite(fl, n-1)
    lt(36)
    fd(l)
    rt(180)
    inflatedart(fl, n-1)
    lt(54)
    fd(l*d)
    rt(126)
    inflatedart(fl, n-1)
    fd(l)
    rt(144)

def draw(l, n, th=2):
    clear()
    lt(90)         # JC: logo mode starts with turtle facing north
    l = l * f**n
    # shapesize(l/100.0, l/100.0, th)  # Python3
    # JC: due to no change in shapesize, there is no tiling!
    shapesize(l/100.0, l/100.0, th)  # now use JC version
    # if n < 2: print('tiledict', tiledict)    # print this only at start
    # n = 0:
    # ('tiledict', {(90, 0.0, 0.0): True, (162, 0.0, 0.0): True, (234, 0.0, 0.0): True, (306, 0.0, 0.0): True, (18, 0.0, 0.0): True})
    # 5 kites and 0 darts = 5 pieces.
    # n = 1:
    # ('tiledict', {(126, 0.0, 0.0): False, (342, -176.336, 242.705): True, (198, 176.336, 242.705): True, (54, 0.0, 0.0): False, (198, 0.0, 0.0): False, (54, -285.317, -92.705): True, (270, -176.336, 242.705): True, (270, 0.0, -0.0): False, (126, 0.0, -300.0): True, (342, -285.317, -92.705): True, (342, 0.0, 0.0): False, (198, 285.317, -92.705): True, (54, -0.0, -300.0): True, (270, 176.336, 242.705): True, (126, 285.317, -92.705): True})
    # 10 kites and 5 darts = 15 pieces.
    for k in tiledict:
        h, x, y = k
        setpos(x, y)
        setheading(h)
        if tiledict[k]:
            shape("kite")
            color("black", (0, 0.75, 0))
        else:
            shape("dart")
            color("black", (0.75, 0, 0))
        stamp()  # mark this

def sun(l, n):
    for i in range(5):
        inflatekite(l, n)
        lt(72)

def star(l,n):
    for i in range(5):
        inflatedart(l, n)
        lt(72)

def makeshapes():
    global kite_poly, dart_poly
    tracer(0)
    # begin_poly()   # Python3
    kite_poly = kite(100) # JC
    # end_poly()     # Python3
    # register_shape("kite", get_poly())  # Python3
    window.register_shape("kite", kite_poly)   # JC: modify
    # begin_poly()   # Python3
    dart_poly = dart(100) # JC
    # end_poly()     # Python3
    # register_shape("dart", get_poly())  # Python3
    window.register_shape("dart", dart_poly)   # JC: modify
    tracer(1)

def start():
    reset()
    lt(90)   # JC: logo mode starts with turtle facing north
    ht()
    pu()
    makeshapes()
    # resizemode("user")   # Python3

def test(l=200, n=4, fun=sun, startpos=(0,0), th=2):
    global tiledict
    goto(startpos)
    setheading(0)
    lt(90)         # JC: logo mode starts with turtle facing north
    tiledict = {}
    tracer(0)
    fun(l, n)
    draw(l, n, th)
    tracer(1)
    nk = len([x for x in tiledict if tiledict[x]])
    nd = len([x for x in tiledict if not tiledict[x]])
    print("%d kites and %d darts = %d pieces." % (nk, nd, nk+nd))

def demo(fun=sun):
    start()
    for i in range(8):
        test(300, i, fun)

def main():
    # title("Penrose-tiling with kites and darts.")
    # mode("logo")          # Python3
    # bgcolor(0.3, 0.3, 0)  # Python3
    window.bgcolor(0.3, 0.3, 0)  # JC
    demo(sun)
    sleep(2)
    demo(star)
    pencolor("black")
    goto(0,-200)
    pencolor(0.7,0.7,1)
    write("Please wait...",
          align="center", font=('Arial Black', 36, 'bold'))
    test(600, 8, startpos=(70, 117))
    return "Done"

main()

# Unable to do shapesize(), so there is no actual tiling.
# Now work out shapesize(), and there is actual tiling!
</textarea>

<textarea id="peace" class="hide">
#!/usr/bin/env python3
"""       turtle-example-suite:

              tdemo_peace.py

A simple drawing suitable as a beginner's
programming example. Aside from the
peacecolors assignment and the for loop,
it only uses turtle commands.
"""

from turtle import *

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
# window.bgcolor("yellow") # keep white background

# no need to scale

def main():
    # peacecolors = ("red3",  "orange", "yellow", "seagreen4", "orchid4", "royalblue1", "dodgerblue4")
    peacecolors = ("#cd0000",  "orange", "yellow", "#2e8b57", "#da70d6", "#4169e1", "#104e8b")

    reset()
    Screen()
    up()
    goto(-320,-195)
    width(70)

    for pcolor in peacecolors:
        color(pcolor)
        down()
        forward(640)
        up()
        backward(640)
        left(90)
        forward(66)
        right(90)

    width(25)
    color("white")
    goto(0,-170)
    down()

    circle(170)
    left(90)
    forward(340)
    up()
    left(180)
    forward(170)
    right(45)
    down()
    forward(170)
    up()
    backward(170)
    left(90)
    down()
    forward(170)
    up()

    goto(0,300) # vanish if hideturtle() is not available ;-)
    return "Done!"

main()

# This Skulpt has fewer colors, so "seagreen4", "orchid4", "royalblue1", "dodgerblue4" all keep the last color, which is "yellow".
# Use hex colors.
</textarea>

<textarea id="rosette" class="hide">
"""      turtle-example-suite:

          tdemo_wikipedia3.py

This example is
inspired by the Wikipedia article on turtle
graphics. (See example wikipedia1 for URLs)

First we create (ne-1) (i.e. 35 in this
example) copies of our first turtle p.
Then we let them perform their steps in
parallel.

Followed by a complete undo().
"""

from turtle import *
from time import sleep

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

# use a scale to enlarge or shrink
scale = float(input('Please set a scale from 1 to 2 (default 1.8)') or '1.8')
print('scale = %f' % scale) # Python 2.6 formatting
# for the window above, best scale = 1.8

def mn_eck(p, ne, sz):
    turtlelist = [p]
    # create ne-1 additional turtles
    for i in range(1, ne):
        q = p.clone()
        q.rt(360.0/ne)
        turtlelist.append(q)
        p = q

    for i in range(ne):
        c = abs(ne/2.0 - i)/(ne * 0.7)
        # let those ne turtles make a step in parallel:
        for t in turtlelist:
            t.rt(360./ne)
            t.pencolor(1-c, 0, c)
            t.fd(sz)

def main():
    p = Turtle()
    p.speed(0)
    p.hideturtle()
    p.pencolor("red")
    p.pensize(3)
    p.setundobuffer(50) # JC: putting this will trigger while loop 3 times, and slower

    window.tracer(36, 0)

    mn_eck(p, 36, 19 * scale)

    sleep(1)

    print('Window has %d turtles.' % len(window.turtles()))
    while any(t.undobufferentries() for t in window.turtles()):
        for t in window.turtles():
            # print('undo buffer: %d' % t.undobufferentries())
            t.undo()
        sleep(0.1)
        update()
        # undo leave a last circle?!
    """
    # This doesn't work.
    print('Window has %d turtles.' % len(window.turtles()))
    for t in window.turtles():
        while t.undobufferentries():
            print('undo buffer: %d' % t.undobufferentries())
            t.undo()
    """        

main()
# undo works, but too fast!
</textarea>

<textarea id="nim" class="hide">
"""      turtle-example-suite:

            tdemo_nim.py

Play nim against the computer. The player
who takes the last stick is the winner.

Implements the model-view-controller
design pattern.
"""

import turtle
import random
import time

# SCREENWIDTH = 640
# SCREENHEIGHT = 480
SCREENWIDTH = 1000
SCREENHEIGHT = 1000

# No need to scale

MINSTICKS = 7
MAXSTICKS = 31

HUNIT = SCREENHEIGHT // 12
WUNIT = SCREENWIDTH // ((MAXSTICKS // 5) * 11 + (MAXSTICKS % 5) * 2)

# Python3:
# SCOLOR = (63, 63, 31)
# HCOLOR = (255, 204, 204)
# COLOR = (204, 204, 255)
# Skulpt: has fraction colors, and / is integer divsion unless floats.
SCOLOR = (63./255, 63./255, 31./255)
HCOLOR = (255./255, 204./255, 204./255)
COLOR = (204./255, 204./255, 255./255)


# Create a turtle screen
window = turtle.Screen()
# window.setup(1000, 1000) # default (500, 500)
window.setup(SCREENWIDTH, SCREENHEIGHT)
# window.bgcolor("yellow") # JC: will set in NimView

# use a scale to enlarge or shrink
# scale = float(input('Please set a scale from 1 to 2 (default 1.8)') or '1.8')
# print('scale = %f' % scale) # Python 2.6 formatting
# for the window above, best scale = 1.8
# ???

def randomrow():
    return random.randint(MINSTICKS, MAXSTICKS)

def computerzug(state):
    xored = state[0] ^ state[1] ^ state[2]
    if xored == 0:
        return randommove(state)
    for z in range(3):
        s = state[z] ^ xored
        if s <= state[z]:
            move = (z, s)
            return move

def randommove(state):
    m = max(state)
    while True:
        z = random.randint(0,2)
        if state[z] > (m > 1):
            break
    rand = random.randint(m > 1, state[z]-1)
    return z, rand


class NimModel(object):
    def __init__(self, game):
        self.game = game

    def setup(self):
        if self.game.state not in [Nim.CREATED, Nim.OVER]:
            return
        self.sticks = [randomrow(), randomrow(), randomrow()]
        print('sticks: ', self.sticks)
        self.player = 0
        self.winner = None
        self.game.view.setup()
        self.game.state = Nim.RUNNING

    def move(self, row, col):
        maxspalte = self.sticks[row]
        self.sticks[row] = col
        self.game.view.notify_move(row, col, maxspalte, self.player)
        if self.game_over():
            self.game.state = Nim.OVER
            self.winner = self.player
            self.game.view.notify_over()
        elif self.player == 0:
            self.player = 1
            row, col = computerzug(self.sticks)
            self.move(row, col)
            self.player = 0

    def game_over(self):
        return self.sticks == [0, 0, 0]

    def notify_move(self, row, col):
        if self.sticks[row] <= col:
            return
        self.move(row, col)


# define a stick shape
def makeStickShape():
    # self.shape("square")
    # self.shapesize(HUNIT/10.0, WUNIT/20.0)  # Python3 
    # turtle square has poly: [(10,-10),(10,10),(-10,10),(-10, -10)];
    # shapesize stretches each (x,y), x by factor HUNIT/10, y by factor WUNIT/20
    # hence the stick poly is: [(HUNIT, -WUNIT/2), ... ]
    window.register_shape('stick', [(HUNIT, -WUNIT/2), (HUNIT, WUNIT/2), (-HUNIT, WUNIT/2), (-HUNIT, -WUNIT/2)])

class Stick(turtle.Turtle):
    def __init__(self, row, col, game):
        # turtle.Turtle.__init__(self, visible=False)  # Python3
        turtle.Turtle.__init__(self)       # JC
        self.hideturtle()                  # JC
        self.row = row
        self.col = col
        self.game = game
        x, y = self.coords(row, col)
        # self.shape("square")
        # self.shapesize(HUNIT/10.0, WUNIT/20.0)  # Python3
        self.shape("stick")
        self.speed(0)
        self.pu()
        self.goto(x,y)
        self.color("white")
        self.showturtle()

    def coords(self, row, col):
        packet, remainder = divmod(col, 5)
        x = (3 + 11 * packet + 2 * remainder) * WUNIT
        y = (2 + 3 * row) * HUNIT
        return x - SCREENWIDTH // 2 + WUNIT // 2, SCREENHEIGHT // 2 - y - HUNIT // 2

    def makemove(self, x, y):
        if self.game.state != Nim.RUNNING:
            return
        self.game.controller.notify_move(self.row, self.col)


class NimView(object):
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.model = game.model
        # self.screen.colormode(255)  # Python3
        self.screen.tracer(False)
        # self.screen.bgcolor(240, 240, 255) # JC
        self.screen.bgcolor(240./255, 240./255, 1.0)
        print('set bgcolor')
        # self.writer = turtle.Turtle(visible=False)  # Python3
        self.writer = turtle.Turtle()   # JC
        self.writer.hideturtle()        # JC
        self.writer.pu()
        self.writer.speed(0)
        self.sticks = {}
        for row in range(3):
            for col in range(MAXSTICKS):
                self.sticks[(row, col)] = Stick(row, col, game)
        self.display("... a moment please ...")
        self.screen.tracer(True)

    def display(self, msg1, msg2=None):
        self.screen.tracer(False)
        self.writer.clear()
        if msg2 is not None:
            self.writer.goto(0, - SCREENHEIGHT // 2 + 48)
            self.writer.pencolor("red")
            self.writer.write(msg2, align="center", font=("Courier",18,"bold"))
        self.writer.goto(0, - SCREENHEIGHT // 2 + 20)
        self.writer.pencolor("black")
        self.writer.write(msg1, align="center", font=("Courier",14,"bold"))
        self.screen.tracer(True)

    def setup(self):
        self.screen.tracer(False)
        for row in range(3):
            for col in range(self.model.sticks[row]):
                self.sticks[(row, col)].color(SCOLOR)
        for row in range(3):
            for col in range(self.model.sticks[row], MAXSTICKS):
                self.sticks[(row, col)].color("white")
        self.display("Your turn! Click leftmost stick to remove.")
        self.screen.tracer(True)

    def notify_move(self, row, col, maxspalte, player):
        if player == 0:
            farbe = HCOLOR
            for s in range(col, maxspalte):
                self.sticks[(row, s)].color(farbe)
        else:
            self.display(" ... thinking ...         ")
            time.sleep(0.5)
            self.display(" ... thinking ... aaah ...")
            farbe = COLOR
            for s in range(maxspalte-1, col-1, -1):
                time.sleep(0.2)
                self.sticks[(row, s)].color(farbe)
            self.display("Your turn! Click leftmost stick to remove.")

    def notify_over(self):
        if self.game.model.winner == 0:
            msg2 = "Congrats. You're the winner!!!"
        else:
            msg2 = "Sorry, the computer is the winner."
        self.display("To play again press space bar. To leave press ESC.", msg2)

    def clear(self):
        if self.game.state == Nim.OVER:
            self.screen.clear()


class NimController(object):

    def __init__(self, game):
        self.game = game
        self.sticks = game.view.sticks
        self.BUSY = False
        for stick in self.sticks.values():
            stick.onclick(stick.makemove)
        self.game.screen.onkey(self.game.model.setup, "space")
        self.game.screen.onkey(self.game.view.clear, "Escape")
        self.game.view.display("Press space bar to start game")
        self.game.screen.listen()

    def notify_move(self, row, col):
        if self.BUSY:
            return
        self.BUSY = True
        self.game.model.notify_move(row, col)
        self.BUSY = False


class Nim(object):
    CREATED = 0
    RUNNING = 1
    OVER = 2
    def __init__(self, screen):
        self.state = Nim.CREATED
        self.screen = screen
        print('set screen')
        self.model = NimModel(self)
        print('set model')
        self.view = NimView(self)
        print('set view')
        self.controller = NimController(self)
        print('set controller')

def main():
    # mainscreen = turtle.Screen()
    # mainscreen.mode("standard")   # Python3
    # mainscreen.setup(SCREENWIDTH, SCREENHEIGHT)
    # nim = Nim(mainscreen)
    makeStickShape() # JC: to replace shapesize
    nim = Nim(window)
    return "EVENTLOOP"

main()

# Note: with makeStickShape(), the sticks are the same as Python3 Demo example.
# With fractional SCOLOR, HCOLOR and COLOR, all colors are correct, and plays a perfect Nim game.
</textarea>

<textarea id="ying" class="hide">
#!/usr/bin/env python3
"""       turtle-example-suite:

            tdemo_yinyang.py

Another drawing suitable as a beginner's
programming example.

The small circles are drawn by the circle
command.

"""

from turtle import *

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

# use a scale to enlarge or shrink
scale = float(input('Please set a scale from 1 to 2 (default 1.8)') or '1.8')
print('scale = %f' % scale) # Python 2.6 formatting
# for the window above, best scale = 1.8

def yin(radius, color1, color2):
    width(3)
    color("black", color1)  # Python3 or Skulpt
    # color("black"); fillcolor(color1)    # JC
    begin_fill()
    circle(radius/2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius/2., 180)
    end_fill()
    left(90)
    up()
    forward(radius*0.35)
    right(90)
    down()
    color(color1, color2)   # Python3 or Skulpt
    # color(color1); fillcolor(color2)    # JC
    begin_fill()
    circle(radius*0.15)
    end_fill()
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)

def main():
    reset()
    yin(200 * scale, "black", "white")
    yin(200 * scale, "white", "black")
    ht()
    return "Done!"

main()

# Note: need to split Python3 color(pen, fill) into color(pen); fillcolor(fill)  for Trinket
# There is no need to split this for color(pen, fill) in Skulpt!
</textarea>

<textarea id="fractal" class="hide">
#!/usr/bin/env python3
"""      turtle-example-suite:

        tdemo_fractalCurves.py

This program draws two fractal-curve-designs:
(1) A hilbert curve (in a box)
(2) A combination of Koch-curves.

The CurvesTurtle class and the fractal-curve-
methods are taken from the PythonCard example
scripts for turtle-graphics.
"""

from turtle import *
from time import sleep    # JC

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

# use a scale to enlarge or shrink
scale = float(input('Please set a scale from 1 to 2 (default 1.8)') or '1.8')
print('scale = %f' % scale) # Python 2.6 formatting
# for the window above, best scale = 1.8

# class CurvesTurtle(Pen):   # Python3 original
class CurvesTurtle(Turtle):  # JC
    # example derived from
    # Turtle Geometry: The Computer as a Medium for Exploring Mathematics
    # by Harold Abelson and Andrea diSessa
    # p. 96-98
    def hilbert(self, size, level, parity):
        if level == 0:
            return
        # rotate and draw first subcurve with opposite parity to big curve
        self.left(parity * 90)
        self.hilbert(size, level - 1, -parity)
        # interface to and draw second subcurve with same parity as big curve
        self.forward(size)
        self.right(parity * 90)
        self.hilbert(size, level - 1, parity)
        # third subcurve
        self.forward(size)
        self.hilbert(size, level - 1, parity)
        # fourth subcurve
        self.right(parity * 90)
        self.forward(size)
        self.hilbert(size, level - 1, -parity)
        # a final turn is needed to make the turtle
        # end up facing outward from the large square
        self.left(parity * 90)

    # Visual Modeling with Logo: A Structural Approach to Seeing
    # by James Clayson
    # Koch curve, after Helge von Koch who introduced this geometric figure in 1904
    # p. 146
    def fractalgon(self, n, rad, lev, dir):
        import math

        # if dir = 1 turn outward
        # if dir = -1 turn inward
        edge = 2 * rad * math.sin(math.pi / n)
        self.pu()
        self.fd(rad)
        self.pd()
        self.rt(180 - (90 * (n - 2) / n))
        for i in range(n):
            self.fractal(edge, lev, dir)
            self.rt(360 / n)
        self.lt(180 - (90 * (n - 2) / n))
        self.pu()
        self.bk(rad)
        self.pd()

    # p. 146
    def fractal(self, dist, depth, dir):
        if depth < 1:
            self.fd(dist)
            return
        self.fractal(dist / 3, depth - 1, dir)
        self.lt(60 * dir)
        self.fractal(dist / 3, depth - 1, dir)
        self.rt(120 * dir)
        self.fractal(dist / 3, depth - 1, dir)
        self.lt(60 * dir)
        self.fractal(dist / 3, depth - 1, dir)

def main():
    ft = CurvesTurtle()

    ft.reset()
    ft.speed(0)
    ft.ht()
    ft.getscreen().tracer(1,0)
    ft.pu()

    # Hilbert Curve
    size = 6 * scale
    ft.setpos(-33*size, -32*size)
    ft.pd()

    ft.fillcolor("red")
    ft.begin_fill()
    ft.fd(size)

    print('Hilbert curve, size %d, level %d, parity %d' % (size, 6, 1))
    ft.hilbert(size, 6, 1)

    # frame the Hilbert Curve
    ft.fd(size)
    for i in range(3):
        ft.lt(90)
        ft.fd(size*(64+i%2))
    ft.pu()
    for i in range(2):
        ft.fd(size)
        ft.rt(90)
    ft.pd()
    for i in range(4):
        ft.fd(size*(66+i%2))
        ft.rt(90)
    ft.end_fill() # of red

    sleep(3)

    ft.reset()
    ft.speed(0)
    ft.ht()
    ft.getscreen().tracer(1,0)

    # Koch curve
    ft.color("black", "blue")  # Python3 color or Skulpt
    # ft.color("black"); ft.fillcolor("blue")  # JC
    print('Koch curve, order %d, size %d, level %d, direction %d' % (3, 250, 4, 1))
    ft.begin_fill()
    ft.fractalgon(3, 250 * scale, 4, 1)
    ft.end_fill()
    print('Koch curve, order %d, size %d, level %d, direction %d' % (3, 200, 4, 1))
    ft.begin_fill()
    ft.color("red")
    ft.fractalgon(3, 200 * scale, 4, -1)
    ft.end_fill()

main()

# Note: Fractal curves now have scaling for full view.
</textarea>

<textarea id="gravity" class="hide">
#!/usr/bin/env python3
"""       turtle-example-suite:

        tdemo_planets_and_moon.py

Gravitational system simulation using the
approximation method from Feynman-lectures,
p.9-8, using turtlegraphics.

Example: heavy central body, light planet,
very light moon!
Planet has a circular orbit, moon a stable
orbit around the planet.

You can hold the movement temporarily by
pressing the left mouse button with the
mouse over the scrollbar of the canvas.

"""

from turtle import *

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

# use a scale to enlarge or shrink
scale = float(input('Please set a scale from 1 to 2 (default 1.8)') or '1.8')
print('scale = %f' % scale) # Python 2.6 formatting
# for the window above, best scale = 1.8

G = 8 * scale  # JC: adjust gravity strength when applying scale

# absolute value of a tuple
def abs(pair):
    x, y = pair
    return (x * x + y * y) ** 0.5  # JC: without math.sqrt

# add two tuples
def add(pair1, pair2):
    x1, y1 = pair1
    x2, y2 = pair2
    return (x1 + x2, y1 + y2)

# multiply a tuple by n
def multiply(pair, n):
    x, y = pair
    return (1.0 * x * n, 1.0 * y * n)  # ensure floats in Skulpt

# poly for a unit circle
unit_circle = [(1.,0.), (.951,.309), (.809,.588), (.588,.809), (.309,.951),
               (0.,1.), (-.309,.951), (-.588,.809), (-.809,.588), (-.951,.309),
               (-1.,0.), (-.951,-.309), (-.809,-.588), (-.588,-.809), (-.309,-.951),
               (-0.,-1.), (.309,-.951), (.588,-.809), (.809,-.588), (.951,-.309)]

# get poly of a circle with radius r
def circle_poly(r):
    return [multiply(i,r) for i in unit_circle]

class GravSys(object):
    def __init__(self):
        self.planets = []
        self.t = 0
        self.dt = 0.01
    def init(self):
        for p in self.planets:
            p.init()
    def start(self):
        for i in range(10000):
            self.t += self.dt
            for p in self.planets:
                p.step()

class Star(Turtle):
    # m = mass, initial location x, initial velocity v, gravity_system, shape name
    def __init__(self, m, x, v, gravSys, shape):
        # Turtle.__init__(self, shape=shape) # Python3
        Turtle.__init__(self)  # JC
        self.shape(shape)      # JC
        self.penup()
        # self.hideturtle()    # JC: cannot hide, otherwise they are invisible!
        self.m = m
        self.setpos(x)
        self.v = v
        gravSys.planets.append(self)
        self.gravSys = gravSys
        # self.resizemode("user")  # Python3
        self.pendown()

    def init(self):
        dt = self.gravSys.dt
        self.a = self.acc()
        # self.v = self.v + 0.5*dt*self.a     # Python3
        self.v = add(self.v, multiply(self.a, 0.5 * dt))  # JC

    def acc(self):
        # a = Vec(0,0)   # Python3
        a = (0,0)        # JC
        for planet in self.gravSys.planets:
            if planet != self:
                # v = planet.pos()-self.pos()    # Python3
                x1, y1 = planet.pos()            # JC
                x2, y2 = self.pos()              # JC
                v = (x1 - x2, y1 - y2)           # JC
                # a += (G*planet.m/abs(v)**3)*v  # Python3
                a = add(a, multiply(v, G*planet.m/abs(v)**3))  # JC
        return a

    def step(self):
        dt = self.gravSys.dt
        # self.setpos(self.pos() + dt*self.v)    # Python3
        self.setpos(add(self.pos(), multiply(self.v, dt)))  # JC
        if self.gravSys.planets.index(self) != 0:
            self.setheading(self.towards(self.gravSys.planets[0]))
        self.a = self.acc()
        # self.v = self.v + dt*self.a  # Python3
        self.v = add(self.v, multiply(self.a, dt))  # JC


## create compound yellow/blue turtleshape for planets
def makeShapes():
    # no compound shapes, just bigger or smaller circles
    window.register_shape('sun', circle_poly(18))  # JC: from 10 * 1.8, sun.shapesize(1.8)
    window.register_shape('earth', circle_poly(8)) # JC: from 10 * 0.8, earth.shapesize(0.8)
    window.register_shape('moon', circle_poly(5))  # JC: from 10 * 0.5, moon.shapesize(0.5)

def main():
    makeShapes()

    ## setup gravitational system
    gs = GravSys()

    # Sun
    # sun = Star(1000000, Vec(0,0), Vec(0,-2.5), gs, "circle")  # Python3
    sun = Star(1000000, (0,0), (0,-2.5), gs, "sun") # JC 
    sun.color("red")      # JC: instead of "yellow"
    # sun.shapesize(1.8)  # Python3
    sun.pu()

    # Earch
    # earth = Star(12500, Vec(210,0), Vec(0,195), gs, "planet")  # Python3
    earth = Star(12500, (210 * scale,0), (0,195), gs, "earth")  # JC
    earth.color("brown")  # JC
    earth.pencolor("green")
    # earth.shapesize(0.8) # Python3
    
    # Moon
    # moon = Star(1, Vec(220,0), Vec(0,295), gs, "planet")  # Python3
    moon = Star(1, (220 * scale,0), (0,295), gs, "moon")  # JC
    moon.color("orange")   # JC
    moon.pencolor("blue")
    # moon.shapesize(0.5)  # Python3
    
    gs.init()
    gs.start()
    return "Done!"

main()

# Note: a good simulation of graivty with turtles!
</textarea>

<textarea id="forest" class="hide">
#!/usr/bin/env python3
"""     turtlegraphics-example-suite:

             tdemo_forest.py

Displays a 'forest' of 3 breadth-first-trees
similar to the one in tree.
For further remarks see tree.py

This example is a 'breadth-first'-rewrite of
a Logo program written by Erich Neuwirth. See
http://homepage.univie.ac.at/erich.neuwirth/
"""

from turtle import *
from random import randrange

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

# use a scale to enlarge or shrink
scale = float(input('Please set a scale from 1 to 2 (default 1.2)') or '1.2')
print('scale = %f' % scale) # Python 2.6 formatting
# for the window above, best scale = 1.2, but the forest is random.

def symRandom(n):
    return randrange(-n,n+1)

def randomize( branchlist, angledist, sizedist ):
    return [ (angle+symRandom(angledist),
              sizefactor*1.01**symRandom(sizedist))
                     for angle, sizefactor in branchlist ]

def randomfd( t, distance, parts, angledist ):
    for i in range(parts):
        t.left(symRandom(angledist))
        t.forward( (1.0 * distance)/parts )

def tree(tlist, size, level, widthfactor, branchlists, angledist=10, sizedist=5):
    # (German) benutzt Liste von turtles und Liste von Zweiglisten,
    # (German) fuer jede turtle eine!
    # uses list of turtles and list of branch lists,
    # one for each turtle!
    # print('tree: level %d' % level)
    # This is a Python generator, with next() built-in.
    if level > 0:
        lst = []
        brs = []
        for t, branchlist in list(zip(tlist,branchlists)):
            t.pensize( size * widthfactor )
            # t.pencolor( 255 - (180 - 11 * level + symRandom(15)),
            #             180 - 11 * level + symRandom(15),
            #             0 )
            # Skulpt colors are three fractions
            t.pencolor( (255 - (180 - 11 * level + symRandom(15)))/255.,
                        (180 - 11 * level + symRandom(15))/255.,  0. )
            t.pendown()
            randomfd(t, size, level, angledist )
            yield 1
            for angle, sizefactor in branchlist:
                t.left(angle)
                lst.append(t.clone())
                brs.append(randomize(branchlist, angledist, sizedist))
                t.right(angle)
        for x in tree(lst, size*sizefactor, level-1, widthfactor, brs,
                      angledist, sizedist):
            yield None


def start(t,x,y):
    # colormode(255)   # Python3
    t.reset()
    t.speed(0)
    t.hideturtle()
    t.left(90)
    t.penup()
    t.setpos(x,y)
    t.pendown()

def doit1(level, pen):
    pen.hideturtle()
    start(pen, 20 * scale, -208 * scale)
    t = tree( [pen], 80 * scale, level, 0.1, [[ (45,0.69), (0,0.65), (-45,0.71) ]] )
    return t

def doit2(level, pen):
    pen.hideturtle()
    start(pen, -135 * scale, -130 * scale)
    t = tree( [pen], 120 * scale, level, 0.1, [[ (45,0.69), (-45,0.71) ]] )
    return t

def doit3(level, pen):
    pen.hideturtle()
    start(pen, 190 * scale, -90 * scale)
    t = tree( [pen], 100 * scale, level, 0.1, [[ (45,0.7), (0,0.72), (-45,0.65) ]] )
    return t

# Hier 3 Baumgeneratoren: (German)
# Here 3 tree generators:
def main():
    p = Turtle()
    p.ht()
    tracer(75,0)
    # Python3 has undobuffersize
    # u = doit1(6, Turtle(undobuffersize=1))
    # s = doit2(7, Turtle(undobuffersize=1))
    # t = doit3(5, Turtle(undobuffersize=1))
    u = doit1(6, Turtle())
    print('Have u')
    s = doit2(7, Turtle())
    print('Have s')
    t = doit3(5, Turtle())
    print('Have t')
    while True:
        done = 0
        for b in u,s,t:
            try:
                # b.__next__() # Python3, works in Trinket
                b.next()       # JC: for Skulpt
            except:
                done += 1
        if done == 3:
            break

    tracer(1,10)

main()

# Note: the forest thus generated is random.
</textarea>

<textarea id="mirror" class="hide">
"""turtledemo.two_canvases

Use TurtleScreen and RawTurtle to draw on two
distinct canvases in a separate window. The
new window must be separately closed in
addition to pressing the STOP button.
"""

from turtle import *

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

# use a scale to enlarge or shrink
scale = float(input('Please set a scale from 1 to 2 (default 1.8)') or '1.8')
print('scale = %f' % scale) # Python 2.6 formatting
# for the window above, best scale = 1.8

STEP = 150 * scale

def main():
    # two turtles
    p = Turtle()
    q = Turtle()

    p.color("red", (1, 0.85, 0.85))  # Python3 or Skulpt
    p.width(3)
    q.color("blue", (0.85, 0.85, 1)) # Python3 or Skulpt
    q.width(3)

    for t in p, q:
        t.shape("turtle")
        t.lt(36)

    q.lt(180)

    for t in p, q:
        t.begin_fill()
    for i in range(5):
        for t in p, q:
            t.fd(STEP)
            t.lt(72)  # JC: 5 * 72 = 360
    for t in p,q:
        t.end_fill()
        t.lt(54)
        t.pu()
        t.bk(STEP)

    return "EVENTLOOP"

main()

# Note: Here we have two turtles instaed of two canvases. Luckily they don't overlap.
</textarea>

<textarea id="hanoi" class="hide">
#!/usr/bin/env python3
"""       turtle-example-suite:

         tdemo_minimal_hanoi.py

A minimal 'Towers of Hanoi' animation:
A tower of 6 discs is transferred from the
left to the right peg.

An imho quite elegant and concise
implementation using a tower class, which
is derived from the built-in type list.

Discs are turtles with shape "square", but
stretched to rectangles by shapesize()
 ---------------------------------------
       To exit press STOP button
 ---------------------------------------
"""

from turtle import *

# Create a turtle screen
window = Screen()
window.setup(1000, 1000) # default (500, 500)
window.bgcolor("yellow")

# use a scale to enlarge or shrink
scale = float(input('Please set a scale from 1 to 2 (default 1.2)') or '1.2')
print('scale = %f' % scale) # Python 2.6 formatting
# for the window above, best scale = 1.2

# SHAPES.square   = [[ 10,-10],[10,10],[-10,10],[-10, -10]];
# [(10, -10). (10,10), (-10,10), (-10, -10)]
# shapesize(1.5, n*1.5, 2)
# SHAPES.circle = [[10,0],[9.51,3.09],[8.09,5.88],[5.88,8.09],[3.09,9.51],[0,10],[-3.09,9.51], [-5.88,8.09],[-8.09,5.88],[-9.51,3.09],[-10,0]]
def makeDisk(n):
    name = 'Disk' + str(n)
    # this is a rectangle
    # poly = [(15, -15 * n), (15,15 * n), (-15,15 * n), (-15, -15 * n)]
    # this is a rectangle with round corners
    poly = [(15,15 * n), (14.27, 15 * n + 4.64), (12.14, 15 * n + 8.82), (8.82, 15 * n + 12.14), (4.64, 15 * n + 14.27),
            (0, 15 * n + 15), (-4.64, 15 * n + 14.27), (-8.82, 15 * n + 12.14), (-12.14, 15 * n + 8.82), (-14.27, 15 * n + 4.64),
            (-15,15 * n), # end of semicircle, do straight part to another semicircle
            (-15, -15 * n + 15), (-14.27, -15 * n - 4.64), (-12.14, -15 * n - 8.82), (-8.82, -15 * n - 12.14), (-4.64, -15 * n - 14.27),
            (0, -15 * n - 15), (4.64, -15 * n - 14.27), (8.82, -15 * n - 12.14), (12.14, -15 * n - 8.82), (14.17, -15 * n - 4.64), (15, -15 * n)]
    # print(name, poly)
    window.register_shape(name, poly)
    return name

# make the Tower shape
def makeTower():
    """
    # JC: use this to make and adjust the tower shape,
    # then remove when the correct poly is printed.
    poly = []
    t = Turtle()
    t.lt(90)               # turn 90 degree for orientation
    t.backward(100 + 2.5)  # adjust horizontally for disks, with half-width 5/2
    poly.append(t.pos())
    t.fd(100)
    poly.append(t.pos())
    t.lt(90)
    t.fd(250)
    poly.append(t.pos())
    t.rt(90)
    t.fd(5)
    poly.append(t.pos())
    t.rt(90)
    t.fd(250)
    poly.append(t.pos())
    t.lt(90)
    t.fd(100)
    poly.append(t.pos())
    print('tower', poly)
    # ('tower', [(0.0, -102.5), (0.0, -2.5), (-250.0, -2.5), (-250.0, 2.5), (0.0, 2.5), (0.0, 102.5)])
    """
    poly = [(0.0, -102.5), (0.0, -2.5), (-250.0, -2.5), (-250.0, 2.5), (0.0, 2.5), (0.0, 102.5)]
    window.register_shape('tower', poly)

# put the tower at position (x,y)
def putTower(x, y):
    t = Turtle()
    t.shape("tower")
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.showturtle()
    return t    

class Disc(Turtle):
    def __init__(self, n):
        # Turtle.__init__(self, shape="square", visible=False)  # Python3
        Turtle.__init__(self)  # JC: this cannot be omitted
        # self.shape("square")          # first make a square
        # self.shapesize(1.5, n*1.5, 2) # square to rectangle  # Python3
        self.shape(makeDisk(n))         # JC: use this one
        self.ht()
        self.pu()
        self.fillcolor(n/6., 0, 1-n/6.)   # Python3 or Skulpt, with fractions
        self.st()

class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    # def __init__(self, x):
    #     "create an empty tower. x is x-position of peg"
    #     self.x = x
    # JC: replace by this one
    def setx(self, x):
        list.__init__(self)  # JC: this cannot be omitted for Tower(), can be omitted for Tower([])
        self.x = x
        self.stand = putTower(x, -170) # JC: adjust for tower base
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        # rint('push', d.pos())
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        # print('pop', d.pos())
        return d

def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n-1, with_, from_, to_)

def play():
    # onkey(None,"space")        # Python3
    window.onkey(None, "space")  # JC: disable SPACE bar
    clear()                      # JC: remove the writing by default turtle
    write("Tower of Hanoi with 6 disks",
              align="center", font=("Courier", 16, "bold"))
    try:
        hanoi(6, t1, t2, t3)
        clear()                  # JC: remove the writing by default turtle
        write("All 6 disks transferred!",
              align="center", font=("Courier", 16, "bold"))
    except Terminator:
        pass  # turtledemo user pressed STOP

def main():
    global t1, t2, t3
    ht(); penup(); goto(0, -225)   # writer turtle
    # Python3 constructors not working in Skulpt
    # t1 = Tower(-250)
    # t2 = Tower(0)
    # t3 = Tower(250)
    # JC: replace by these:
    makeTower()
    t1 = Tower(); t1.setx(-250 * scale)
    t2 = Tower(); t2.setx(0 * scale)
    t3 = Tower(); t3.setx(250 * scale)
    # make tower of 6 discs, from big to small
    for i in range(6,0,-1):
        t1.push(Disc(i))
    # prepare spartanic user interface ;-)
    write("Press spacebar to start game",
          align="center", font=("Courier", 16, "bold"))
    # onkey(play, "space")  # Python3
    # listen()              # Python3
    window.onkey(play, "space")  # JC
    window.listen()              # JC
    return "EVENTLOOP"

main()

# Note: must click the canvas before pressing SPACE bar, now disc has round corners.
# The three towers have a shape, but cannot find the equivalent of STOP key.
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
