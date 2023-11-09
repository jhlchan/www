---
title: Pyscript - Demo 10D
header-includes: |
    <style>
       body { min-width: 90% !important; }
    </style>
    <style>
       .hide {
          display: none;
       }
    </style>
include-after: |
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo10d.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo10d.html -->
---

# Pyscript - Python3 Help Turtle Demos by Trinket

<!-- Using Trinket for ease of debugging, before using Skulpt. -->

<!--
In Trinket or Skulpt:

import turtle

print(dir(turtle))
['Screen', 'Turtle', '__doc__', '__name__', '__package__', 'back', 'backward', 'begin_fill', 'bk', 'bye', 'circle', 'clear', 'clone', 'color', 'degrees', 'delay', 'distance', 'done', 'dot', 'down', 'end_fill', 'fd', 'fill', 'fillcolor', 'forward', 'getpen', 'getscreen', 'getturtle', 'goto_$rw$', 'heading', 'hideturtle', 'home', 'ht', 'isdown', 'isvisible', 'left', 'lt', 'mainloop', 'onclick', 'ondrag', 'onrelease', 'pd', 'pencolor', 'pendown', 'pensize', 'penup', 'pos', 'position', 'pu', 'radians', 'reset', 'right', 'rt', 'seth', 'setheading', 'setpos', 'setposition', 'setundobuffer', 'setx', 'sety', 'shape', 'showturtle', 'speed', 'st', 'stamp', 'towards', 'tracer', 'undo', 'undobufferentries', 'up', 'update', 'width', 'window_height', 'window_width', 'write', 'xcor', 'ycor']

print(dir(turtle.Screen))
['__init__', '__module__', 'addshape', 'bgcolor', 'bgpic', 'bye', 'clear', 'clearscreen', 'delay', 'done', 'exitonclick', 'getshapes', 'listen', 'mainloop', 'onclick', 'onkey', 'onscreenclick', 'ontimer', 'register_shape', 'reset', 'resetscreen', 'setup', 'setworldcoordinates', 'tracer', 'turtles', 'update', 'window_height', 'window_width']
 
print(dir(turtle.Turtle))
['__init__', '__module__', 'back', 'backward', 'begin_fill', 'bk', 'circle', 'clear', 'clone', 'color', 'degrees', 'delay', 'distance', 'done', 'dot', 'down', 'end_fill', 'fd', 'fill', 'fillcolor', 'forward', 'getpen', 'getscreen', 'getturtle', 'heading', 'hideturtle', 'home', 'ht', 'isdown', 'isvisible', 'left', 'lt', 'mainloop', 'onclick', 'ondrag', 'onrelease', 'pd', 'pencolor', 'pendown', 'pensize', 'penup', 'pos', 'position', 'pu', 'radians', 'reset', 'right', 'rt', 'seth', 'setheading', 'setpos', 'setposition', 'setundobuffer', 'setx', 'sety', 'shape', 'showturtle', 'speed', 'st', 'stamp', 'towards', 'tracer', 'undo', 'undobufferentries', 'up', 'update', 'width', 'window_height', 'window_width', 'write', 'xcor', 'ycor']


import inspect

print(dir(inspect))
['__doc__', '__name__', '__package__', 'getcallargs', 'isbuiltin', 'isfunction', 'ismethod']

no: getsource !

-->

## Tree

<!--
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
from turtle import Turtle, mainloop
# from time import perf_counter as clock  # JC: remove timing

scale = 0.6  # JC: apply scale to have whole view

def tree(plist, l, a, f):
    """ plist is list of pens
    l is length of branch
    a is half of the angle between 2 branches
    f is factor by which branch is shortened
    from level to level."""
    if l > 3:
        lst = []
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        for x in tree(lst, l*f, a, f):
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
    for x in t:
        pass

def main():
    # a=clock()       # JC: no timing
    maketree()
    # b=clock()       # JC: no timing
    # return "done: %.2f sec." % (b-a)  # JC: no primt

# JC: replace main() call
# if __name__ == "__main__":
#     msg = main()
#     print(msg)
#     mainloop()
main()

Note: version in Python3 Help has:
from turtle import Turtle, mainloop
from time import perf_counter as clock

showing timing, and uses mainloop().
-->
<iframe src="https://trinket.io/embed/python/11128719e1?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Round Dance

<!--
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

def stop():
    global running
    running = False

def main():
    global running
    # clearscreen()      # Python3
    # bgcolor("gray10")  # Python3
    window = Screen()    # JC
    window.clearscreen() # JC
    # window.bgcolor("gray10") # JC, leave white background
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
        p =get_shapepoly()
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
    setpos(0, -200)
    dancers = []
    for i in range(180):
        fd(7)
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
    cs = 1
    while running:
        ta = -4
        for dancer in dancers:
            dancer.fd(7)
            dancer.lt(2)
            # dancer.tilt(ta)  # Python3
            ta = -4 if ta > 0 else 2
        if cs < 180:
            right(4)
            # shapesize(cs)  # Python3
            cs *= 1.005
        update()
    return "DONE!"

# if __name__=='__main__':
#     print(main())
#     mainloop()
main()

Note: This "Round Dance" has many Python3 features: compound shape. shapesize, tilt, onkeypress, listen.
-->
<iframe src="https://trinket.io/embed/python/9222a31d06?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Color Mixer

<!--
# colormixer

from turtle import Screen, Turtle, mainloop

class ColorTurtle(Turtle):

    def __init__(self, x, y):
        Turtle.__init__(self)
        self.shape("turtle")
        # self.resizemode("user")   # Python3
        # self.shapesize(3,3,5)     # Python3
        self.pensize(10)
        self._color = [0,0,0]
        self.x = x
        self._color[x] = y
        self.color(self._color)
        self.speed(0)
        self.left(90)
        self.pu()
        self.goto(x,0)
        self.pd()
        self.sety(1)
        self.pu()
        self.sety(y)
        self.pencolor("gray25")
        self.ondrag(self.shift)

    def shift(self, x, y):
        self.sety(max(0,min(y,1)))
        self._color[self.x] = self.ycor()
        self.fillcolor(self._color)
        setbgcolor()

# JC: put global screen here
screen = Screen()
# screen.bgcolor("green")

def setbgcolor():
    # screen.bgcolor(red.ycor(), green.ycor(), blue.ycor())  # Python3 ?
    # JC: just a black background
    screen.bgcolor("#6214") # JC: need a method to convert percentages to RGBA value
    print(red.ycor(), green.ycor(), blue.ycor())
    # JC: at first (0.5, 0.5, 0.5), but background is black
    # JC: on click, all sliders move in sync, and all color ratios are the same

def main():
    global screen, red, green, blue
    # screen = Screen()  # Python3
    screen.delay(0)
    screen.setworldcoordinates(-1, -0.3, 3, 1.3)

    red = ColorTurtle(0, .5)
    green = ColorTurtle(1, .5)
    blue = ColorTurtle(2, .5)
    setbgcolor()

    writer = Turtle()
    writer.ht()
    writer.pu()
    writer.goto(1,1.15)
    writer.write("DRAG!",align="center",font=("Arial",30,("bold","italic")))
    return "EVENTLOOP"

# if __name__ == "__main__":
#     msg = main()
#     print(msg)``
#     mainloop()
main()

Note: Python3 has bgcolor(red, blue, green),
and ondrag works for Class instances.
-->

<iframe src="https://trinket.io/embed/python/2f9abecf42?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Byte Design

<!--
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

from turtle import Turtle, mainloop
# from time import perf_counter as clock  # JC: remove timing

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
    # at = clock()     # JC: no timing
    # t.design(t.position(), 2)      # Python3
    t.design(t.position(), 1.6)      # JC: use scale 1.8 for full view
    # et = clock()     # JC: no timing
    # return "runtime: %.2f sec." % (et-at)
    return "Done!"

# if __name__ == '__main__':
#     msg = main()
#     print(msg)
#     mainloop()
main()

Note: Except for timing, this one works, and scale = 1.6 gives full view in Trinket.
-->

<iframe src="https://trinket.io/embed/python/c526dde1b6?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Chaos

<!--
# File: tdemo_chaos.py
# Author: Gregor Lingl
# Date: 2009-06-24

# A demonstration of chaos

from turtle import *

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

window = Screen()   # JC: use global window

def main():
    # reset()   # JC: comment this out to have something appearing
    # setworldcoordinates(-1.0,-0.1, N+1, 1.1)  # Python3
    window.setworldcoordinates(-1.0,-0.1, N+1, 1.1) # JC: change this
    window.bgcolor('yellow')                        # JC: add this
    speed(0)
    pensize(2)  # JC: add this, default pensize(1) gives tiny dots
    hideturtle()
    coosys()
    plot(f, 0.35, "blue")
    plot(g, 0.35, "green")
    plot(h, 0.35, "red")
    # Now zoom in:
    for s in range(100):
        # setworldcoordinates(0.5*s,-0.1, N+1, 1.1)   # Python3
        window.setworldcoordinates(0.5*s,-0.1, N+1, 1.1) # JC: change this
        # but now any setworldcoordinates will clear the plots!
    return "Done!"

# if __name__ == "__main__":
#     main()
#     mainloop()
main()



Note: no error message, but nothing appears if there is reset().
With reset() commented out, sometimes it gives chaos graph as in Python3 Help Turtle demo.
Otherwise, it is just a collection of tiny dots, no chaos graph.
Final image still disappears even with mainloop().
Definitely cannot detect the "Now zoom in" part in Trinket.
-->

<iframe src="https://trinket.io/embed/python/2d7414dfce?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


## Clock

<!--
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
    fd(laenge*1.15)
    rt(90)
    fd(spitze/2.0)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze/2.0)

window = Screen()    # JC: global window

def make_hand_shape(name, laenge, spitze):
    reset()
    jump(-laenge*0.15)
    # begin_poly()    # Python3
    hand(laenge, spitze)
    # end_poly()      # Python3
    # hand_form = get_poly()  # Python3
    hand_form = [(0,0), (1,1)]
    # register_shape(name, hand_form) # Python3
    window.register_shape(name, hand_form) # JC

def clockface(radius):
    reset()
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
    make_hand_shape("second_hand", 125, 25)
    make_hand_shape("minute_hand",  130, 25)
    make_hand_shape("hour_hand", 90, 25)
    clockface(160)
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
    #writer.mode("logo")
    writer.ht()
    writer.pu()
    writer.bk(85)

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
    try:
        tracer(False)  # Terminator can occur here
        writer.clear()
        writer.home()
        writer.forward(65)
        writer.write(wochentag(t),
                     align="center", font=("Courier", 14, "bold"))
        writer.back(150)
        writer.write(datum(t),
                     align="center", font=("Courier", 14, "bold"))
        writer.forward(85)
        second_hand.setheading(6*sekunde)  # or here
        minute_hand.setheading(6*minute)
        hour_hand.setheading(30*stunde)
        tracer(True)
        # ontimer(tick, 100)   # Python3
    except Terminator:
        pass  # turtledemo user pressed STOP

def main():
    tracer(False)
    setup()
    tracer(True)
    tick()
    return "EVENTLOOP"

# if __name__ == "__main__":
#     mode("logo")
#     msg = main()
#     print(msg)
#     mainloop()
main()

Note: The hand_form is not working in Skulpt.
Have a clock showing eventually, with date, but no hands.
The format of date showing is different from Python3 Help Turtle Demo.
-->

<iframe src="https://trinket.io/embed/python/41bf5f2fea?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


## Sorting

<!--
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


class Block(Turtle):

    def __init__(self, size):
        self.size = size
        # Turtle.__init__(self, shape="square", visible=False)  # Python3
        self = Turtle()   # JC: add this
        self.shape("square")
        self.hideturtle()
        self.pu()
        # self.shapesize(size * 1.5, 1.5, 2) # square to rectangle  # Python3
        self.fillcolor("black")
        self.st()

    def glow(self):
        self.fillcolor("red")

    def unglow(self):
        self.fillcolor("black")

    def __repr__(self):
        return "Block size: {0}".format(self.size)


class Shelf(list):

    def __init__(self, y):
        "create a shelf. y is y-position of first block"
        self.y = y
        self.x = -150

    def push(self, d):
        # width, _, _ = d.shapesize()   # Python3
        width = d.size                  # JC: use this
        # align blocks by the bottom edge
        y_offset = width / 2 * 20
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
        width, _, _ = b.shapesize()
        # align blocks by the bottom edge
        y_offset = width / 2 * 20
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
    s = Shelf([])        # JC: to avoid 'int' object is not iterable
    vals = (4, 2, 8, 9, 1, 5, 10, 3, 7, 6)
    for i in vals:
        s.push(Block(i))

def disable_keys():
    onkey(None, "s")
    onkey(None, "i")
    onkey(None, "q")
    onkey(None, "r")

def enable_keys():
    onkey(start_isort, "i")
    onkey(start_ssort, "s")
    onkey(start_qsort, "q")
    onkey(randomize, "r")
    onkey(bye, "space")

def zmain():
    getscreen().clearscreen()
    ht(); penup()
    init_shelf()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()
    listen()
    return "EVENTLOOP"

instructions1 = "press i for insertion sort, s for selection sort, q for quicksort"
instructions2 = "spacebar to quit, r to randomize"

# if __name__=="__main__":
#     msg = main()
#     mainloop()
# zmain()  # JC: not working

# JC a dummy turtle
def main():
    getscreen().clearscreen()
    pencolor('green')
    forward(100)
    dot(15)
    
main()


Note: have trouble calling the constructor of Shelf(-200) in Python 2.6
Since this one cannot start properly, remove "?start=result" in iframe URL.
No use, need to comment out the iframe or the main().
-->

<iframe src="https://trinket.io/embed/python/8afd0eeed8?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


## Paint

<!--
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

def switchupdown(x=0, y=0):
    # if pen()["pendown"]:  # Python3
    if isdown():            # JC: use this
        end_fill()
        up()
    else:
        down()
        begin_fill()

def changecolor(x=0, y=0):
    global colors
    colors = colors[1:]+colors[:1]
    color(colors[0])

window = Screen()   # JC: global window
colors=["red", "green", "blue", "yellow"]  # JC: global colors

def main():
    global colors
    shape("circle")
    # resizemode("user")   # Python3
    # shapesize(.5)        # Python3
    width(3)
    # colors=["red", "green", "blue", "yellow"] # Python3
    color(colors[0])
    switchupdown()
    # onscreenclick(goto,1)             # Python3
    # onscreenclick(changecolor,2)      # Python3
    # onscreenclick(switchupdown,3)     # Python3
    window.onscreenclick(goto,1)
    window.onscreenclick(changecolor,2)
    window.onscreenclick(switchupdown,3)
    return "EVENTLOOP"

# if __name__ == "__main__":
#     msg = main()
#     print(msg)
#     mainloop()
main()

Note: Only a red dot at center.
Looks like Skulpt canvas cannot detect any mouse click/event.
In the Python3 Help Turtle Demo, right-click cycles color, but cannot simulate mouse to switch up/down. Also, there is no color filling.
-->

<iframe src="https://trinket.io/embed/python/a7ed44fece?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


## Lindenmayer

<!--
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


def main():
    ################################
    # Example 1: Snake kolam
    ################################


    def r():
        right(45)

    def l():
        left(45)

    def f():
        forward(7.5)

    snake_rules = {"-":r, "+":l, "f":f, "b":"f+f+f--f--f+f+f"}
    snake_replacementRules = {"b": "b+f+b--f--b+f+b"}
    snake_start = "b--f--b--f"

    drawing = replace(snake_start, snake_replacementRules, 3)

    reset()
    speed(3)
    tracer(1,0)
    ht()
    up()
    backward(195)
    down()
    draw(drawing, snake_rules)

    from time import sleep
    sleep(3)

    ################################
    # Example 2: Anklets of Krishna
    ################################

    def A():
        color("red")
        circle(10,90)

    def B():
        from math import sqrt
        color("black")
        l = 5/sqrt(2)
        forward(l)
        circle(l, 270)
        forward(l)

    def F():
        color("green")
        forward(10)

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
    return "Done!"

# if __name__=='__main__':
#     msg = main()
#     print(msg)
#     mainloop()
main()

Note: just works!
First image in full view, second image full view needs a bit scaling.
-->

<iframe src="https://trinket.io/embed/python/3c402420b2?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


## Penrose

<!--
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
from math import cos, pi
# from time import perf_counter as clock, sleep  # Python3
from time import sleep                           # JC

f = (5**0.5-1)/2.0   # (sqrt(5)-1)/2 -- golden ratio
d = 2 * cos(3*pi/10)

def kite(l):
    fl = f * l
    lt(36)
    fd(l)
    rt(108)
    fd(fl)
    rt(36)
    fd(fl)
    rt(108)
    fd(l)
    rt(144)

def dart(l):
    fl = f * l
    lt(36)
    fd(l)
    rt(144)
    fd(fl)
    lt(36)
    fd(fl)
    rt(144)
    fd(l)
    rt(144)

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
    l = l * f**n
    # shapesize(l/100.0, l/100.0, th)  # Python3
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
        stamp()

def sun(l, n):
    for i in range(5):
        inflatekite(l, n)
        lt(72)

def star(l,n):
    for i in range(5):
        inflatedart(l, n)
        lt(72)

window = Screen()   # JC: global window

def makeshapes():
    tracer(0)
    # begin_poly()   # Python3
    kite(100)
    # end_poly()     # Python3
    # register_shape("kite", get_poly())  # Python3
    window.register_shape("kite", [(1,0), (0,1)]) # JC: change
    # begin_poly()   # Python3
    dart(100)
    # end_poly()     # Python3
    # register_shape("dart", get_poly())  # Python3
    window.register_shape("kite", [(0,0), (1,1)]) # JC: change
    tracer(1)

def start():
    reset()
    ht()
    pu()
    makeshapes()
    # resizemode("user")   # Python3

def test(l=200, n=4, fun=sun, startpos=(0,0), th=2):
    global tiledict
    goto(startpos)
    setheading(0)
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
        # a = clock()       # Python3 timing
        test(300, i, fun)
        # b = clock()       # Python3 timing
        # JC: remove timing and sleep
        # t = b - a
        # if t < 2:
        #     sleep(2 - t)

def main():
    #title("Penrose-tiling with kites and darts.")
    # mode("logo")          # Python3
    # bgcolor(0.3, 0.3, 0)  # Python3
    window.bgcolor('pink')   # JC: use this
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

# if __name__ == "__main__":
#     msg = main()
#     mainloop()
main()

Note: cannot make the shapes kite and dart propertly, so just dot-shapes.
-->

<iframe src="https://trinket.io/embed/python/14ecbe3073?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


## Peace

<!--
#!/usr/bin/env python3
"""       turtle-example-suite:

              tdemo_peace.py

A simple drawing suitable as a beginner's
programming example. Aside from the
peacecolors assignment and the for loop,
it only uses turtle commands.
"""

from turtle import *

def main():
    peacecolors = ("red3",  "orange", "yellow",
                   "seagreen4", "orchid4",
                   "royalblue1", "dodgerblue4")

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

# if __name__ == "__main__":
#     main()
#     mainloop()
main()

Note: just works!
-->

<iframe src="https://trinket.io/embed/python/93b5b4f3e1?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


## Rosette

<!--
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
from turtle import Screen, Turtle, mainloop
# from time import perf_counter as clock, sleep   # Python3 timing
from time import sleep                            # JC

def mn_eck(p, ne,sz):
    turtlelist = [p]
    #create ne-1 additional turtles
    for i in range(1,ne):
        q = p.clone()
        q.rt(360.0/ne)
        turtlelist.append(q)
        p = q
    for i in range(ne):
        c = abs(ne/2.0-i)/(ne*.7)
        # let those ne turtles make a step
        # in parallel:
        for t in turtlelist:
            t.rt(360./ne)
            t.pencolor(1-c,0,c) # JC: Skulpt uses color names or hex, so this is black
            t.fd(sz)

def main():
    s = Screen()
    # s.bgcolor("black")  # JC: change this to show the pen, always black
    s.bgcolor("yellow")
    p=Turtle()
    p.speed(0)
    p.hideturtle()
    p.pencolor("red")
    p.pensize(3)

    s.tracer(36,0)

    # at = clock()      # Python3 timing
    mn_eck(p, 36, 19)
    # et = clock()      # Python3 timing
    # z1 = et-at        # JC: remove timing

    sleep(1)

    # at = clock()      # Python3 timing
    while any(t.undobufferentries() for t in s.turtles()):
        for t in s.turtles():
            t.undo()
    # et = clock()      # Python3 timing
    # return "runtime: %.3f sec" % (z1+et-at)  # JC: no timing to report


# if __name__ == '__main__':
#     msg = main()
#     print(msg)
#     mainloop()
main()

Note: This uses pencolor(red, blue, green), but Skulpt colors are strings or hex.
-->

<iframe src="https://trinket.io/embed/python/c12c7966f7?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


## Nim

<!--
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

SCREENWIDTH = 640
SCREENHEIGHT = 480

MINSTICKS = 7
MAXSTICKS = 31

HUNIT = SCREENHEIGHT // 12
WUNIT = SCREENWIDTH // ((MAXSTICKS // 5) * 11 + (MAXSTICKS % 5) * 2)

SCOLOR = (63, 63, 31)
HCOLOR = (255, 204, 204)
COLOR = (204, 204, 255)

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


class Stick(turtle.Turtle):
    def __init__(self, row, col, game):
        # turtle.Turtle.__init__(self, visible=False)  # Python3
        turtle.Turtle.__init__(self)       # JC
        self.hideturtle()                  # JC
        self.row = row
        self.col = col
        self.game = game
        x, y = self.coords(row, col)
        self.shape("square")
        # self.shapesize(HUNIT/10.0, WUNIT/20.0)  # Python3 
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
        self.screen.bgcolor((240, 240, 255))
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
        self.model = NimModel(self)
        self.view = NimView(self)
        self.controller = NimController(self)


def main():
    mainscreen = turtle.Screen()
    # mainscreen.mode("standard")   # Python3
    mainscreen.setup(SCREENWIDTH, SCREENHEIGHT)
    nim = Nim(mainscreen)
    return "EVENTLOOP"

# if __name__ == "__main__":
#     main()
#     turtle.mainloop()
main()

Note: This one shows short bars, Python3 Help Turtle Demo shows thin bars.
Press Space Bar has no action here, but mouse click seems to have action.
-->

<iframe src="https://trinket.io/embed/python/d8f5d018ec?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## YinYang

<!--
#!/usr/bin/env python3
"""       turtle-example-suite:

            tdemo_yinyang.py

Another drawing suitable as a beginner's
programming example.

The small circles are drawn by the circle
command.

"""

from turtle import *

def yin(radius, color1, color2):
    width(3)
    # color("black", color1)  # Python3
    color("black"); fillcolor(color1)    # JC
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
    # color(color1, color2)   @ Python3
    color(color1); fillcolor(color2)    # JC
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
    yin(200, "black", "white")
    yin(200, "white", "black")
    ht()
    return "Done!"

# if __name__ == '__main__':
#     main()
#     mainloop()
main()

Note: need to split Python3 color(pen, fill) into color(pen); fillcolor(fill).
-->

<iframe src="https://trinket.io/embed/python/986bd8f363?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


## Fractal Curves
<!--
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
# from time import sleep, perf_counter as clock  # Python3 timing
from time import sleep    # JC

# class CurvesTurtle(Pen):   # Python3 original
class CurvesTurtle(Turtle): # JC
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

    size = 6
    ft.setpos(-33*size, -32*size)
    ft.pd()

    # ta=clock()     # Python3 timing
    ft.fillcolor("red")
    ft.begin_fill()
    ft.fd(size)

    ft.hilbert(size, 6, 1)

    # frame
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
    ft.end_fill()
    # tb=clock()    # Python3 timing
    # JC: remove timing
    # res =  "Hilbert: %.2fsec. " % (tb-ta)

    sleep(3)

    ft.reset()
    ft.speed(0)
    ft.ht()
    ft.getscreen().tracer(1,0)

    # ta=clock()    # Python3 timing
    # ft.color("black", "blue")  # Python3 color
    ft.color("black"); ft.fillcolor("blue")  # JC
    ft.begin_fill()
    ft.fractalgon(3, 250, 4, 1)
    ft.end_fill()
    ft.begin_fill()
    ft.color("red")
    ft.fractalgon(3, 200, 4, -1)
    ft.end_fill()
    # tb=clock()   # Python3 timing
    # JC: remove timing
    # res +=  "Koch: %.2fsec." % (tb-ta)
    # return res

# if __name__  == '__main__':
#     msg = main()
#     print(msg)
#     mainloop()
main()

Note: Timing in Python3 is removed.
Fractal curves may need scaling for full view.
-->

<iframe src="https://trinket.io/embed/python/262b5df015?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


## Planet and Moon
<!--
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
# from turtle import Shape, Turtle, mainloop, Vec2D as Vec  # Python3
from turtle import Turtle, mainloop   # JC: no Shape, no Vec2D

G = 8

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
    def __init__(self, m, x, v, gravSys, shape):
        # Turtle.__init__(self, shape=shape) # Python3
        Turtle.__init__(self)  # JC
        self.shape = shape     # JC
        self.penup()
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
        self.v = self.v + int(0.5*dt)*self.a  # JC: integer acceleration
    def acc(self):
        # a = Vec(0,0)   # Python3
        a = [0,0]        # JC
        for planet in self.gravSys.planets:
            if planet != self:
                # v = planet.pos()-self.pos()   # Python3
                x1, y1 = planet.pos()           # JC
                x2, y2 = self.pos()             # JC
                v = [x1 - x2, y1 - y2]          # JC
                # a += (G*planet.m/abs(v)**3)*v  # Python3
                # a = a + (G*planet.m/abs(v)**3)*v  # JC: even this says 'a' undefined

        return a
    def step(self):
        dt = self.gravSys.dt
        # self.setpos(self.pos() + dt*self.v)    # Python3
        self.setpos(self.pos())  # JC: remove velocity v, not a tuple
        if self.gravSys.planets.index(self) != 0:
            self.setheading(self.towards(self.gravSys.planets[0]))
        self.a = self.acc()
        # self.v = self.v + dt*self.a  # Python3
        self.v = self.v + int(dt) * self.a  # JC

## create compound yellow/blue turtleshape for planets

def main():
    s = Turtle()
    s.reset()
    s.getscreen().tracer(0,0)
    s.ht()
    s.pu()
    s.fd(6)
    s.lt(90)
    # s.begin_poly()   # Python3
    s.circle(6, 180)
    # s.end_poly()     # Python3
    # m1 = s.get_poly()  # no poly
    # s.begin_poly()   # Python3
    s.circle(6,180)
    # s.end_poly()     @ # Python3
    # m2 = s.get_poly()  # no poly

    # Python3 has Shape
    # planetshape = Shape("compound")
    # planetshape.addcomponent(m1,"orange")
    # planetshape.addcomponent(m2,"blue")
    planetshape = [(0,0), (0,1), (1,1), (1,0), (0,0)]  # JC: planet = square
    s.getscreen().register_shape("planet", planetshape)
    s.getscreen().tracer(1,0)

    ## setup gravitational system
    gs = GravSys()
    # sun = Star(1000000, Vec(0,0), Vec(0,-2.5), gs, "circle")  # Python3
    sun = Star(1000000, [0,0], [0,-2.5], gs, "circle") 
    sun.color("yellow")
    # sun.shapesize(1.8)  # Python3
    sun.pu()
    # earth = Star(12500, Vec(210,0), Vec(0,195), gs, "planet")  # Python3
    earth = Star(12500, [210,0], [0,195], gs, "planet")  # JC
    earth.pencolor("green")
    # earth.shapesize(0.8) # Python3
    # moon = Star(1, Vec(220,0), Vec(0,295), gs, "planet")  # Python3
    moon = Star(1, [220,0], [0,295], gs, "planet")  # JC
    moon.pencolor("blue")
    # moon.shapesize(0.5)  # Python3
    gs.init()
    gs.start()
    return "Done!"

# if __name__ == '__main__':
#     main()
#     mainloop()
main()

Note: Just some dots (Sun or Earth or Moon) fleeting by, as velocities and accerations are truncated badly.
-->

<iframe src="https://trinket.io/embed/python/25d3ce7f9e?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


## Forest
<!--
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
# from turtle import Turtle, colormode, tracer, mainloop  # Python3
from turtle import Turtle, tracer, mainloop
from random import randrange
# from time import perf_counter as clock   # Python3 timing

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
    # benutzt Liste von turtles und Liste von Zweiglisten,
    # fuer jede turtle eine!
    if level > 0:
        lst = []
        brs = []
        for t, branchlist in list(zip(tlist,branchlists)):
            t.pensize( size * widthfactor )
            t.pencolor( 255 - (180 - 11 * level + symRandom(15)),
                        180 - 11 * level + symRandom(15),
                        0 )
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
    start(pen, 20, -208)
    t = tree( [pen], 80, level, 0.1, [[ (45,0.69), (0,0.65), (-45,0.71) ]] )
    return t

def doit2(level, pen):
    pen.hideturtle()
    start(pen, -135, -130)
    t = tree( [pen], 120, level, 0.1, [[ (45,0.69), (-45,0.71) ]] )
    return t

def doit3(level, pen):
    pen.hideturtle()
    start(pen, 190, -90)
    t = tree( [pen], 100, level, 0.1, [[ (45,0.7), (0,0.72), (-45,0.65) ]] )
    return t

# Hier 3 Baumgeneratoren:
def main():
    p = Turtle()
    p.ht()
    tracer(75,0)
    # Python3 has undobuffersize
    # u = doit1(6, Turtle(undobuffersize=1))
    # s = doit2(7, Turtle(undobuffersize=1))
    # t = doit3(5, Turtle(undobuffersize=1))
    u = doit1(6, Turtle())
    s = doit2(7, Turtle())
    t = doit3(5, Turtle())
    # a = clock()    # Python3 timing
    while True:
        done = 0
        for b in u,s,t:
            try:
                b.__next__()
            except:
                done += 1
        if done == 3:
            break

    tracer(1,10)
    # b = clock()   # Python3 timing
    # return "runtime: %.2f sec." % (b-a)  # no timing to return

# if __name__ == '__main__':
#     main()
#     mainloop()
main()

Note: Here undobuffersize is removed. May need scale for full view.
-->

<iframe src="https://trinket.io/embed/python/c6a5d6c7c3?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Two Turtles
<!--
"""turtledemo.two_canvases

Use TurtleScreen and RawTurtle to draw on two
distinct canvases in a separate window. The
new window must be separately closed in
addition to pressing the STOP button.
"""

# from turtle import TurtleScreen, RawTurtle, TK   # Python3
from turtle import Screen, Turtle                  # JC

def main():
    # Python3 has TK
    # root = TK.Tk()
    # cv1 = TK.Canvas(root, width=300, height=200, bg="#ddffff")
    # cv2 = TK.Canvas(root, width=300, height=200, bg="#ffeeee")
    # cv1.pack()
    # cv2.pack()

    # JC: cannot have two screens
    # s1 = TurtleScreen(cv1)
    # s1.bgcolor(0.85, 0.85, 1)
    # s2 = TurtleScreen(cv2)
    # s2.bgcolor(1, 0.85, 0.85)
    s1 = Screen()                  # JC
    s1.bgcolor('yellow')           # JC

    # Python3 has RawTurtle
    # p = RawTurtle(s1)
    # q = RawTurtle(s2)
    p = Turtle()                   # JC
    q = Turtle()                   # JC another one

    # p.color("red", (1, 0.85, 0.85))  # Python3
    p.color("red")
    p.fillcolor('pink')
    p.width(3)
    # q.color("blue", (0.85, 0.85, 1)) # Python3
    q.color("blue")
    q.fillcolor('lime')
    q.width(3)

    for t in p,q:
        t.shape("turtle")
        t.lt(36)

    q.lt(180)

    for t in p, q:
        t.begin_fill()
    for i in range(5):
        for t in p, q:
            t.fd(50)
            t.lt(72)
    for t in p,q:
        t.end_fill()
        t.lt(54)
        t.pu()
        t.bk(50)

    return "EVENTLOOP"


# if __name__ == '__main__':
#     main()
#     TK.mainloop()  # keep window open until user closes it
main()

Note: Here we have two turtles instaed of two canvases. Luckily they don't overlap.
-->

<iframe src="https://trinket.io/embed/python/e4caf87867?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


## Minimal Hanoi
<!--
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

class Disc(Turtle):
    def __init__(self, n):
        # Turtle.__init__(self, shape="square", visible=False)  # Python3
        Turtle.__init__(self)
        self.shape("square")
        self.hideturtle()
        self.pu()
        # self.shapesize(1.5, n*1.5, 2) # square to rectangle  # Python3
        # self.fillcolor(n/6., 0, 1-n/6.)   # Python3
        self.fillcolor('yellow')
        self.st()

class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self, x):
        "create an empty tower. x is x-position of peg"
        self.x = x
    # JC: add this one
    def setx(self, x):
        self.x = x
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n-1, with_, from_, to_)

window = Screen()  # JC: globasl window

def play():
    # onkey(None,"space")    # Python3
    # clear()                # Python3
    window.onkey(None,"space")  # JC
    window.clear()              # JC
    try:
        hanoi(6, t1, t2, t3)
        write("press STOP button to exit",
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
    t1 = Tower([]); t1.setx(-250)
    t2 = Tower([]); t2.setx(0)
    t3 = Tower([]); t1.setx(250)
    # make tower of 6 discs
    for i in range(6,0,-1):
        t1.push(Disc(i))
    # prepare spartanic user interface ;-)
    write("press spacebar to start game",
          align="center", font=("Courier", 16, "bold"))
    # onkey(play, "space")  # Python3
    # listen()              # Python3
    window.onkey(play, "space")  # JC
    window.listen()              # JC
    return "EVENTLOOP"

# if __name__=="__main__":
#     msg = main()
#     print(msg)
#     mainloop()
main()

Note: Due to Tower(list) constructor, this is not really working, just some yellow blocks fleeting.
Python3 Help Turtle Demo has fleeting blocks stack up as first pile, and instruction: Press spacebar to start game.
-->

<iframe src="https://trinket.io/embed/python/e87a25e9c8?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Extra 1
<!--
import pygal

# Our data is a list of series.
# Each series is a list with a label and a list of data points
data = [["Firefox", [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1]],
        ["Chrome",  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3]],
        ["IE",      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1]],
        ["Others",  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5]]]


# Make a Pygal chart
stackedline_chart = pygal.StackedLine(fill=True)
stackedline_chart.title = "Browser usage evolution (in %)"
stackedline_chart.x_labels = map(str, range(2002, 2013))

# For each series in our data, add label and data points
for label, data_points in data:
    stackedline_chart.add(label, data_points)

# Render the chart
stackedline_chart.render()

# Example modified from the pygal.org documentation
-->

<iframe src="https://trinket.io/embed/python/0bafac9081?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


## Extra 2
<!--
# Spirals
import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor('black')

def drawCircles(t, size, n, d):
    for _ in range(n):
        t.circle(size)
        size = size - d

def drawSpecial(t, size, n, d, repeat):
  for i in range(repeat):
    drawCircles(t, size, n, d)
    t.right(360/repeat)


Albert = turtle.Turtle()
Albert.speed(0)
Albert.color('white')
rotate = int(360)
drawSpecial(Albert, 100, 10, 4, 10)

Steve = turtle.Turtle()
Steve.speed(0)
Steve.color('yellow')
rotate = int(90)
drawSpecial(Steve, 100, 4, 10, 10)

Barry = turtle.Turtle()
Barry.speed(0)
Barry.color('blue')
rotate = int(80)
drawSpecial(Barry, 100, 4, 5, 10)

Terry = turtle.Turtle()
Terry.speed(0)
Terry.color('orange')
rotate = int(90)
drawSpecial(Terry, 100, 4, 19, 10)

Will = turtle.Turtle()
Will.speed(0)
Will.color('pink')
rotate = int(90)
drawSpecial(Will, 100, 4, 20, 10)

-->

<iframe src="https://trinket.io/embed/python/cfd41616fc?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


## Spare

<!--
This one has the Logo code:
shapes.py

# This is a custom module we've made.  
# Modules are files full of code that you can import into your programs.
# This one teaches our turtle to draw various shapes.

import turtle

def draw_circle(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(size)
  turtle.end_fill()
    
def draw_triangle(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range (3):
    turtle.forward(size*3)
    turtle.left(120)
  turtle.end_fill()
  turtle.setheading(0)
    
def draw_square(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range (4):
    turtle.forward(size*2)
    turtle.left(90)
  turtle.end_fill()
  turtle.setheading(0)
  
def draw_star(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.right(144)
  for i in range(5):
    turtle.forward(size*2)
    turtle.right(144)
    turtle.forward(size*2)
  turtle.end_fill()
  turtle.setheading(0)

main.py

# You can edit this code and run it right here in the browser!
# First we'll import some turtles and shapes: 
from turtle import *
from shapes import *

# Create a turtle named Tommy:
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(7)

# Draw three circles:
draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)

# Write a little message:
tommy.penup()
tommy.goto(0,-50)
tommy.color("black")
tommy.write("Teach With Code!", None, "center", "16pt bold")
tommy.goto(0,-80)

# Try changing draw_circle to draw_square, draw_triangle, or draw_star

new:
python/abca1f6721
python/ebac891477
python/0346ed4f97
python/ed611b92a7
python/9adc2ce435
python/ce9686aab9
python/688d642ecc

python/790c74fcc9
python/14ecbe3073
python/d2f483d970
python/b24989033a
python/8d1bf88ecc
python/7415d68e62
python/447cc14376
python/e55870fa79
python/68a99324d0
python/c237f12bc6
python/736255b9f4
python/d2f483d970
python/8951626abc
python/7ef558297b
python/d765679079
python/ce9686aab9
python/a7ed44fece
python/5295adff4f
python/ac0524d22e
python/63450952ba
-->
<iframe src="https://trinket.io/embed/python/3d8d7ce66b?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

<!-- Important: Always reload the URL (not just reload the page) to have individual Trinkets working. -->

---

<!-- pandoc -s demo10d.md -o demo10d.html -->
