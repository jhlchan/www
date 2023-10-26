---
title: Pyscript - Demo 7
header-includes: |
    <style>
       body { min-width: 90% !important; }
    </style>
include-before: |
    <link href="https://fonts.cdnfonts.com/css/digital-7-mono" rel="stylesheet">
    <style>
    .clock {
        zbackground-color:#333; /* almost black */
        background-color:#334ba3; /* dark blue */
        padding:25px;
        max-width:300px;
        width:100%;
        text-align:center;
        border-radius:5px;
        margin: 0 auto;
    }
    .digital {
        background: #442469;  /* fallback for old browsers, dark pink */
        xbackground: -webkit-linear-gradient(to right, #243B55, #141E30);  /* Chrome 10-25, Safari 5.1-6 */
        ybackground: linear-gradient(to right, #243B55, #141E30); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
        padding:25px;
        max-width:550px;
        width:100%;
        text-align:center;
        border-radius:5px;
        margin:0 auto;
      
    }
    #time{
        font-family: 'Digital-7 Mono', sans-serif;
        font-size:60px;
        text-shadow:0px 0px 1px #fff;
        color:#fff;
    }
    #date {
        letter-spacing:3px;
        font-size:14px;
        font-family:arial,sans-serif;
        color:#fff;
    }
    </style>    
include-after: |
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css"/>
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo07.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo07.html -->
---

# Pyscript - Ticking Clocks

## Classic Clock

:::{.clock}
<canvas id="clock" width="300" height="300">
</canvas>
:::

## Digital Clock

::::::{#clockdate .digital}
:::{#time}
:::

:::{#date}
:::
::::::


Type your Python code (hover mouse/pointer to bottom right-end for Green arrow to run code):
<py-repl></py-repl>

<!-- pyscript -->
```{=html}
<py-script>
from datetime import datetime
from js import document, Math, setInterval
from pyodide.ffi import create_proxy

# Classic round-face clock
def classic_clock():
    canvas = document.getElementById("clock") # not Element("canvas")
    ctx = canvas.getContext("2d")
    radius = canvas.height / 2
    ctx.translate(radius, radius) # move (0,0) to (radius, radius)
    radius = radius * 0.90 # shrink clock radius

    drawClock(ctx, radius)
    interval_id = setInterval(create_proxy(drawClock), 1000, ctx, radius)

# Draw the clock
def drawClock(ctx, radius):
    drawFace(ctx, radius)
    drawNumbers(ctx, radius)
    drawTime(ctx, radius)

# Draw the face
def drawFace(ctx, radius):
    ctx.beginPath()
    ctx.arc(0, 0, radius, 0, 2 * Math.PI)
    ctx.fillStyle = 'white'
    ctx.fill()
    grad = ctx.createRadialGradient(0,0,radius*0.95, 0,0,radius*1.05)
    grad.addColorStop(0, '#333')
    grad.addColorStop(0.5, 'white')
    grad.addColorStop(1, '#333')
    ctx.strokeStyle = grad
    ctx.lineWidth = radius * 0.1
    ctx.stroke()
    ctx.beginPath()
    ctx.arc(0, 0, radius*0.1, 0, 2 * Math.PI)
    ctx.fillStyle = '#333'
    ctx.fill()

# Draw the numbers
def drawNumbers(ctx, radius):
    ctx.font = str(radius * 0.15) + "px arial"
    ctx.textBaseline = "middle"
    ctx.textAlign = "center"
    for num in range(1, 13):
        ang = num * Math.PI / 6
        ctx.rotate(ang)
        ctx.translate(0, -radius * 0.85)
        ctx.rotate(-ang)
        ctx.fillText(str(num), 0, 0)
        ctx.rotate(ang)
        ctx.translate(0, radius * 0.85)
        ctx.rotate(-ang)

# Draw the time
def drawTime(ctx, radius):
    now = datetime.now()

    hour = now.hour
    minute = now.minute
    second = now.second

    # hour
    hour = hour % 12
    hour = (hour * Math.PI / 6)
    hour += (minute * Math.PI / (6*60))
    hour += (second * Math.PI / (360 * 60))

    drawHand(ctx, hour, radius*0.5, radius*0.07)

    # minute
    minute = (minute * Math.PI / 30)
    minute += (second * Math.PI / (30 * 60))

    drawHand(ctx, minute, radius * 0.8, radius * 0.07)

    #  second
    second = second * Math.PI / 30
    drawHand(ctx, second, radius * 0.9, radius * 0.02)

# Draw a clock hand
def drawHand(ctx, pos, length, width):
    ctx.beginPath()
    ctx.lineWidth = width
    ctx.lineCap = "round"
    ctx.moveTo(0,0)
    ctx.rotate(pos)
    ctx.lineTo(0, -length)
    ctx.stroke()
    ctx.rotate(-pos)

# Digital Clock with date
def digital_clock():
    showDateTime()
    intervalID = setInterval(create_proxy(showDateTime), 1000)

# Display using Python string formatting codes for datetime
def showDateTime():
    now = datetime.now()
    time = Element('time')
    date = Element('date')
    # Font is digital using digital-7-mono
    time.write(now.strftime("%H:%M:%S %p"))   
    date.write(now.strftime("%A %d %B %Y"))

classic_clock()
digital_clock()
</py-script>
```
---

<!-- pandoc -s demo07.md -o demo07.html -->