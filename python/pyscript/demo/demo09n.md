---
title: Pyscript - Demo 9N
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
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo09n.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo09n.html -->
---

# Pyscript - Drill into Fractal

<!-- output target -->
## Fractal

<!--
```{=html}
<div id="newton" class="param">
    <div class="tcenter">Newton set</div>
    <fieldset class="inrow">
        <span class="nobreak">p(z) = </span>
        <input id="poly" type="text" value="z**3 - 2*z + 2" />
        <span class="nobreak">a = </span>
        <input id="coef" type="text" value="1" class="twidth" />
        <div class="inrow">
            <span class="nobreak">x = [</span>
            <input id="x0" type="text" value="-2.5" class="numbox" />
            <span class="nobreak">, </span>
            <input id="x1" type="text" value="2.5" class="numbox" />
            <span class="nobreak">]</span>
        </div>
        <div class="inrow">
            <span class="nobreak">y = [</span>
            <input id="y0" type="text" value="-5.0" class="numbox" />
            <span class="nobreak">, </span>
            <input id="y1" type="text" value="5.0"  class="numbox" />
            <span class="nobreak">]</span>
        </div>
        <div class="inrow">
            <div class="nobreak">
                <input id="conv" type="radio" name="type" value="convergence" checked /> convergence
            </div>
            <div class="nobreak">
                <input id="iter" type="radio" name="type" value="iterations" /> iterations
            </div>
        </div>
    </fieldset>
    <div class="loading"></div>
    <canvas></canvas>
</div>
```
-->

::::::{#newton .param}

:::::{.tcenter}
__Newton set__
:::::

<fieldset class="inrow">

[p(z) = ]{.nobreak}
<input id="poly" type="text" class="py-input" value="z**3 - 2*z + 2">

[a = ]{.nobreak}
<input id="coef" type="text" class="twidth" value="1">

::::{.inrow}

[x = &lbrack;]{.nobreak}
<input id="x0" type="text" class="numbox" value="-2.5">

[, ]{.nobreak}
<input id="x1" type="text" class="numbox" value="2.5">

[&rbrack;]{.nobreak}

::::

::::{.inrow}

[y = &lbrack;]{.nobreak}
<input id="y0" type="text" class="numbox" value="-5.0">

[, ]{.nobreak}
<input id="y1" type="text" class="numbox" value="5.0">

[&rbrack;]{.nobreak}

::::

::::{.inrow}

:::{.nobreak}
<input id="conv" type="radio" name="type" value="convergence" checked /> convergence
:::
&nbsp;&nbsp;&nbsp;

:::{.nobreak}
<input id="iter" type="radio" name="type" value="iterations" /> iterations
:::
::::

</fieldset>

:::::{.loading}
:::::

<canvas></canvas>

::::::



Type your Python code (hover mouse/pointer to bottom right-end for Green arrow to run code):
<py-repl></py-repl>

<!--

Polynomial
<class 'numpy.polynomial.polynomial.Polynomial'>

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

from numpy.polynomial import Polynomial
from examples.palettes import Magma256

def prepare_canvas(width: int, height: int, canvas: Element) -> Context2d:
    ctx = canvas.getContext("2d")

    canvas.style.width = f"{width}px"
    canvas.style.height = f"{height}px"

    canvas.width = width
    canvas.height = height

    ctx.clearRect(0, 0, width, height)

    return ctx

def color_map(array: np.array, palette: np.array) -> np.array:
    size, _ = palette.shape
    index = (array/array.max()*(size - 1)).round().astype("uint8")

    width, height = array.shape
    image = np.full((width, height, 4), 0xff, dtype=np.uint8)
    image[:, :, :3] = palette[index]

    return image

def draw_image(ctx: Context2d, image: np.array) -> None:
  data = Uint8ClampedArray.new(to_js(image.tobytes()))
  width, height, _ = image.shape
  image_data = ImageData.new(data, width, height)
  ctx.putImageData(image_data, 0, 0)

width, height = 600, 600

# Newton set
Range = tuple[float, float]

def newton(
    width: int,
    height: int,
    *,
    p: Polynomial,
    a: complex,
    xr: Range = (-2.5, 1),
    yr: Range = (-1, 1),
    max_iterations: int = 100
) -> tuple[np.array, np.array]:
    """ """
    # To make navigation easier we calculate these values
    x_from, x_to = xr
    y_from, y_to = yr

    # Here the actual algorithm starts
    x = np.linspace(x_from, x_to, width).reshape((1, width))
    y = np.linspace(y_from, y_to, height).reshape((height, 1))
    z = x + 1j * y

    # Compute the derivative
    dp = p.deriv()

    # Compute roots
    roots = p.roots()
    epsilon = 1e-5

    # Set the initial conditions
    a = np.full(z.shape, a)

    # To keep track in which iteration the point diverged
    div_time = np.zeros(z.shape, dtype=int)

    # To keep track on which points did not converge so far
    m = np.full(a.shape, True, dtype=bool)

    # To keep track which root each point converged to
    r = np.full(a.shape, 0, dtype=int)

    for i in range(max_iterations):
        z[m] = z[m] - a[m] * p(z[m]) / dp(z[m])

        for j, root in enumerate(roots):
            converged = (np.abs(z.real - root.real) < epsilon) & (
                np.abs(z.imag - root.imag) < epsilon
            )
            m[converged] = False
            r[converged] = j + 1

        div_time[m] = i

    return div_time, r


# Drawing Newton set
def ranges():
  x0_in = document.querySelector("#x0")
  x1_in = document.querySelector("#x1")
  y0_in = document.querySelector("#y0")
  y1_in = document.querySelector("#y1")

  xr = (float(x0_in.value), float(x1_in.value))
  yr = (float(y0_in.value), float(y1_in.value))

  return xr, yr

current_image = None

async def draw_newton() -> None:
  spinner = document.querySelector("#newton .loading")
  canvas = document.querySelector("#newton canvas")

  spinner.style.display = ""
  canvas.style.display = "none"

  ctx = prepare_canvas(width, height, canvas)

  console.log("Computing Newton set ...")

  poly_in = document.querySelector("#poly")
  coef_in = document.querySelector("#coef")
  conv_in = document.querySelector("#conv")
  iter_in = document.querySelector("#iter")

  xr, yr = ranges()

  # z**3 - 1
  # z**8 + 15*z**4 - 16
  # z**3 - 2*z + 2

  expr = sympy.parse_expr(poly_in.value)
  coeffs = [ complex(c) for c in reversed(sympy.Poly(expr, sympy.Symbol("z")).all_coeffs()) ]
  poly = np.polynomial.Polynomial(coeffs)

  coef = complex(sympy.parse_expr(coef_in.value))

  console.time("newton")
  iters, roots = newton(width, height, p=poly, a=coef, xr=xr, yr=yr)
  console.timeEnd("newton")

  if conv_in.checked:
    n = poly.degree() + 1
    k = int(len(Magma256)/n)

    colors = Magma256[::k, :][:n]
    colors[0, :] = [255, 0, 0] # red: no convergence

    image = color_map(roots, colors)
  else:
    image = color_map(iters, Magma256)

  global current_image
  current_image = image
  draw_image(ctx, image)

  spinner.style.display = "none"
  canvas.style.display = "block"

# Handle changes in Newton set
handler = create_proxy(lambda _event: draw_newton())
document.querySelector("#newton fieldset").addEventListener("change", handler)

canvas = document.querySelector("#newton canvas")

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
    return (sx - offset) / factor

  bds = canvas.getBoundingClientRect()
  event_sx, event_sy = event.clientX - bds.x, event.clientY - bds.y

  ctx = canvas.getContext("2d")

  pressed = event.buttons == 1
  if is_selecting:
    if not pressed:
      xr, yr = ranges()

      x0 = invert(init_sx, xr, (0, width))
      x1 = invert(sx, xr, (0, width))
      y0 = invert(init_sy, yr, (0, height))
      y1 = invert(sy, yr, (0, height))

      print(f'top-left: ({init_sx},{init_sy}), bottom-right: ({sx},{sy}) with original ranges: {xr}, {yr}, new ranges: ({x0}, {x1}), ({y0}, {y1}).')
      # top-left: (87.5,204.0833282470703), bottom-right: (431.5,414.0833282470703)
      # with original ranges: (-2.5, 2.5), (-5.0, 5.0),
      #           new ranges: (-1.7708333333333333, 1.0958333333333334), (-1.5986111958821614, 1.9013888041178386).
      document.querySelector("#x0").value = x0
      document.querySelector("#x1").value = x1
      document.querySelector("#y0").value = y0
      document.querySelector("#y1").value = y1

      is_selecting = False
      init_sx, init_sy = None, None
      sx, sy = init_sx, init_sy

      await draw_newton()
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

import asyncio

async def main():
  await draw_newton()

asyncio.ensure_future(main())
</py-script>
```

---

<!-- pandoc -s demo09n.md -o demo09n.html -->