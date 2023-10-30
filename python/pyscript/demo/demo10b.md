---
title: Pyscript - Demo 10B
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
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo10b.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo10b.html -->
---

# Pyscript - Turtle Graphics by Trinket


## Hypotrochoid
A __[hypotrochoid](https://en.wikipedia.org/wiki/Hypotrochoid)__ is a type of curve traced by a point attached to a circle of radius $r$ rolling around the _inside_ of a fixed circle of radius $R$, where the point is a distance $d$ from the center of the interior circle.

The parametric equation for a hypotrochoid is:
<!-- $$ ... $$ is a math block, centralized, $ ... $ is inline math --> 
$$
(x(\theta),\ y(\theta)) = (\alpha\ cos\theta\ +\ d\ cos(\beta\theta),\ \alpha\ sin\theta\ -\ d\ sin(\beta\theta))
$$
where $\alpha = (R - r)$, and $\beta = (R - r)/r$.

<!--
# Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/
import turtle
from math import cos,sin
from time import sleep

window = turtle.Screen()
window.bgcolor("#FFFFFF")

spirograph = turtle.Turtle()
spirograph.hideturtle()
spirograph.tracer(0)
spirograph.speed(0)
spirograph.pensize(2)

pen = turtle.Turtle()
pen.hideturtle()
pen.tracer(0)
pen.speed(0)
pen.pensize(3)
pen.color("#AA00AA")

R = 125
r = 85
d = 125
angle = 0

pen.penup()
pen.goto(R - r + d,0)
pen.pendown()

theta = 0.2
steps = 8 * int(6*3.14/theta)

for t in range(0,steps):
    spirograph.clear()
    spirograph.penup()
    spirograph.setheading(0)
    spirograph.goto(0,-R)
    spirograph.color("#999999")
    spirograph.pendown()
    spirograph.circle(R)
    angle += theta
    
    a, b = (R - r), (R - r)/r

    x = a * cos(angle)
    y = a * sin(angle)
    spirograph.penup()
    spirograph.goto(x,y-r)
    spirograph.color("#222222")
    spirograph.pendown()
    spirograph.circle(r)
    spirograph.penup()
    spirograph.goto(x,y)
    spirograph.dot(5)
    
    x = a * cos(angle) + d * cos(b * angle)
    y = a * sin(angle) - d * sin(b * angle)
    spirograph.pendown()
    spirograph.goto(x,y)
    spirograph.dot(5)

    pen.goto(spirograph.pos())

    spirograph.getscreen().update() 
    sleep(0.05)

sleep(0.5)
# Hide Spirograph
spirograph.clear()
spirograph.getscreen().update()

https://trinket.io/embed/python/6fe6e6d51b?start=result
https://trinket.io/embed/python3/9456173d6d?start=result
Turtle Graphics is only available in a Python2 trinket, not a Python3 trinket.
-->
<iframe src="https://trinket.io/embed/python/6fe6e6d51b?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

<!--
# Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/
import turtle
from math import cos,sin
from time import sleep

window = turtle.Screen()
window.bgcolor("#FFFFFF")

spirograph = turtle.Turtle()
spirograph.hideturtle()
spirograph.tracer(0)
spirograph.speed(0)
spirograph.pensize(2)

pen = turtle.Turtle()
pen.hideturtle()
pen.tracer(0)
pen.speed(0)
pen.pensize(3)
pen.color("#AA00AA")

R = 125
r = 75
d = 125
angle = 0

pen.penup()
pen.goto(R - r + d,0)
pen.pendown()

theta = 0.2
steps = int(6*3.14/theta)

for t in range(0,steps):
    spirograph.clear()
    spirograph.penup()
    spirograph.setheading(0)
    spirograph.goto(0,-R)
    spirograph.color("#999999")
    spirograph.pendown()
    spirograph.circle(R)
    angle += theta
    
    a, b = (R - r), (R - r)/r

    x = a * cos(angle)
    y = a * sin(angle)
    spirograph.penup()
    spirograph.goto(x,y-r)
    spirograph.color("#222222")
    spirograph.pendown()
    spirograph.circle(r)
    spirograph.penup()
    spirograph.goto(x,y)
    spirograph.dot(5)
    
    x = a * cos(angle) + d * cos(b * angle)
    y = a * sin(angle) - d * sin(b * angle)
    spirograph.pendown()
    spirograph.goto(x,y)
    spirograph.dot(5)

    pen.goto(spirograph.pos())    

    spirograph.getscreen().update() 
    sleep(0.05)

sleep(0.5)
# Hide Spirograph
spirograph.clear()
spirograph.getscreen().update()

https://trinket.io/embed/python/8581c30000?start=result
https://trinket.io/embed/python3/9456173d6d?start=result
-->
<iframe src="https://trinket.io/embed/python/8581c30000?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Hypocycloid
Find out the properties of an __[hypocycloid](https://en.wikipedia.org/wiki/Hypocycloid)__ and adapt the Python code (see below) to create your own Hypocycloid curves.

This is a hypotrochoid with $d = r$, the radius of the smaller circle. That is, the pen is attached at the rim of the smaller circle:
$$
(x(\theta),\ y(\theta)) = (\alpha\ cos\theta\ +\ r\ cos(\beta\theta),\ \alpha\ sin\theta\ -\ r\ sin(\beta\theta))
$$
where $\alpha = (R - r)$, and $\beta = (R - r)/r$.

<!--
# Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/
import turtle
from math import cos,sin
from time import sleep

window = turtle.Screen()
window.bgcolor("#FFFFFF")

spirograph = turtle.Turtle()
spirograph.hideturtle()
spirograph.tracer(0)
spirograph.speed(0)
spirograph.pensize(2)

pen = turtle.Turtle()
pen.hideturtle()
pen.tracer(0)
pen.speed(0)
pen.pensize(3)
pen.color("#AA00AA")

R = 125
r = 85
d = r
angle = 0

pen.penup()
pen.goto(R - r + d,0)
pen.pendown()

theta = 0.2
steps = 6 * int(6*3.14/theta)

for t in range(0,steps):
    spirograph.clear()
    spirograph.penup()
    spirograph.setheading(0)
    spirograph.goto(0,-R)
    spirograph.color("#999999")
    spirograph.pendown()
    spirograph.circle(R)
    angle += theta
    
    a, b = (R - r), (R - r)/r

    x = a * cos(angle)
    y = a * sin(angle)
    spirograph.penup()
    spirograph.goto(x,y-r)
    spirograph.color("#222222")
    spirograph.pendown()
    spirograph.circle(r)
    spirograph.penup()
    spirograph.goto(x,y)
    spirograph.dot(5)
    
    x = a * cos(angle) + d * cos(b * angle)
    y = a * sin(angle) - d * sin(b * angle)
    spirograph.pendown()
    spirograph.goto(x,y)
    spirograph.dot(5)

    pen.goto(spirograph.pos())    

    spirograph.getscreen().update() 
    sleep(0.05)

sleep(0.5)
# Hide Spirograph
spirograph.clear()
spirograph.getscreen().update()

https://trinket.io/embed/python/2194390327?start=result
https://trinket.io/embed/python3/9456173d6d?start=result
-->
<iframe src="https://trinket.io/embed/python/2194390327?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


## Epitrochoid
A **epitrochoid** is a type of curve traced by a point attached to a circle of radius $r$ rolling around the _outside_ of a fixed circle of radius $R$, where the point is a distance $d$ from the center of the interior circle.

Find out the properties of an __[epitrochoid](https://en.wikipedia.org/wiki/Epitrochoid)__ and adapt the Python code (see below) to create your own Epitrochoid curves.

The parametric equation for a epitrochoid is:
<!-- $$ ... $$ is a math block, centralized, $ ... $ is inline math --> 
$$
(x(\theta),\ y(\theta)) = (\alpha\ cos\theta\ +\ d\ cos(\beta\theta),\ \alpha\ sin\theta\ -\ d\ sin(\beta\theta))
$$
where $\alpha = (R + r)$, and $\beta = (R + r)/r$.

<!--
# Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/
import turtle
from math import cos,sin
from time import sleep

window = turtle.Screen()
window.bgcolor("#FFFFFF")

spirograph = turtle.Turtle()
spirograph.hideturtle()
spirograph.tracer(0)
spirograph.speed(0)
spirograph.pensize(2)

pen = turtle.Turtle()
pen.hideturtle()
pen.tracer(0)
pen.speed(0)
pen.pensize(3)
pen.color("#AA00AA")

R = 85
r = 35
d = 30
angle = 0

pen.penup()
pen.goto(R + r + d,0)
pen.pendown()

theta = 0.2
steps = 3 * int(6*3.14/theta)

for t in range(0,steps):
    spirograph.clear()
    spirograph.penup()
    spirograph.setheading(0)
    spirograph.goto(0,-R)
    spirograph.color("#999999")
    spirograph.pendown()
    spirograph.circle(R)
    angle += theta
    
    a, b = (R + r), (R + r)/r

    x = a * cos(angle)
    y = a * sin(angle)
    spirograph.penup()
    spirograph.goto(x,y-r)
    spirograph.color("#222222")
    spirograph.pendown()
    spirograph.circle(r)
    spirograph.penup()
    spirograph.goto(x,y)
    spirograph.dot(5)
    
    x = a * cos(angle) + d * cos(b * angle)
    y = a * sin(angle) - d * sin(b * angle)
    spirograph.pendown()
    spirograph.goto(x,y)
    spirograph.dot(5)

    pen.goto(spirograph.pos())    

    spirograph.getscreen().update() 
    sleep(0.05)

sleep(0.5)
# Hide Spirograph
spirograph.clear()
spirograph.getscreen().update()

https://trinket.io/embed/python/5f76c1df4d?start=result
https://trinket.io/embed/python3/9456173d6d?start=result
-->
<iframe src="https://trinket.io/embed/python/5f76c1df4d?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Epicycloid
Find out the properties of an __[epicycloid](https://en.wikipedia.org/wiki/Epicycloid)__ and adapt the Python code (see below) to create your own Epicycloid curves.

This is an epitrochoid with $d = r$, the radius of the smaller circle. That is, the pen is attached at the rim of the smaller circle:
$$
(x(\theta),\ y(\theta)) = (\alpha\ cos\theta\ +\ r\ cos(\beta\theta),\ \alpha\ sin\theta\ -\ r\ sin(\beta\theta))
$$
where $\alpha = (R + r)$, and $\beta = (R + r)/r$.

<!--
# Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/
import turtle
from math import cos,sin
from time import sleep

window = turtle.Screen()
window.bgcolor("#FFFFFF")

spirograph = turtle.Turtle()
spirograph.hideturtle()
spirograph.tracer(0)
spirograph.speed(0)
spirograph.pensize(2)

pen = turtle.Turtle()
pen.hideturtle()
pen.tracer(0)
pen.speed(0)
pen.pensize(3)
pen.color("#AA00AA")

R = 75
r = 50
d = r
angle = 0

pen.penup()
pen.goto(R + r + d,0)
pen.pendown()

theta = 0.2
steps = int(6*3.14/theta)

for t in range(0,steps):
    spirograph.clear()
    spirograph.penup()
    spirograph.setheading(0)
    spirograph.goto(0,-R)
    spirograph.color("#999999")
    spirograph.pendown()
    spirograph.circle(R)
    angle += theta
    
    a, b = (R + r), (R + r)/r

    x = a * cos(angle)
    y = a * sin(angle)
    spirograph.penup()
    spirograph.goto(x,y-r)
    spirograph.color("#222222")
    spirograph.pendown()
    spirograph.circle(r)
    spirograph.penup()
    spirograph.goto(x,y)
    spirograph.dot(5)
    
    x = a * cos(angle) + d * cos(b * angle)
    y = a * sin(angle) - d * sin(b * angle)
    spirograph.pendown()
    spirograph.goto(x,y)
    spirograph.dot(5)

    pen.goto(spirograph.pos())    

    spirograph.getscreen().update() 
    sleep(0.05)

sleep(0.5)
# Hide Spirograph
spirograph.clear()
spirograph.getscreen().update()

https://trinket.io/embed/python/f9c2168ea8?start=result
https://trinket.io/embed/python3/9456173d6d?start=result
-->
<iframe src="https://trinket.io/embed/python/f9c2168ea8?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Cycloid
A cycloid is the curve traced by a point on the rim of a circular wheel as the wheel rolls along a straight line without slipping.

Find out the properties of a __[cycloid](https://en.wikipedia.org/wiki/Cycloid)__ and adapt the Python code (see below) to create your own Cycloid curves.

The equation for the cycloid for a rolling cirlce of radius $r$ is:
$$
(x(\theta),\ y(\theta)) = (r\ (\theta\  -\ sin\theta), r\ (1\ -\ cos\theta))
$$

<!--
# Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/
import turtle
from math import cos, sin, pi
from time import sleep

window = turtle.Screen()
window.bgcolor("#FFFFFF")

# the drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.tracer(0)
pen.speed(0)
pen.pensize(3)
pen.color("#AA00AA")

# the rolling circle
wheel = turtle.Turtle()
wheel.hideturtle()
wheel.tracer(0)
wheel.speed(0)
wheel.pensize(1)

# the wheel center
c = turtle.Turtle()
c.hideturtle()
c.tracer(0)
c.speed(0)

# the ground
ground = turtle.Turtle()

r = 60
angle = 0
theta = 0.1
steps = 80
offset = 3 * r

pen.penup()
pen.backward(offset)
pen.pendown()

wheel.penup()
wheel.back(offset)

c.penup()
c.goto(-offset, r)

ground.penup()
ground.goto(-3 * r, 0)
ground.pendown()
ground.forward(7 * r)

for _ in range(0, steps):
    wheel.clear()
    wheel.down()
    wheel.circle(r)
    x = r * (angle - sin(angle))
    y = r * (1 - cos(angle))
    pen.goto(x - offset, y)
    c.clear()
    c.down()
    c.goto(pen.position())
    c.up()
    angle += theta
    wheel.up()
    wheel.forward(r * theta)
    c.goto(wheel.position())
    c.setheading(-90)
    c.back(r)
    
    wheel.getscreen().update() 
    sleep(0.05)

>>>> another hypocycloid
# Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/
import turtle
from math import cos,sin
from time import sleep

window = turtle.Screen()
window.bgcolor("#FFFFFF")

spirograph = turtle.Turtle()
spirograph.hideturtle()
spirograph.tracer(0)
spirograph.speed(0)
spirograph.pensize(2)

pen = turtle.Turtle()
pen.hideturtle()
pen.tracer(0)
pen.speed(0)
pen.pensize(3)
pen.color("#AA00AA")

# make spirograph a straight line, otherwise just a hypocycloid.
R = 150
r = 50
d = r
angle = 0

pen.penup()
# pen.goto(R - r + d,0)
pen.goto(r,0)
pen.pendown()

theta = 0.2
steps = int(6*3.14/theta/5) 

for t in range(0,steps):
    spirograph.clear()
    spirograph.penup()
    spirograph.setheading(0)
    spirograph.goto(0,-R)
    spirograph.color("#999999")
    spirograph.pendown()
    spirograph.circle(R)
    angle += theta
    
    a, b = (R - r), (R - r)/r

    x = b * angle / 5 - a
    y = 0
    spirograph.penup()
    spirograph.goto(x,y-r)
    spirograph.color("#222222")
    spirograph.pendown()
    spirograph.circle(r)
    spirograph.penup()
    spirograph.goto(x,y)
    spirograph.dot(5)
    
    x = a * cos(angle) + d * cos(b * angle)
    y = a * sin(angle) - d * sin(b * angle)
    spirograph.pendown()
    spirograph.goto(x,y)
    spirograph.dot(5)

    pen.goto(spirograph.pos())    

    spirograph.getscreen().update() 
    sleep(0.05)

sleep(0.5)
# Hide Spirograph
# spirograph.clear()
spirograph.getscreen().update()
>>>
-->
<iframe src="https://trinket.io/embed/python/98fe46235f?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Cycloid (by ChatGPT)
<!--
import turtle
import math

# Create a turtle screen
wn = turtle.Screen()
wn.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed to the maximum

# Parameters for the cycloid
R = 100  # Radius of the cycloid
r = 30   # Radius of the rolling circle
d = 100  # Distance from the center of the rolling circle to the tracing point

# Function to draw a cycloid segment
def draw_cycloid_segment():
    for angle in range(0, 360):
        radian_angle = math.radians(angle)
        x = (R - r) * math.cos(radian_angle) + d * math.cos((R - r) * radian_angle / r)
        y = (R - r) * math.sin(radian_angle) - d * math.sin((R - r) * radian_angle / r)
        t.goto(x, y)

# Position the turtle at the starting point
t.penup()
t.goto(0, R - r)
t.pendown()

# Animate the drawing of the cycloid
for _ in range(4):  # Draw four segments of the cycloid
    draw_cycloid_segment()

# Close the turtle graphics window when clicked
wn.exitonclick()

This draws not a cycloid, but a 3 segment pattern with a bug. Suppose to be 4 segments,'
Where is the bug?
the starting point is wrong: putting angle 0 gives (R - r + d, 0)
After one segment, x = (R - r) * cos(2 * pi) + d * cos ((R - r)/r * 2pi),
thus the segment just repeats.
Need to put range(0, 3 * 360), since (R - r)/r = (100 - 30)/30 = 7/3.

# Cycloid by ChatGPT (corrected version)

import turtle
import math

# Create a turtle screen
wn = turtle.Screen()
wn.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed to the maximum
t.pensize(3)
t.color("#AA00AA")

# Parameters for the cycloid
R = 100  # Radius of the cycloid
r = 30   # Radius of the rolling circle
d = 100  # Distance from the center of the rolling circle to the tracing point
n = 3    # number of rounds. (R - r)/r = 70/30 = 7/3,
         # and 7/3 (n * 2 * pi) gives a multiple of 2 * pi when n = 3

# Function to draw a cycloid
def draw_cycloid():
    for angle in range(0, n * 360):
        radian_angle = math.radians(angle)
        x = (R - r) * math.cos(radian_angle) + d * math.cos((R - r) * radian_angle / r)
        y = (R - r) * math.sin(radian_angle) - d * math.sin((R - r) * radian_angle / r)
        t.goto(x, y)

# Position the turtle at the starting point
t.penup()
t.goto(R - r + d, 0)
t.pendown()

# Animate the drawing of the cycloid
draw_cycloid()

# This is a hypotrochoid, not a cycloid.

-->
<iframe src="https://trinket.io/embed/python/df7721c652?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

<!-- pandoc -s demo10b.md -o demo10b.html --mathjax  (for better math display) -->
