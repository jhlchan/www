---
title: Pyscript - Demo 9J
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
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo09j.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo09j.html -->
---

# Pyscript - Julia set

## Examples

![Julia set at c = 0.285+0.01j](https://miro.medium.com/v2/resize:fit:1144/format:webp/1*ZYCMeaEp4BHkZCbG5fhHlA.png)

![Julia set at c = -0.835-0.2321j](https://miro.medium.com/v2/resize:fit:1144/format:webp/1*dcPxPvO5YgOFaxaqpJ1k8g.png)

## Playground
<!-- output target -->

<!--
```{=html}
<div style="display: flex; flex-direction: column; gap: 1em; width: 600px;">
    <div id="julia">
        <div style="text-align: center">Julia set</div>
        <div>
            <div class="loading"></div>
            <canvas></canvas>
        </div>
    </div>
</div>
```
-->

::::::{#julia .param}

<fieldset class="inrow">

[complex number c = ]{.nobreak}
<input id="complex" type="text" class="py-input" value="-0.4 + 0.6j">

[max number of iteration = ]{.nobreak}
<input id="max" type="text" class="py-input" value="100">

::::{.inrow}

[x range = &lbrack;]{.nobreak}
<input id="x0" type="text" class="numbox" value="-1.5">

[, ]{.nobreak}
<input id="x1" type="text" class="numbox" value="1.5">

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
The Julia Set
The Mandelbrot Set’s Less Famous Sibling
Y. Natsume, 10 November 2021.
https://www.cantorsparadise.com/the-julia-set-e03c29bed3d0

The Julia set is one of the most beautiful fractals to have been discovered. Named after the esteemed French mathematician Gaston Julia, the Julia set expresses a complex and rich set of dynamics, giving rise to a wide range of breathtaking visuals. Also as we shall see later on, the Julia set is related to the much more famous Mandelbrot set!

In this article, we will explore how to use Python to create the Julia set!

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

# Convert data array to color array using palette
def color_map(array: np.array, palette: np.array) -> np.array:
    size, _ = palette.shape
    index = (array/array.max()*(size - 1)).round().astype("uint8")

    width, height = array.shape
    image = np.full((width, height, 4), 0xff, dtype=np.uint8)
    image[:, :, :3] = palette[index]

    return image

# Draw image on the canvas
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


# global parameter of c for Julia set
julia_c = -0.4 + 0.6j  # a complex number, parser will remove spaces

    
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
    global julia_c
    point = Element('complex').value
    c = complex(point.replace(' ', '')) # remove whitespaces for complex conversion
    if c == julia_c:
       xr, yr = ranges()   # take the ranges from input
    else:
       julia_c = c         # update global and reset ranges
       # pass a list argument to tuple, otherwise
       # TypeError: tuple expected at most 1 argument, got 2
       xr, yr = Range([-1.5, 1.5]), Range([-1.5, 1.5])
       setRanges(xr, yr)

    if debug: print(f'Julia at {c}, with x-range {xr} and y-range {yr}.')

    # (x,y) at the center of xr, yr
    # determine x, y from ranges,
    # determine zoom by (3 units)/(side), where side is the square that fits the selected rectangle.
    # max iterations is taken from input
    x = sum(xr)/2
    y = sum(yr)/2
    zoom = 3 / min (xr[1] - xr[0], yr[1] - yr[0])
    max_iterations = int(Element('max').value)
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
current_image = None

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
  global current_image
  current_image = image
  draw_image(ctx, image)

  spinner.style.display = "none"
  canvas.style.display = "block"

# Handle changes in Julia set
handler = create_proxy(lambda _event: draw_julia())
document.querySelector("#julia fieldset").addEventListener("change", handler)

canvas = document.querySelector("#julia canvas")

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

      setRanges((x0,x1), (y0, y1))

      is_selecting = False
      init_sx, init_sy = None, None
      sx, sy = init_sx, init_sy

      await draw_julia()
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
    # Range([-1.5, 1.5]), Range([-1.5, 1.5])
    setRanges((-1.5, 1,5), (-1.5, 1.5))
    await draw_julia()

# Note: py-click cannot accommodate an async function.
btn = document.getElementById('reset')
btn.addEventListener('click', create_proxy(reset))


import asyncio

async def main():
  await draw_julia()

asyncio.ensure_future(main())
</py-script>
```

---

<!-- pandoc -s demo09j.md -o demo09j.html -->