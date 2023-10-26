---
title: Pyscript - Demo 11
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
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo11.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo11.html -->
---

# Pyscript - Game for 2 Players

## Pyscript Othello!{#header .centre}

:::{#game .board }
:::

<py-terminal id="debug"></py-terminal>

Type your Python code (hover mouse/pointer to bottom right-end for Green arrow to run code):
<py-repl></py-repl>

<!--
srepmub / Pyscript-Othello-Board /pyscript_othello.html
https://github.com/srepmub/Pyscript-Othello-Board/blob/main/pyscript_othello.html

REVERSI OTHELLO (PYTHON RECIPE)
Reversi/Othello Board Game using Minimax, Alpha-Beta Pruning, Negamax, Negascout algorithms.
https://code.activestate.com/recipes/580698-reversi-othello/

These two systems have different conventions for the coordinates:

+--+--+--+--+--+--+--+--+
|  |  |  |  |  |  |  |  |  0
+--+--+--+--+--+--+--+--+
|  |  |  |  |  |  |  |  |  1
+--+--+--+--+--+--+--+--+
|  |  |  |? |  |  |  |  |  2
+--+--+--+--+--+--+--+--+
|  |  |  |o |x |  |  |  |  3
+--+--+--+--+--+--+--+--+
|  |  |  |x |o |  |  |  |  4
+--+--+--+--+--+--+--+--+
|  |  |  |  |  |  |  |  |  5
+--+--+--+--+--+--+--+--+
|  |  |  |  |  |  |  |  |  6
+--+--+--+--+--+--+--+--+
|  |  |  |  |  |  |  |  |  7
+--+--+--+--+--+--+--+--+
 0   1  2  3  4  5  6  7 

Second one to first one: 0 = empty, 1 = black, 2 = white.
The location ? for first one is: X = 2, Y = 3, for second one is: X = 3, Y = 2.
For consistency, with the minimal change, all we need to do is:
(1) flip the ids for cell and image when creating them in the GUI.
(2) flip (x,y) when updating the board by GUI in do_flip.
-->

<!-- pyscript -->
:::{ .hide }
```{=html}
<py-script>
from js import document
from pyodide.ffi import create_proxy

# modify input (This works, prompt with text!)
input = js.prompt

# logging
debug = True
# debug = False

if not debug: document.getElementById('debug').style = 'display: none'

# number of human players
nplayers = 2   # game just checks valid move
# nplayers = 1   # game is human vs AI
# nplayers = 0   # game is AI vs AI
# Is it possible for the game to play according to a move script?

# neighbours of a piece
directions = [(1, 1), (-1, 1), (0, 1), (1, -1), (-1, -1), (0, -1), (1, 0), (-1, 0)]

#########################
# The AI move algorithm #
#########################
import copy  # for deepcopy

# the board representation as 2x2 matrix
n = 8 # board size (must be even)
board = [['0' for x in range(n)] for y in range(n)]

# 8 directions for any even n
dirx = [-1, 0, 1, -1, 1, -1, 0, 1]
diry = [-1, -1, -1, 0, 0, 1, 1, 1]
# ordering is different from directions, should not be important

# initialise the board
def InitBoard():
    p = n // 2 - 1    # integer division
    q = n - 1 - p     # for n = 8, p = 3, q = 4
    board[p][p] = '2'
    board[q][p] = '1'        
    board[p][q] = '1'
    board[q][q] = '2'

# print the board with rows and column numbered
def PrintBoard():
    m = len(str(n - 1))
    for y in range(n):
        row = ''
        for x in range(n):
            row += board[y][x]
            row += ' ' * m
        print(row, y)
    print(' ' * (m + 1) * n + ' Y')
    row = '' # last row of column indices
    for x in range(n):
        row += str(x).zfill(m) + ' '
    print(row + ' X\n')

# make a move on the board, at (x,y) by player
def MakeMove(board, x, y, player): # assuming valid move
    total = 0 # total number of opponent pieces taken
    board[y][x] = player
    for d in range(8): # 8 directions
        count = 0

        for i in range(n):
            dx = x + dirx[d] * (i + 1)
            dy = y + diry[d] * (i + 1)
            if dx < 0 or dx >= n or dy < 0 or dy >= n:
                count = 0; break
            elif board[dy][dx] == player:
                break
            elif board[dy][dx] == '0':
                count = 0; break
            else:
                count += 1

        for i in range(count):
            dx = x + dirx[d] * (i + 1)
            dy = y + diry[d] * (i + 1)
            board[dy][dx] = player

        total += count

    # board is modified
    return (board, total)

# check if move (x,y) is valid for player
def ValidMove(board, x, y, player):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if board[y][x] != '0':
        return False
    _ , total = MakeMove(copy.deepcopy(board), x, y, player)
    return total != 0

# board evaluation
minEvalBoard = -1                    # min - 1
maxEvalBoard = n * n + 4 * n + 4 + 1 # max + 1

# evaluate the board for player
def EvalBoard(board, player):
    score = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] == player:
                if (x == 0 or x == n - 1) and (y == 0 or y == n - 1):
                    score += 4 # corner
                elif (x == 0 or x == n - 1) or (y == 0 or y == n - 1):
                    score += 2 # side
                else:
                    score += 1
    return score

# check if no valid move is possible
def IsTerminalNode(board, player):
    for y in range(n):
        for x in range(n):
            if ValidMove(board, x, y, player):
                return False
    return True

# get a list of sorted nodes
def GetSortedNodes(board, player):
    sortedNodes = []
    for y in range(n):
        for x in range(n):
            if ValidMove(board, x, y, player):
                boardTemp, _ = MakeMove(copy.deepcopy(board), x, y, player)
                sortedNodes.append((boardTemp, EvalBoard(boardTemp, player)))
    sortedNodes = sorted(sortedNodes, key = lambda node: node[1], reverse = True)
    sortedNodes = [node[0] for node in sortedNodes]
    return sortedNodes

# compute the best move by a player
def BestMove(board, player):
    maxPoints = 0
    mx, my = (-1, -1)
    for y in range(n):
        for x in range(n):
            if ValidMove(board, x, y, player):
                boardTemp, _ = MakeMove(copy.deepcopy(board), x, y, player)
                '''
                if opt == 0:
                    points = EvalBoard(boardTemp, player)
                elif opt == 1:
                    points = Minimax(boardTemp, player, depth, True)
                elif opt == 2:
                    points = AlphaBeta(board, player, depth, minEvalBoard, maxEvalBoard, True)
                elif opt == 3:
                    points = Negamax(boardTemp, player, depth, 1)
                elif opt == 4:
                    points = NegamaxAB(boardTemp, player, depth, minEvalBoard, maxEvalBoard, 1)
                elif opt == 5:
                    points = Negascout(boardTemp, player, depth, minEvalBoard, maxEvalBoard, 1)
                elif opt == 6:
                    points = AlphaBetaSN(board, player, depth, minEvalBoard, maxEvalBoard, True)
                elif opt == 7:
                    points = NegamaxABSN(boardTemp, player, depth, minEvalBoard, maxEvalBoard, 1)
                elif opt == 8:
                    points = NegascoutSN(boardTemp, player, depth, minEvalBoard, maxEvalBoard, 1)
                '''
                points = EvalBoard(boardTemp, player)
                if points > maxPoints:
                    maxPoints = points
                    mx, my = (x, y)

    return (mx, my)

# play the game (text version) for m moves
def othello(m):
    print('Players: 1 = User,  2 = AI\n')
    InitBoard()
    # while True:
    global board
    step = 0
    while step < m:
        step += 1 
        for player in ['1', '2']:
            print()
            PrintBoard()
            print(f'PLAYER: {player}')
            if IsTerminalNode(board, player):
                print('Player cannot play! Game ended!')
                print(f"Score User: {EvalBoard(board, '1')}")
                print(f"Score AI  : {EvalBoard(board, '2')}")
                step = m
                break      
            if player == '1': # user's turn
                x, y = BestMove(board, player)
                if not (x == -1 and y == -1):
                    board, total = MakeMove(board, x, y, player)
                    print(f'User played (X Y): {x} {y}')
                    print(f'# of pieces taken: {total}')
            else: # AI's turn
                x, y = BestMove(board, player)
                if not (x == -1 and y == -1):
                    board, total = MakeMove(board, x, y, player)
                    print(f'AI played (X Y): {x} {y}')
                    print(f'# of pieces taken: {total}')

# play 3 steps
# othello(3)

# Use AI algorithm for a player move
def ai_move(player):
    global board
    x, y = BestMove(board, player)
    if not (x == -1 and y == -1):
       board, total = MakeMove(board, x, y, player)
       print(f'AI played (X Y): {x} {y}')
       print(f'# of pieces taken: {total}')               
    return (x, y)

#########################
# The GUI Interface     #
#########################

# state mapping between the two versions
def state(color):
    if color == 'empty': return '0'
    if color == 'black': return '1'
    if color == 'white': return '2'
    return '?'

# get cell (x,y)
def cell(x, y):
    return document.getElementById(f'{x}_{y}')

# get shape (x,y)
def shape(x, y):
    return document.getElementById(f'img{x}_{y}')

# put a piece at (x,y) with color
def do_flip(x, y, color):
    cell(x, y).color = color
    board[y][x] = state(color) # update board with flip
    img = shape(x,y)
    # match piece with correct color
    if color == 'white':
        img.classList.remove('black')    
        img.classList.add('white')
    else:
        img.classList.remove('white')    
        img.classList.add('black')

# put a piece at neighbour of (x,y) in direction (dx, dy)
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

# flip any stone caused by the move (mx, my)
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

# check if valid move
def valid_move(move):
    x, y = move
    return not (x == -1 and y == -1)

# make a move
def make_move(move):
    global color # for update
    if debug: print(f'move: {move} by {color} = player {state(color)}')
    flip_stones(move)
    if debug: PrintBoard()
    color = flip(color)
    if debug: print(f'current player: {color} = player {state(color)}')

# flip color
def flip(color):
    return 'black' if color == 'white' else 'white'

# title for warning
title = document.getElementById('header')

# handle click on a cell
def on_click(e):
    if e.target.id.startswith('img'):
        title.innerHTML = 'Cell is occupied!'
        title.style.background = 'pink'
    else:
        if debug: print(f'click cell id = {e.target.id}')
        x, y = [int(i) for i in e.target.id.split('_')]
        if possible_move(x, y):
            title.innerHTML = 'Othello'
            title.style.background = ''
            make_move((x,y))
            # AI to move
            move = ai_move(state(color))
            if valid_move(move):
                make_move(move)
            else:
                title.innerHTML = 'Game Over!'
                title.style.background = 'green'
        else:
            title.innerHTML = 'Cell is ILLEGAL!'
            title.style.background = 'red'

# make the board cells (with flip id for consistency)
def make_board():
    cells = document.createElement('table')
    cells.id = 'board'
    for i in range(8):
        tr = document.createElement('tr')
        for j in range(8):
            td = document.createElement('td')
            td.id = f'{j}_{i}' # flip id
            td.classList.add('cell')
            td.align = 'center'
            td.color = 'empty'
            img = document.createElement('img')
            img.id = f'img{j}_{i}' # flip id
            td.appendChild(img)
            tr.appendChild(td)
            td.addEventListener('click', create_proxy(on_click))
            board[j][i] = state('empty') # initialize board with flip

        cells.appendChild(tr)

    return cells

# initial game pieces
game = document.getElementById('game')
game.appendChild(make_board())
do_flip(3, 3, 'white')
do_flip(4, 4, 'white')
do_flip(3, 4, 'black')
do_flip(4, 3, 'black')

if debug: print('New Game Board:\n')
if debug: PrintBoard()

# black play first
color = 'black'
if debug: print(f'first player: {color}')

</py-script>
```
:::

---

<!-- pandoc -s demo11.md -o demo11.html -->