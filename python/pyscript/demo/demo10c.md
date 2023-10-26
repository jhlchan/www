---
title: Pyscript - Demo 10C
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
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo10c.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo10c.html -->
---

# Pyscript - Trinket Playground

Spare ones for edit (always copy the source code):

## First: Plots
<!--
# First plot
import matplotlib.pyplot as plt
import numpy as np

# First plot
plt.clf()  # clear, not really need for first

# specify the x coordinates
angle = np.linspace(0, 2 * np.pi, 100)

# make some plots
plt.plot(angle, np.sin(angle), color='green')
plt.plot(angle, np.cos(angle), color='blue')
plt.xlabel('angle')
plt.ylabel('value')
plt.title('Sine (green) and Cosine (blue) waves, from 0 to 2π:')

# display the plots
plt.show()

https://trinket.io/embed/python/193e1dfa73?start=result
Python2 version matplotlib has color error: both curves have the last mentioned color.
https://trinket.io/embed/python3/b72802dffd?start=result
Python3 version matplotlib has correct colors.
-->
<iframe src="https://trinket.io/embed/python3/b72802dffd?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Another Matplotlib Plot (Python3 only)
<!--
# Second plot
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

plt.clf()  # clear the plot

# First create the x and y coordinates of the points.
n_angles = 36
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles

x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
z = (np.cos(radii) * np.cos(3 * angles)).flatten()

# Create the Triangulation; no triangles so Delaunay triangulation created.
triang = tri.Triangulation(x, y)

# Mask off unwanted triangles.
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)

fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tpc = ax1.tripcolor(triang, z, shading='flat')
fig1.colorbar(tpc)
ax1.set_title('tripcolor of Delaunay triangulation, flat shading')

plt.show()

https://trinket.io/embed/python/193e1dfa73?start=result 
ImportError: No module named matplotlib.tri on line 21 in main.py. You can find a list of available modules at docs/python.
https://trinket.io/embed/python3/9456173d6d?start=result
The library matplotlib.tri is available in Python3.
-->
<iframe src="https://trinket.io/embed/python3/81a0ee1c11?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Second: Turtles
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

https://trinket.io/embed/python/75a0bfd770?start=result
https://trinket.io/embed/python3/9456173d6d?start=result
Turtle Graphics is only available in a Python2 trinket, not a Python3 trinket.
-->
<iframe src="https://trinket.io/embed/python/b93957a637?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Another Turtle Graphics
<!--
import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size)
    turtle.penup()
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(500)

draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)

tommy.penup()
tommy.goto(0,-50)
tommy.color('black')
tommy.write("Let's Learn Python!", align="center", font=(None, 16, "bold"))
tommy.goto(0,-80)

https://trinket.io/embed/python/75a0bfd770?start=result
https://trinket.io/embed/python3/9456173d6d?start=result
Turtle Graphics is only available in a Python2 trinket, not a Python3 trinket.
-->
<iframe src="https://trinket.io/embed/python/e29af862c7?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Third (also Plots for now)
<!--
# Data Scatter Plot

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [9, 10, 11, 12, 13, 14, 15, 16]

plt.scatter(x,y, label="Skatter", marker="*", s=50)
plt.xlabel("x" )
plt.ylabel("y")
plt.title("Basic Scatter Plot")

plt.legend()
plt.show()

https://trinket.io/embed/python/bac4c74ed4?start=result  not working in Python2
https://trinket.io/embed/python3/9456173d6d?start=result  only works in Python3
-->
<iframe src="https://trinket.io/embed/python3/a06cc2b4ef?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


## Cycloid (by Matplotlib)

<!--
How to plot Cycloid with python
by chunying lyu, 6 March 2019.
https://medium.com/@lyuchunying27/how-to-plot-cycloid-with-python-c0defaf0403a

# Cycloid by Matplotlib

import matplotlib.pyplot as plt
import numpy as np

def circle(x0, y0, color='r', r=1):
    t = np.arange(0,2*np.pi,1./100)
    x = np.cos(t)*r + x0
    y = np.sin(t)*r + y0
    plt.plot(x,y,color=color)

def bar(x0, y0, theta, color='m', r=1):
    rr = np.arange(0,r,1./100)
    x = np.cos(theta)*rr + x0
    y = np.sin(theta)*rr + y0
    plt.plot(x,y,color=color)

# plot cycloid
theta = np.arange(0,2*np.pi,1./100)
x = theta - np.sin(theta)
y = 1-np.cos(theta)
plt.axis('equal')
plt.plot(x,y,'y')

# plot origin circle (x0=0,y0=1)
circle(0,1,'r')
bar(0,1,-np.pi/2,'r')

# plot circle 1
theta = np.pi*0.4
circle(theta,1,'g')
bar(theta,1,-theta-np.pi/2,'g')
bar(theta,1,-np.pi/2,'c')

# show the cycloid
plt.show()

-->
<iframe src="https://trinket.io/embed/python3/65146feb5c?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Cycloid (by Turtle)
<!--
# Cycloid by Turtle Graphics

import turtle
from time import sleep

c = turtle.Turtle()  # draw the circle
t = turtle.Turtle()  # center of circle, as turtle
pen = turtle.Turtle() # the drawing pen
ground = turtle.Turtle() # the horizontal ground

c.hideturtle()
c.tracer(0)
c.speed(0)

t.hideturtle()
t.tracer(0)
t.speed(0)

pen.hideturtle()
pen.tracer(0)
pen.speed(0)

ground.hideturtle()
ground.tracer(0)
ground.speed(0)

# radius for circle 
r = 60

# set the center
c.penup()
c.goto(-3 * r,0)
t.penup()
t.goto(-3 * r,r)   # at center
pen.penup()
pen.goto(c.position()) # pen at circle bottom
pen.pendown()
pen.pensize(3)
pen.color("#AA00AA")
ground.goto(c.position()) # ground at circle bottom

# pen to follow a dot on the circle
def mark(angle):
    t.right(90 + angle)
    t.pendown()
    t.forward(r)
    t.penup()
    pen.goto(t.position())
    t.backward(r)
    t.left(90 + angle)
    t.getscreen().update() 
    sleep(0.05)

# move turtle
step = 10
angle = 0  # turle angle in degrees
speed = 1.0  # this gives a cycloid with cusps

for j in range(1, 50):
   t.clear()
   c.clear()
   c.pendown()
   c.forward(step)
   c.circle(r)
   ground.forward(step)
   t.forward(step)
   angle += speed * step 
   mark(angle)

-->
<iframe src="https://trinket.io/embed/python/07dc228601?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Turtle Random Walk

<!--
# Random Walk by Turtle

import turtle
import random

# Assumes turtle.mode('standard')
DIRECTIONS = (EAST, NORTH, WEST, SOUTH) = (0, 90, 180, 270)

# turtle turn and walk
def go(heading, size):
    turtle.setheading(heading)
    turtle.forward(size)

# random walk with size and steps
def random_walk(size, steps):
    for _ in range(steps):
        go(random.choice(DIRECTIONS), size)

# make a turtle and do the walk
turtle.hideturtle()
turtle.speed(0) # fastest
random_walk(15, 1000)

>>> this is better

# Random Walk by Turtle

import turtle
import random

# Assumes turtle.mode('standard')
DIRECTIONS = (EAST, NORTH, WEST, SOUTH) = (0, 90, 180, 270)

t = turtle.Turtle()
t.speed(0) # fastest
t.pensize(2)
t.color("#AA00AA")
t.setheading(0)
    
# turtle turn and walk
def go(heading, size):
    t.setheading(heading)
    t.forward(size)

# random walk with size and steps
def random_walk(size, steps):
    for _ in range(steps):
        go(random.choice(DIRECTIONS), size)

# do the walk
random_walk(15, 500)

Random walk in Python + turtle
https://codereview.stackexchange.com/questions/74495/random-walk-in-python-turtle

-->
<iframe src="https://trinket.io/embed/python/469cd2e5d1?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

<!-- pandoc -s demo10c.md -o demo10c.html -->
