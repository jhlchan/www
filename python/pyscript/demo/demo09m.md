---
title: Pyscript - Demo 9M
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

        .param {
            display: flex;
            flex-direction: column;
            width: 600px;
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
    </style>
include-after: |
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css"/>
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo09m.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo09m.html -->
---

# Pyscript - Mandelbrot Set

## Static Pictures

![Mandelbrot set](https://files.realpython.com/media/plot_mandelbrot_with_circle.ad8b99d3ee01.png){ width=48% }

![Mandelbrot set from vector computations](https://blogs.sas.com/content/iml/files/2019/07/Mandelbrot1.png){ width=48% }


## Interactive Canvas
<!-- output target -->

<!--
```{=html}
<div style="display: flex; flex-direction: column; gap: 1em; width: 600px;">
    <div id="mandelbrot">
        <div style="text-align: center">Mandelbrot set</div>
            <div class="loading"></div>
            <canvas></canvas>
    </div>
</div>
```
-->

::::::{#mandelbrot .param}

<fieldset class="inrow">

[max number of iteration = ]{.nobreak}
<input id="max" type="text" class="py-input" value="100">

::::{.inrow}

[x range = &lbrack;]{.nobreak}
<input id="x0" type="text" class="numbox" value="-2">

[, ]{.nobreak}
<input id="x1" type="text" class="numbox" value="1">

[&rbrack;]{.nobreak}

::::

::::{.inrow}

[y range = &lbrack;]{.nobreak}
<input id="y0" type="text" class="numbox" value="-1.5">

[, ]{.nobreak}
<input id="y1" type="text" class="numbox" value="1.5">

[&rbrack;]{.nobreak}

<button id="reset" class="py-button">Reset</button>

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

Vectorize the computation of the Mandelbrot set in a matrix language
by Rick Wicklin, July 29, 2019 
https://blogs.sas.com/content/iml/2019/07/29/vectorize-computation-mandelbrot-set.html
https://blogs.sas.com/content/iml/files/2019/07/Mandelbrot1.png

The classical algorithm for the Mandelbrot set

As a reminder, the Mandelbrot set is a visualization of a portion of the complex plane. If c is a complex number, you determine the color for c by iterating a complex quadratic map z <- z2 + c, starting with z=0. You keep track of how many iterations it takes before the iteration diverges to infinity, which in practice means that |z| exceeds some radius, such as 5. The parameter values for which the iteration remains bounded belong to the Mandelbrot set. Other points are colored according to the number of iterations before the trajectory exceeded the specified radius.

 The classical computation of the Mandelbrot set iterates over the parameter values in a grid, as follows:

For each value c in a grid:
   Set z = 0
   For i = 1 to MaxIter:
      Apply the quadratic map, f, to form the i_th iteration, z_i = f^i(z; c).
      If z_i > radius, stop and remember the number of iterations.
   End;
   If the trajectory did not diverge, assume parameter value is in the Mandelbrot set.
End;

An advantage of this algorithm is that it does not require much memory, so it was great for the PCs of the 1980s! For each parameter, the color is determined (and often plotted), and then the parameter is never needed again. 

A vectorized algorithm for the Mandelbrot set

In the classical algorithm, all computations are scalar computations. The outer loop is typically over a large number, K, of grid points. The maximum number of iterations is typically 100 or more. Thus, the algorithm performs 100*K scalar computations in order to obtain the colors for the image. For a large grid that contains K=250,000 parameters, that's 25 million scalar computations for the low-memory algorithm.

A vectorized version of this algorithm inverts the two loops. Instead of looping over the parameters and iterating each associated quadratic map, you can store the parameter values in a grid and iterate all K trajectories at once by applying the quadratic map in a vectorized manner. The vectorized algorithm is: 

Define c to be a large grid of parameters.
Initialize a large grid z = 0, which will hold the current state.
For i = 1 to MaxIter:
   For all points that have not yet diverged:
      Apply the quadratic map, f, to z to update the current state.
      If any z > radius, assign the number of iterations for those parameters.
   End;
End;
If a trajectory did not diverge, assume parameter value is in the Mandelbrot set.

The vectorized algorithm performs the same computations as the scalar algorithm, but each iteration of the quadratic map operates on a huge number of current states (z). Also, each all states are checked for divergence by using a single call to a vector operation. There are many fewer function calls, which reduces overhead costs, but the vectorized program uses a lot of memory to store all the parameters and states. 


mandelbrot at (-0.5,0), with x-range (-2.5, 2.5) and y-range (-5.0, 5.0).
top-left: (0.5,3.0833282470703125), bottom-right: (597.5,404.0833282470703) with original ranges: (-2.5, 2.5), (-5.0, 5.0), new ranges: (-2.495833333333333, 2.4791666666666665), (-4.948611195882162, 1.7347221374511719).
mandelbrot at (-0.5,0), with x-range (-2.495833333333333, 2.4791666666666665) and y-range (-4.948611195882162, 1.7347221374511719).

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
def ranges():
  x0_in = document.querySelector("#x0")
  x1_in = document.querySelector("#x1")
  y0_in = document.querySelector("#y0")
  y1_in = document.querySelector("#y1")

  xr = (float(x0_in.value), float(x1_in.value))
  yr = (float(y0_in.value), float(y1_in.value))

  return xr, yr

# set ranges
def setRanges(xr, yr):
    document.querySelector("#x0").value = xr[0]
    document.querySelector("#x1").value = xr[1]
    document.querySelector("#y0").value = yr[0]
    document.querySelector("#y1").value = yr[1]

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
    xr, yr = ranges()
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
    max_iterations = int(Element('max').value)
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
current_image = None

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
  global current_image
  current_image = image
  draw_image(ctx, image)

  spinner.style.display = "none"
  canvas.style.display = "block"


# Handle changes in Mandelbrot set
handler = create_proxy(lambda _event: draw_mandelbrot())
document.querySelector("#mandelbrot fieldset").addEventListener("change", handler)

canvas = document.querySelector("#mandelbrot canvas")

# globals here, too
is_selecting = False
init_sx, init_sy = None, None
sx, sy = None, None

async def mousemove(event):
  global is_selecting
  global init_sx
  global init_sy
  global sx
  global sy

  def invert(sx, source_range, target_range):
    source_start, source_end = source_range
    target_start, target_end = target_range
    factor = (target_end - target_start)/(source_end - source_start)
    offset = -(factor * source_start) + target_start
    # avoid ZeroDivisionError: float division by zero
    return (sx - offset) / factor

  bds = canvas.getBoundingClientRect()
  event_sx, event_sy = event.clientX - bds.x, event.clientY - bds.y

  ctx = canvas.getContext("2d")

  pressed = event.buttons == 1
  if is_selecting:
    if not pressed:
      xr, yr = ranges()
      # ignore if range is zero
      if max(xr) == min(xr): return
      if max(yr) == min(yr): return

      x0 = invert(init_sx, xr, (0, width))
      x1 = invert(sx, xr, (0, width))
      y0 = invert(init_sy, yr, (0, height))
      y1 = invert(sy, yr, (0, height))

      if debug: print(f'top-left: ({init_sx},{init_sy}), bottom-right: ({sx},{sy}) with original ranges: {xr}, {yr}, new ranges: ({x0}, {x1}), ({y0}, {y1}).')
      # when selecting upper right:
      # top-left: (254.5,102.08332824707031), bottom-right: (507.5,270.0833282470703)
      # with original ranges: (-2.5, 2.5), (-5.0, 5.0),
      # new ranges: (-0.37916666666666665, 1.7291666666666667), (-3.2986111958821613, -0.49861119588216146).

      setRanges((x0, x1), (y0, y1))

      is_selecting = False
      init_sx, init_sy = None, None
      sx, sy = init_sx, init_sy

      await draw_mandelbrot()
    else:
      ctx.save()
      ctx.clearRect(0, 0, width, height)
      draw_image(ctx, current_image)
      sx, sy = event_sx, event_sy
      ctx.beginPath()
      ctx.rect(init_sx, init_sy, sx - init_sx, sy - init_sy)
      ctx.fillStyle = "rgba(255, 255, 255, 0.4)"
      ctx.strokeStyle = "rgba(255, 255, 255, 1.0)"
      ctx.fill()
      ctx.stroke()
      ctx.restore()
  else:
    if pressed:
      is_selecting = True
      init_sx, init_sy = event_sx, event_sy
      sx, sy = init_sx, init_sy

canvas.addEventListener("mousemove", create_proxy(mousemove))

# the click event is ignored
async def reset(event):
    # Range([-2, 1]), Range([-1.5, 1.5])
    setRanges((-2, 1), (-1.5, 1.5))
    await draw_mandelbrot()

# Note: py-click cannot accommodate an async function.
btn = document.getElementById('reset')
btn.addEventListener('click', create_proxy(reset))


import asyncio

async def main():
  await draw_mandelbrot()

asyncio.ensure_future(main())
</py-script>
```

<!--
:::{#picture .param}
<canvas></canvas>
:::


  # draw another one
  canvas2 = document.querySelector("#picture canvas")
  canvas2.style.display = "none"
  ctx2 = prepare_canvas(width, height, canvas2)
  # x: -0.5 to 0 shifts left : 0 to 0.5 shifts up, zoom: 1.5 magnifies, max_iterations = 100 seems good
  iters2 = mandelbrot(width, height, x = 0, y = 0, zoom = 1.5)
  image2 = color_map(iters2, Magma256)
  draw_image(ctx2, image2)
  canvas2.style.display = "block"
-->


---

<!-- pandoc -s demo09m.md -o demo09m.html -->