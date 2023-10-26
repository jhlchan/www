---
title: Pyscript - Demo 11A
header-includes: |
    <style>
       body { min-width: 90% !important; }
    </style>
    <style>
        .centre {
          text-align: centre;
        }
        .board {
          border: 1px solid black;
          margin: auto;
          width: 60%;
          zwidth: 780px;
        }
        .cell {
          background: green;
          border: 1px solid black;
          width: 80px;
          height: 80px;
        }
        .black {
           border-radius: 50%;
           height: 38px;
           width: 38px;
           border: 2px solid #484848;
           background: black;
         }
        .white {
           border-radius: 50%;
           height: 38px;
           width: 38px;
           border: 2px solid #484848;
           background: white;
         }
         .hide {
            display: none;
         }
    </style>
include-after: |
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css"/>
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo11a.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo11a.html -->
---

# Pyscript - Game for 2 Players

## Pyscript Othello!{#header .centre}

:::{#game .board }
:::

Type your Python code (hover mouse/pointer to bottom right-end for Green arrow to run code):
<py-repl></py-repl>

<!--
srepmub / Pyscript-Othello-Board /pyscript_othello.html
https://github.com/srepmub/Pyscript-Othello-Board/blob/main/pyscript_othello.html

-->

<!-- pyscript -->
:::{ .hide }
```{=html}
<py-script>
from js import document
from pyodide.ffi import create_proxy

# neighbours of a piece
directions = [(1, 1), (-1, 1), (0, 1), (1, -1), (-1, -1), (0, -1), (1, 0), (-1, 0)]

# get cell (x,y)
def cell(x, y):
    return document.getElementById(f'{x}_{y}')

# put a piece at (x,y) with color
def do_flip(x, y, color):
    cell(x, y).color = color
    img = document.getElementById(f'img{x}_{y}')
    # match piece with correct color
    if color == 'white':
        img.classList.remove('black')    
        img.classList.add('white')
    else:
        img.classList.remove('white')    
        img.classList.add('black')

# put a piece at neighbour of (x,y)
def flip_in_direction(x, y, direction):
    dx, dy = direction
    other_color = False
    while True:
        x, y = x + dx, y + dy
        if x not in range(8) or y not in range(8):
            return False

        c = cell(x, y)
        if c.color == 'empty':
            return False
        if c.color != color:
            other_color = True
        else:
            return other_color

# flip any stone caused by the move
def flip_stones(move):
    mx, my = move
    for direction in directions:
        if flip_in_direction(mx, my, direction):
             dx, dy = direction
             x, y = mx + dx, my + dy
             while cell(x, y).color != color:
                 do_flip(x, y, color)  # color = current player
                 x, y = x + dx, y + dy

    do_flip(mx, my, color)

# check if a move at (x,y) is possible
def possible_move(x, y):
    c = cell(x, y)
    if c.color == 'empty':
        for direction in directions:
            if flip_in_direction(x, y, direction):
                return True

# title for warning
title = document.getElementById('header')

# handle click on a cell
def on_click(e):
    global color
    if e.target.id.startswith('img'):
        title.innerHTML = 'ILLEGAL!'
        title.style.background = 'red'
    else:
        x, y = [int(i) for i in e.target.id.split('_')]
        if possible_move(x, y):
            flip_stones((x, y))
            color = 'black' if color == 'white' else 'white'
            title.innerHTML = 'Othello'
            title.style.background = ''
        else:
            title.innerHTML = 'ILLEGAL!'
            title.style.background = 'red'

# make the game board
game = document.getElementById('game')
cells = document.createElement('table')
cells.id = 'board'
game.appendChild(cells)

# make the board cells
for i in range(8):
    tr = document.createElement('tr')
    for j in range(8):
        td = document.createElement('td')
        td.id = f'{i}_{j}'
        td.classList.add('cell')
        td.align = 'center'
        td.color = 'empty'
        img = document.createElement('img')
        img.id = f'img{i}_{j}'
        td.appendChild(img)
        tr.appendChild(td)
        td.addEventListener('click', create_proxy(on_click))

    cells.appendChild(tr)

# initial game pieces
do_flip(3, 3, 'white')
do_flip(4, 4, 'white')
do_flip(3, 4, 'black')
do_flip(4, 3, 'black')

# black play first
color = 'black'
</py-script>
```
:::

---

<!-- pandoc -s demo11a.md -o demo11a.html -->