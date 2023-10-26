---
title: Pyscript - Demo 8
header-includes: |
    <style>
       body { min-width: 90% !important; }
    </style>
include-after: |
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css"/>
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo01.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo01.html -->
---

# Pyscript - Fermat's Two Squares


Get the two squares of: <input id="input" class="py-input" value="97">
<button id="click-btn" class="py-button" py-click="go()">Go</button>

<py-terminal>Output terminal:</py-terminal>


Type your Python code (hover mouse/pointer to bottom right-end for Green arrow to run code):
<py-repl></py-repl>

<!-- pyscript -->
```{=html}
<py-script>
# Python has arbitrary-precision integer arithmetic
# Python version 3.8 has math.isqrt() to compute the (floor) integer square root
# Note: Python tuple is immutable, but list is mutable.
# Python functions can take a tuple and returns a (new) tuple.

from math import isqrt         # math.isqrt = integer square-root
from datetime import datetime  # datetime.datetime = now, difference c has c.total_seconds().
from time import time_ns       # time.time_ns gives timestamp to nanoseconds from epoch.
# Python in MacBook Air with M2 is too fast to detect runtime difference in this case.
from js import console         # for console.time('name') and console.timeEnd('name')

# Check if n is a square
def is_square(n):
    root = isqrt(n)
    return root * root == n

# Check if n is a tik, of the form 4k + 1
def is_tik(n):
    return False if n == 0 else n%4 == 1

# Flip of a triple
def flip(t):
    (x,y,z) = t
    return (x,z,y)

# Zagier of a triple
def zagier(t):
    (x,y,z) = t
    return      (x + 2 * z,z,y - z - x) if x < y - z \
           else (2 * y - x,y,x + z - y) if x < 2 * y \
           else (x - 2 * y,x + z - y,y)

# Check if triple is a Zagier fix
def is_zagier_fix(t):
    (x,y,z) = t
    return x == y

# Check if triple is a Flip fix
def is_flip_fix(t):
    (x,y,z) = t
    return y == z

# Iterative Algorithm
def iterating(n):
    assert is_tik(n), f'Input number {n} is not of the form 4k + 1'
    assert not is_square(n), f'Input number {n} is a square, not acceptable.'
    start = datetime.now()
    (x,y,z) = (1, 1, n // 4) # initial Zagier fix
    print((x,y,z), end='')
    count = 1
    while y != z:
        (x,y,z) = zagier (flip ((x,y,z)))
        print(' ➜', (x,y,z), end='')
        count += 1

    (u,v) = (x,y + z)
    stop = datetime.now()
    slip = stop - start
    assert u * u + v * v == n
    print()
    print(f'{n} = {u*u} + {v*v} = {u}² + {v}², with {count} nodes, time elapsed {slip}.')

# Hopping Algorithm
def hopping(n):
    assert is_tik(n), f'Input number {n} is not of the form 4k + 1'
    assert not is_square(n), f'Input number {n} is a square, not acceptable.'
    start = datetime.now()
    (x,y,z) = (1, n // 4, 1) # initial flip of Zagier fix
    c = isqrt(n)       # parameter = √n
    print((x,y,z), end='')
    hop = 0
    while y != z:
        m = (x + c) // (2 * z)                              # hop step
        (x,y,z) = (2 * m * z - x, z, y + m * x - m * m * z) # hop node
        print(' ▶', (x,y,z), end='')
        hop += 1

    (u,v) = (x,y + z)
    stop = datetime.now()
    slip = stop - start
    assert u * u + v * v == n
    print()
    print(f'{n} = {u*u} + {v*v} = {u}² + {v}², with {hop} hops, time elapsed {slip}.')

# Handle button Go
def go():
    value = Element('input').value

    print("Fermat's two squares by iteration:")
    console.log("ermat's two squares by iteration ...")
    console.time("iteration")
    iterating(int(value))
    console.timeEnd("iteration")

    print("Fermat's two squares by hopping:")
    console.log("ermat's two squares by hopping ...")
    console.time("hopping")
    hopping(int(value))
    console.timeEnd("hopping")

</py-script>
```
---

<!-- pandoc -s demo08.md -o demo08.html -->