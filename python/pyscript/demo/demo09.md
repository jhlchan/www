---
title: Pyscript - Demo 9
header-includes: |
    <style>
       body { min-width: 90% !important; }
    </style>
include-before: |
    <style>
        .loading {
            display: inline-block;
            width: 50px;
            height: 50px;
            border: 3px solid rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            border-top-color: black;
            animation: spin 1s ease-in-out infinite;
        }

        canvas {
            display: none;
        }

        @keyframes spin {
            to {
                transform: rotate(360deg);
            }
        }
        .tcenter {
            text-align: center;
        }
        .twidth {
            width: 40px;
        }
        .nobreak {
            white-space: pre;
        }
        .inrow {
            display: flex;
            flex-direction: row;
        }
        .numbox {
            width: 80px; 
            text-align: right;
        }
        .param {
            display: flex;
            flex-direction: column;
            width: 600px;
        }
    </style>
include-after: |
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css"/>
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo09.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo09.html -->
---

# Pyscript - Mandelbrot and Julia sets

## Relationship

![One Mandelbrot set but many Julia sets](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*haCkgC_ZFkPlVQumVj3pjA.jpeg){ width=60% }

![Julia sets around the Mandelbrot set](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*3hh5Vtc7dxm1cYd3HD-ntg.jpeg){ width=60% }


| Julia set identifier  |  at complex number c   |
|:----------------------|-----------------------:|
| 1                     | -0.722 + 0.246j        |
| 2                     | -0.74529 + 0.113075j   |
| 3                     | -0.40 - 0.59j          |
| 4                     | 0.355534 - 0.337292j   |
| 5                     | 0.34 - 0.05j           |
| 6                     | 0.37 + 0.1j            |
| 7                     | 0.355 + 0.355j         |
| 8                     | 0.54 + 0.54j           |
| 9                     | 0 + 0.8j               |
| 10                    | -0.54 + 0.54j          | 


## Mandelbrot Set
<!-- output target -->


::::::{#mandelbrot .param}

<fieldset class="inrow">

[max number of iteration = ]{.nobreak}
<input id="mmax" type="text" class="py-input" value="100">

::::{.inrow}

[x range = &lbrack;]{.nobreak}
<input id="mx0" type="text" class="numbox" value="-2">

[, ]{.nobreak}
<input id="mx1" type="text" class="numbox" value="1">

[&rbrack;]{.nobreak}

::::

::::{.inrow}

[y range = &lbrack;]{.nobreak}
<input id="my0" type="text" class="numbox" value="-1.5">

[, ]{.nobreak}
<input id="my1" type="text" class="numbox" value="1.5">

[&rbrack;]{.nobreak}

<button id="mreset" class="py-button">Reset</button>

::::

</fieldset>

The complex point c at: []{#point}

:::::{.loading}
:::::

<canvas></canvas>

::::::

## Julia Set

::::::{#julia .param}

<fieldset class="inrow">

[complex number c = ]{.nobreak}
<input id="complex" type="text" class="py-input" value="-0.4 + 0.6j">

[max number of iteration = ]{.nobreak}
<input id="jmax" type="text" class="py-input" value="100">

::::{.inrow}

[x range = &lbrack;]{.nobreak}
<input id="jx0" type="text" class="numbox" value="-1.5">

[, ]{.nobreak}
<input id="jx1" type="text" class="numbox" value="1.5">

[&rbrack;]{.nobreak}

::::

::::{.inrow}

[y range = &lbrack;]{.nobreak}
<input id="jy0" type="text" class="numbox" value="-1.5">

[, ]{.nobreak}
<input id="jy1" type="text" class="numbox" value="1.5">

[&rbrack;]{.nobreak}

<button id="jreset" class="py-button">Reset</button>

::::

</fieldset>


:::::{.loading}
:::::

<canvas></canvas>

::::::

<py-terminal id="debug"></py-terminal>


Type your Python code (hover mouse/pointer to bottom right-end for Green arrow to run code):
<py-repl></py-repl>


<!--

Draw the Mandelbrot Set in Python
by Bartosz Zaczyński
https://realpython.com/mandelbrot-set-python/

The Map of Julia Sets
It’s hard to talk about the Mandelbrot set without mentioning Julia sets, which had been discovered by French mathematician Gaston Julia several decades earlier without the help of computers. Julia sets and the Mandelbrot set are closely related because you can obtain them through the same recursive formula, only with different sets of starting conditions.

While there’s only one Mandelbrot set, there are infinitely many Julia sets. So far, you always started the sequence at z0 = 0 and systematically tested some arbitrary complex number, c, for its membership. On the other hand, to find out if a number belongs to a Julia set, you must use that number as the starting point for the sequence and pick another value for the c parameter.

Here’s a quick comparison of the formula’s terms depending on which set you’re investigating:
Term    Mandelbrot Set  Julia Set
  z0                 0   Candidate value
   c   Candidate value     Fixed constant

You can download the complete source code used throughout this tutorial by clicking the link below:
https://realpython.com/bonus/mandelbrot-set-python-project-code/
email: u4988135@anu.edu.au
materials-mandelbrot-set-python.zip
https://github.com/realpython/materials/tree/master/mandelbrot-set-python

Animating Fractals with Python: Julia and Maldelbrot Sets
by Edward Roe, 7 April 2022.
https://medium.com/@er_95882/animating-fractals-with-python-julia-and-maldelbrot-sets-e65a04549423
Many animations in Python code

References

[1] Julia, Gaston, Mémoire sur l’itération des fonctions rationnelles. Journal de Mathématiques Pures et Appliquées (in French). 1: 47–245, 1918.
[2] Mandelbrot, Benoit B., The Fractal Geometry of Nature. W. H. Freeman and Company, 1982.
[4] Peitgen, Heinz-Otto and Richter, Peter H. The Beauty of Fractals: Images of Complex Dynamical Systems. Springer, 1986.
[5] Stewart, Ian (Editor). The Colours of Infinity: The Beauty and Power of Fractals. Springer, 2004.

Julia Set: Animate your own in Python with Matplotlib
by Vladimir Ilievski
(Squared: Science Explained)
https://isquared.digital/visualizations/2020-06-26-julia-set/
Animation: Julia set convergence for c = r e^{ia}  as a changes counterclockwise
The source code behind this animation and simulation can be found in this Python Notebook.
https://github.com/IlievskiV/Amusive-Blogging-N-Coding/blob/master/Visualizations/julia_set.ipynb

-->

<!-- pyscript -->
```{=html}
<py-config>
    packages = ["numpy", "sympy"]
    [[fetch]]
    files = ["examples/palettes.py"]
</py-config>
<py-script>
from pyodide.ffi import to_js, create_proxy

import numpy as np
import sympy

from js import (
    console,
    document,
    devicePixelRatio,
    ImageData,
    Uint8ClampedArray,
    CanvasRenderingContext2D as Context2d,
    requestAnimationFrame,
)

from examples.palettes import Magma256

# Given a canvas element, set its width and height, return its 2D context
def prepare_canvas(width: int, height: int, canvas: Element) -> Context2d:
    ctx = canvas.getContext("2d")

    canvas.style.width = f"{width}px"
    canvas.style.height = f"{height}px"

    canvas.width = width
    canvas.height = height

    ctx.clearRect(0, 0, width, height)

    return ctx

# Convert the data array to color array using the palette
def color_map(array: np.array, palette: np.array) -> np.array:
    size, _ = palette.shape
    index = (array/array.max()*(size - 1)).round().astype("uint8")

    width, height = array.shape
    image = np.full((width, height, 4), 0xff, dtype=np.uint8)
    image[:, :, :3] = palette[index]

    return image

# Draw the image on the canvas
def draw_image(ctx: Context2d, image: np.array) -> None:
  data = Uint8ClampedArray.new(to_js(image.tobytes()))
  width, height, _ = image.shape
  image_data = ImageData.new(data, width, height)
  ctx.putImageData(image_data, 0, 0)

# standard width and height
width, height = 600, 600

# logging
# debug = True
debug = False

if not debug: document.getElementById('debug').style = 'display: none'

# Range for selection
Range = tuple[float, float]

# get ranges
def ranges(args):
  x0_in = document.querySelector(args[0])
  x1_in = document.querySelector(args[1])
  y0_in = document.querySelector(args[2])
  y1_in = document.querySelector(args[3])

  xr = (float(x0_in.value), float(x1_in.value))
  yr = (float(y0_in.value), float(y1_in.value))

  return xr, yr

# set ranges
def setRanges(args, xr, yr):
    document.querySelector(args[0]).value = xr[0]
    document.querySelector(args[1]).value = xr[1]
    document.querySelector(args[2]).value = yr[0]
    document.querySelector(args[3]).value = yr[1]


# Mandelbrot set
# compute the divergence time of a point z = (x,y) with zoom factor and max iterations
def mandelbrot(
    width: int,
    height: int,
    *,
    x: float = -0.5,
    y: float = 0,
    zoom: int = 1,
    max_iterations: int = 100
) -> np.array:
    """
    https://www.learnpythonwithrune.org/numpy-compute-mandelbrot-set-by-vectorization
    """
    xr, yr = ranges(['#mx0','#mx1','#my0','#my1'])
    if debug: print(f'mandelbrot at ({x},{y}), with x-range {xr} and y-range {yr}.')
    # mandelbrot at (-0.5,0), with x-range (-2.5, 2.5) and y-range (-5.0, 5.0).
    # mandelbrot at (-0.5,0), with x-range (-0.37916666666666665, 1.7291666666666667) and y-range (-3.2986111958821613, -0.49861119588216146).

    # JC modifications
    # (x,y) at the center of xr, yr
    # determine x, y from ranges,
    # determine zoom by (3 units)/(side), where side is the square that fits the selected rectangle.
    # max iterations is taken from input
    x = sum(xr)/2
    y = sum(yr)/2
    zoom = 3 / min (xr[1] - xr[0], yr[1] - yr[0])
    max_iterations = int(Element('mmax').value)
    # the original x = -0.5 is average of xr: Range = (-2, 1)
    # the original y =  0.0 is average of yr: Range = (-1.5, 1.5)
    # End JC modifications

    # To make navigation easier we calculate these values
    x_width, y_height = 1.5, 1.5 * height / width
    x_from, x_to = x - x_width / zoom, x + x_width / zoom
    y_from, y_to = y - y_height / zoom, y + y_height / zoom

    # Here the actual algorithm starts
    x = np.linspace(x_from, x_to, width).reshape((1, width))
    y = np.linspace(y_from, y_to, height).reshape((height, 1))
    c = x + 1j * y  # 1j is the imaginary unit, a complex number
    # Python has built-in complex arithmetic.

    # Initialize z to all zero
    z = np.zeros(c.shape, dtype=np.complex128)

    # To keep track in which iteration the point diverged
    div_time = np.zeros(z.shape, dtype=int)

    # To keep track on which points did not converge so far
    m = np.full(c.shape, True, dtype=bool)
    for i in range(max_iterations):
        z[m] = z[m] ** 2 + c[m]
        diverged = np.greater(
            np.abs(z), 2, out=np.full(c.shape, False), where=m
        )  # Find diverging
        div_time[diverged] = i  # set the value of the diverged iteration number
        m[np.abs(z) > 2] = False  # to remember which have diverged

    return div_time


# Drawing Mandelbrot set

# global here
mcurrent_image = None

async def draw_mandelbrot() -> None:
  spinner = document.querySelector("#mandelbrot .loading")
  canvas = document.querySelector("#mandelbrot canvas")

  spinner.style.display = ""
  canvas.style.display = "none"

  ctx = prepare_canvas(width, height, canvas)

  console.log("Computing Mandelbrot set ...")
  console.time("mandelbrot")
  iters = mandelbrot(width, height)
  console.timeEnd("mandelbrot")

  image = color_map(iters, Magma256)

  # must say global here, so that current_image is the outside one.
  global mcurrent_image
  mcurrent_image = image  # update global
  # draw_image(ctx, image)
  mark(julia_c) # mark c will draw the image

  spinner.style.display = "none"
  canvas.style.display = "block"


# Handle changes in Mandelbrot set
mhandler = create_proxy(lambda _event: draw_mandelbrot())
document.querySelector("#mandelbrot fieldset").addEventListener("change", mhandler)

mcanvas = document.querySelector("#mandelbrot canvas")

# get the pointer coordinates in canvas given a pointer event
def getPoint(event):
    # mcanvas is read-only, no need for global
    rect = mcanvas.getBoundingClientRect()
    # rect.x = rect.left = 75, rect.y = rect.top = 41,
    # rect.right = rect.left + 600 = 675, rect.bottom = rect.top + 600 = 641
    # event         (e.x, e.y)    (e.x - r.x, e.y - r.y)    canvas          coordinates
    # top left       (75,  41)             (0, 0)            (0, 0)         (-2, 1.5)
    # top right     (675,  41)           (600, 0)          (600, 0)         ( 1, 1.5)
    # bottom left    (75, 641)             (0, 600)          (0, 600)       (-2,-1.5)
    # bottom right  (675, 641)           (600, 600)        (600, 600)       ( 1,-1.5)
    print(f'getPoint event at: {event.clientX}, {event.clientY}, rect.xy = {rect.x}, {rect.y}')
    cx = event.clientX - rect.x  # canvas x from left to right
    cy = event.clientY - rect.y  # canvas y from top to bottom
    # adjust coordinates to complex(x,y)
    scale = 200  # since 0 to 600 for -2 to 1, scale = 600/3 = 200
    x = (cx - mcanvas.width/2) / scale - 1/2  # new x from left to right
    # x = (cx - 400)/200: (cx, x) = (0, -2)  (100, -1.5) (200, -1)  (300, 0) (400, 0)    (500, 0.5) (600, 1)
    y = (mcanvas.height/2 - cy) / scale  # new y from bottom to top
    # y = (300 - cy)/200: (cy, y) = (0, 1.5) (100,1)     (200, 0.5) (300, 0) (400, -0.5) (500,-1)   (600,-1.5)
    print(f'getPoint result: {x}, {y}')
    return x, y

# get the pointer event given the pointer coordinates
def setPoint(x, y):
    rect = mcanvas.getBoundingClientRect()
    scale = 200  # since 0 to 600 for -1.5 to 1.5
    if debug: print(f'Set point before: {x}, {y} and scale: {scale}, half of {mcanvas.height}')
    cx = (x + 1/2) * scale  + (mcanvas.width / 2)
    cy = (mcanvas.height / 2) - y * scale
    if debug: print(f'Set point after: {cx}, {cy} by rect left/top: {rect.left}, {rect.top}')
    return cx, cy   # the canvas coordinates

# invert a select range
def invert(sx, source_range, target_range):
    source_start, source_end = source_range
    target_start, target_end = target_range
    factor = (target_end - target_start)/(source_end - source_start)
    if debug: print(f'invert: factor = {factor}')
    offset = -(factor * source_start) + target_start
    # avoid ZeroDivisionError: float division by zero
    return (sx - offset) / factor

# globals variables for modification
mis_selecting = False
minit_sx, minit_sy = None, None
msx, msy = None, None

async def mmousemove(event):
  # declare global, as they will be updated
  global mis_selecting
  global minit_sx
  global minit_sy
  global msx
  global msy

  # only reading mcanvas, which is global
  bds = mcanvas.getBoundingClientRect()
  event_sx, event_sy = event.clientX - bds.x, event.clientY - bds.y

  ctx = mcanvas.getContext("2d")

  # show coordinates of the point
  x, y = getPoint(event)
  # complex to string removing parentheses
  display(str(complex(x,y))[1:-1], target="point", append=False)

  pressed = event.buttons == 1
  if mis_selecting:
    if not pressed:
      xr, yr = ranges(['#mx0','#mx1','#my0','#my1'])
      # ignore if range is too small
      if (xr[1] - xr[0] < 2) or (yr[1] - yr[0] < 2):
         display('Mandelbrot selected?', target='point', append=False)
         return

      x0 = invert(minit_sx, xr, (0, width))
      x1 = invert(msx, xr, (0, width))
      y0 = invert(minit_sy, yr, (0, height))
      y1 = invert(msy, yr, (0, height))

      if debug: print(f'top-left: ({minit_sx},{minit_sy}), bottom-right: ({msx},{msy}) with original ranges: {xr}, {yr}, new ranges: ({x0}, {x1}), ({y0}, {y1}).')

      setRanges(['#mx0','#mx1','#my0','#my1'], (x0, x1), (y0, y1))

      mis_selecting = False
      minit_sx, minit_sy = None, None
      msx, msy = minit_sx, minit_sy

      await draw_mandelbrot()
    else:
      ctx.save()
      ctx.clearRect(0, 0, width, height)
      draw_image(ctx, mcurrent_image)
      msx, msy = event_sx, event_sy
      ctx.beginPath()
      ctx.rect(minit_sx, minit_sy, msx - minit_sx, msy - minit_sy)
      ctx.fillStyle = "rgba(255, 255, 255, 0.4)"
      ctx.strokeStyle = "rgba(255, 255, 255, 1.0)"
      ctx.fill()
      ctx.stroke()
      ctx.restore()
  else:
    if pressed:
      mis_selecting = True
      minit_sx, minit_sy = event_sx, event_sy
      msx, msy = minit_sx, minit_sy

mcanvas.addEventListener("mousemove", create_proxy(mmousemove))

# the click event is ignored
async def mreset(event):
    # Range([-2, 1]), Range([-1.5, 1.5])
    setRanges(['#mx0','#mx1','#my0','#my1'], (-2, 1), (-1.5, 1.5))
    await draw_mandelbrot()

# Note: py-click cannot accommodate an async function.
document.getElementById('mreset').addEventListener('click', create_proxy(mreset))


# the complex number for Julia set
julia_c = complex(0,0) # cannot get this from id='point' due to mousemove
# other values of beauty:
# -1.0225+0.25199996948242187j
# -0.40 + 0.6j -- all with too simple colors

# mark complex c on Mandelbrot canvas
def mark(c):
    ctx = mcanvas.getContext("2d")
    # redraw the image
    draw_image(ctx, mcurrent_image) # reading global
    x, y = c.real, c.imag  # real and imaginary parts
    sx, sy = setPoint(x,y)
    if debug: print(f'mark: setPoint({x}, {y}) gives {sx}, {sy}.')
    ctx.save()
    # this is a rectangular dot
    # ctx.fillStyle = 'yellow'
    # ctx.fillRect(sx,sy,10,10)
    # this is a circular ring
    ctx.beginPath()
    ctx.arc(sx, sy, 5, 0, 6.28) # 5 pixels radius
    ctx.lineWidth = 2
    ctx.strokeStyle = 'yellow'
    ctx.stroke()
    ctx.restore()

# get mouse position of canvas given a double-click event
async def dblclick(event):
    x, y = getPoint(event)
    c = complex(x,y)
    display('Julia at: ' + str(c)[1:-1], target="point", append=False)
    global julia_c  # for global update
    julia_c = c     # do global update
    putComplex(c)   # ignore the return standard ranges
    # draw the Julia set as new
    await draw_julia()

mcanvas.addEventListener("dblclick", create_proxy(dblclick))

# update the complex point as input
def putComplex(c):
    # property 'value' of 'Element' object has no setter
    document.getElementById("complex").value = str(c)[1:-1] # remove parenthesis
    # pass a list argument to tuple, otherwise
    # TypeError: tuple expected at most 1 argument, got 2
    xr, yr = Range([-1.5, 1.5]), Range([-1.5, 1.5])
    setRanges(['#jx0','#jx1','#jy0','#jy1'], xr, yr)
    # also update mark in Mandelbrot
    mark(c)
    return xr, yr

# Julia set
def julia(
    width: int,
    height: int,
    *,
    c: complex = -0.4 + 0.6j,
    x: float = 0,
    y: float = 0,
    zoom: int = 1,
    max_iterations: int = 100
) -> np.array:
    """
    https://www.learnpythonwithrune.org/numpy-calculate-the-julia-set-with-vectorization
    """
    # JC modifications
    # c is obtained from input
    point = Element('complex').value
    c = complex(point.replace(' ', '')) # remove whitespaces for complex conversion
    global julia_c  # declare global here
    if c == julia_c:
       xr, yr = ranges(['#jx0', '#jx1', '#jy0', '#jy1'])   # take the ranges from input
    else:
       julia_c = c         # update global and reset ranges
       xr, yr = putComplex(c)

    if debug: print(f'Julia at {c}, with x-range {xr} and y-range {yr}.')

    # (x,y) at the center of xr, yr
    # determine x, y from ranges,
    # determine zoom by (3 units)/(side), where side is the square that fits the selected rectangle.
    # max iterations is taken from input
    x = sum(xr)/2
    y = sum(yr)/2
    zoom = 3 / min (xr[1] - xr[0], yr[1] - yr[0])
    max_iterations = int(Element('jmax').value)
    # the original x = 0 is average of xr: Range = (-1.5, 1.5)
    # the original y = 0 is average of yr: Range = (-1.5, 1.5)
    # End JC modifications

    # To make navigation easier we calculate these values
    x_width, y_height = 1.5, 1.5 * height / width
    x_from, x_to = x - x_width / zoom, x + x_width / zoom
    y_from, y_to = y - y_height / zoom, y + y_height / zoom

    # Here the actual algorithm starts
    x = np.linspace(x_from, x_to, width).reshape((1, width))
    y = np.linspace(y_from, y_to, height).reshape((height, 1))
    z = x + 1j * y

    # Initialize z to all zero
    c = np.full(z.shape, c)

    # To keep track in which iteration the point diverged
    div_time = np.zeros(z.shape, dtype=int)

    # To keep track on which points did not converge so far
    m = np.full(c.shape, True, dtype=bool)
    for i in range(max_iterations):
        z[m] = z[m] ** 2 + c[m]
        m[np.abs(z) > 2] = False
        div_time[m] = i

    return div_time


# Drawing Julia set

# global here
jcurrent_image = None

async def draw_julia() -> None:
  spinner = document.querySelector("#julia .loading")
  canvas = document.querySelector("#julia canvas")

  spinner.style.display = ""
  canvas.style.display = "none"

  ctx = prepare_canvas(width, height, canvas)

  console.log("Computing Julia set ...")
  console.time("julia")
  iters = julia(width, height)
  console.timeEnd("julia")

  image = color_map(iters, Magma256)

  # must say global here, so that current_image is the outside one.
  global jcurrent_image
  jcurrent_image = image # update global
  draw_image(ctx, image)

  spinner.style.display = "none"
  canvas.style.display = "block"


# Handle changes in Julia set
jhandler = create_proxy(lambda _event: draw_julia())
document.querySelector("#julia fieldset").addEventListener("change", jhandler)

jcanvas = document.querySelector("#julia canvas")

# globals here, too
jis_selecting = False
jinit_sx, jinit_sy = None, None
jsx, jsy = None, None

async def jmousemove(event):
  global jis_selecting
  global jinit_sx
  global jinit_sy
  global jsx
  global jsy

  bds = jcanvas.getBoundingClientRect()
  event_sx, event_sy = event.clientX - bds.x, event.clientY - bds.y

  ctx = jcanvas.getContext("2d")

  pressed = event.buttons == 1
  if jis_selecting:
    if not pressed:
      xr, yr = ranges(['#jx0','#jx1','#jy0','#jy1'])
      # ignore if range is too small
      if (xr[1] - xr[0] < 2) or (yr[1] - yr[0] < 2):
         display('Julia selected?', target='point', append=False)
         return

      x0 = invert(jinit_sx, xr, (0, width))
      x1 = invert(jsx, xr, (0, width))
      y0 = invert(jinit_sy, yr, (0, height))
      y1 = invert(jsy, yr, (0, height))

      if debug: print(f'top-left: ({jinit_sx},{jinit_sy}), bottom-right: ({jsx},{jsy}) with original ranges: {xr}, {yr}, new ranges: ({x0}, {x1}), ({y0}, {y1}).')

      setRanges(['#jx0','#jx1','#jy0','#jy1'], (x0, x1), (y0, y1))

      jis_selecting = False
      jinit_sx, jinit_sy = None, None
      jsx, jsy = jinit_sx, jinit_sy

      await draw_julia()
    else:
      ctx.save()
      ctx.clearRect(0, 0, width, height)
      draw_image(ctx, jcurrent_image)
      jsx, jsy = event_sx, event_sy
      ctx.beginPath()
      ctx.rect(jinit_sx, jinit_sy, jsx - jinit_sx, jsy - jinit_sy)
      ctx.fillStyle = "rgba(255, 255, 255, 0.4)"
      ctx.strokeStyle = "rgba(255, 255, 255, 1.0)"
      ctx.fill()
      ctx.stroke()
      ctx.restore()
  else:
    if pressed:
      jis_selecting = True
      jinit_sx, jinit_sy = event_sx, event_sy
      jsx, jsy = jinit_sx, jinit_sy

jcanvas.addEventListener("mousemove", create_proxy(jmousemove))

# the click event is ignored
async def jreset(event):
    # Range([-1.5, 1.5]), Range([-1.5, 1.5])
    setRanges(['#jx0','#jx1','#jy0','#jy1'], (-1.5, 1,5), (-1.5, 1.5))
    await draw_julia()

# Note: py-click cannot accommodate an async function.
document.getElementById('jreset').addEventListener('click', create_proxy(jreset))


# main program
import asyncio

async def main():
    _ = await asyncio.gather(
        draw_mandelbrot(),
        draw_julia(),
      )

asyncio.ensure_future(main())
</py-script>
```

---

<!-- pandoc -s demo09.md -o demo09.html -->