---
title: Pyscript - Demo 1
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

# Pyscript - Computing Primes

[Python version: ]{#output}


Get primes up to: <input id="input" class="py-input" value="100">
<button id="click-btn" class="py-button" py-click="handle_click()">Go</button>


<py-terminal>Output terminal:</py-terminal>


Type your Python code (hover mouse/pointer to bottom right-end for Green arrow to run code):
<py-repl></py-repl>

<!-- pyscript -->
```{=html}
<py-script>
from datetime import datetime
import sys
import math

def show_info():
    display(sys.version, target="output")
    display('Current date and time from Python:', target="output")
    now = datetime.now()
    display(now.strftime("%m/%d/%Y, %H:%M:%S"), target="output")

def primes_to(n):
    primes = []
    primes.append(2) # the only even prime
    for num in range(3,n + 1,2): # all odd primes <= n, from 3, step 2
        if all (num%j != 0 for j in range(3,int(math.sqrt(num))+1,2)):
            primes.append(num) # pick up the odd prime

    return primes

def handle_click():
    input = Element("input")
    limit = int(input.value) # string to int
    # display(primes_to(limit), target="output") 
    print(f'Primes up to {limit}:')
    print(primes_to(limit)) 

# main
show_info()
</py-script>
```
---

<!-- pandoc -s demo01.md -o demo01.html -->