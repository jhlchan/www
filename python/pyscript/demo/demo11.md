---
title: Pyscript - Demo 11
header-includes: |
    <style>
       body { min-width: 90% !important; }
    </style>
    <style>
        .header {
          text-align: center;
          font-size: 30px;
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
         .param {
            background: lightgreen;
         }
         .info {
            background: lavender;
         }
    </style>
include-after: |
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css"/>
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo11.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo11.html -->
---

# Pyscript - Game for 2 Players

## Othello{#header .header}

:::{.board .param}
&nbsp;&nbsp;&nbsp;
Pick algorithm: <select id="option" class="py-input">
    <option value="0" selected>Evaluate Board</option>
    <option value="1">Minimax</option>
    <option value="2">Minimax with &alpha;-&beta; pruning</option>
    <option value="3">Negamax</option>
    <option value="4">Negamax with &alpha;-&beta; pruning</option>
    <option value="5">Negascout</option>
    <option value="6">Minimax &alpha;-&beta; with sorted nodes</option>
    <option value="7">Negamax &alpha;-&beta; with sorted nodes</option>
    <option value="8">Negascout with sorted nodes</option>
</select>
Number of players: <select id="nplayer" class="py-input">
    <option value="2" selected>2</option>
    <option value="1">1</option>
    <option value="0">0</option>
</select>
Game: <select id="code" class="py-input">
    <option value="0" selected>New</option>
</select>

* Number of players: 2 = black vs white, 1 = black vs machine , 0 = machine vs machine.
* Game moves are recorded, click "Save" to get the moves in clipboard.
:::

:::{#game .board }
:::

:::{.board .info}
&nbsp;&nbsp;&nbsp;
<img class="black"></img> [move]{#black .py-input} total: [0]{#bcount .py-input}
<img class="white"></img> [move]{#white .py-input} total: [0]{#wcount .py-input}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[{Message Area}]{#message .py-input }
<button id="save" class="py-button">Save</button>
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
 0  1  2  3  4  5  6  7 

Second one to first one: 0 = empty, 1 = black, 2 = white.
The location ? for first one is: X = 2, Y = 3, for second one is: X = 3, Y = 2.
For consistency, with the minimal change, all we need to do is:
(1) flip the ids for cell and image when creating them in the GUI.
(2) flip (x,y) when updating the board by GUI in do_flip.

This situation arises from the inconsistency between matrix notation and cell notation.

In matrix notation, the first row from left to right is: [0][0], [0][1], [0][2], ...
In cell notation,   the first row from left to right is: (0, 0), (1, 0), (2, 0), ...
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
# debug = True
debug = False

if not debug: document.getElementById('debug').style = 'display: none'

# number of human players
nplayer = 2   # game just checks valid move
# nplayer = 1   # game is human vs AI
# nplayer = 0   # game is AI vs AI
# Is it possible for the game to play according to a move script?

# option for algorithm
option = 0    # EvalBoard

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

# make a move (x,y) on the board by player
# board in arg is a deepcopy of global board
def MakeMove(board, move, player):
    x, y = move  # assuming valid move
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

    # return updated board in arg
    return (board, total)

# check if move (x,y) is valid for player
def ValidMove(board, move, player):
    x, y = move
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if board[y][x] != '0':
        return False
    # ignore updated board copy in validity check     
    _ , total = MakeMove(copy.deepcopy(board), move, player)
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
            if ValidMove(board, (x, y), player):
                return False
    return True

# get a list of sorted nodes
def GetSortedNodes(board, player):
    sortedNodes = []
    for y in range(n):
        for x in range(n):
            if ValidMove(board, (x, y), player):
                boardTemp, _ = MakeMove(copy.deepcopy(board), (x, y), player)
                sortedNodes.append((boardTemp, EvalBoard(boardTemp, player)))
    sortedNodes = sorted(sortedNodes, key = lambda node: node[1], reverse = True)
    sortedNodes = [node[0] for node in sortedNodes]
    return sortedNodes

# Minimax algorithm
# https://en.wikipedia.org/wiki/Minimax
def Minimax(board, player, depth, maximizingPlayer):
    if depth == 0 or IsTerminalNode(board, player):
        return EvalBoard(board, player)
    if maximizingPlayer:
        bestValue = minEvalBoard
        for y in range(n):
            for x in range(n):
                if ValidMove(board, (x, y), player):
                    boardTemp, _ = MakeMove(copy.deepcopy(board), (x, y), player)
                    v = Minimax(boardTemp, player, depth - 1, False)
                    bestValue = max(bestValue, v)
    else: # minimizingPlayer
        bestValue = maxEvalBoard
        for y in range(n):
            for x in range(n):
                if ValidMove(board, (x, y), player):
                    boardTemp, _ = MakeMove(copy.deepcopy(board), (x, y), player)
                    v = Minimax(boardTemp, player, depth - 1, True)
                    bestValue = min(bestValue, v)
    return bestValue

# Alpha-beta Pruning
# https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
def AlphaBeta(board, player, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or IsTerminalNode(board, player):
        return EvalBoard(board, player)
    if maximizingPlayer:
        v = minEvalBoard
        for y in range(n):
            for x in range(n):
                if ValidMove(board, (x, y), player):
                    boardTemp, _ = MakeMove(copy.deepcopy(board), (x, y), player)
                    v = max(v, AlphaBeta(boardTemp, player, depth - 1, alpha, beta, False))
                    alpha = max(alpha, v)
                    if beta <= alpha:
                        break # beta cut-off
        return v
    else: # minimizingPlayer
        v = maxEvalBoard
        for y in range(n):
            for x in range(n):
                if ValidMove(board, (x, y), player):
                    boardTemp, _ = MakeMove(copy.deepcopy(board), (x, y), player)
                    v = min(v, AlphaBeta(boardTemp, player, depth - 1, alpha, beta, True))
                    beta = min(beta, v)
                    if beta <= alpha:
                        break # alpha cut-off
        return v

# Alpha-beta Pruning with Sorted Nodes
def AlphaBetaSN(board, player, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or IsTerminalNode(board, player):
        return EvalBoard(board, player)
    sortedNodes = GetSortedNodes(board, player)
    if maximizingPlayer:
        v = minEvalBoard
        for boardTemp in sortedNodes:
            v = max(v, AlphaBetaSN(boardTemp, player, depth - 1, alpha, beta, False))
            alpha = max(alpha, v)
            if beta <= alpha:
                break # beta cut-off
        return v
    else: # minimizingPlayer
        v = maxEvalBoard
        for boardTemp in sortedNodes:
            v = min(v, AlphaBetaSN(boardTemp, player, depth - 1, alpha, beta, True))
            beta = min(beta, v)
            if beta <= alpha:
                break # alpha cut-off
        return v

# Negamax
# https://en.wikipedia.org/wiki/Negamax
def Negamax(board, player, depth, color):
    if depth == 0 or IsTerminalNode(board, player):
        return color * EvalBoard(board, player)
    bestValue = minEvalBoard
    for y in range(n):
        for x in range(n):
            if ValidMove(board, (x, y), player):
                boardTemp, _ = MakeMove(copy.deepcopy(board), (x, y), player)
                v = -Negamax(boardTemp, player, depth - 1, -color)
                bestValue = max(bestValue, v)
    return bestValue

# Negamax with Alpha-beta Pruning
def NegamaxAB(board, player, depth, alpha, beta, color):
    if depth == 0 or IsTerminalNode(board, player):
        return color * EvalBoard(board, player)
    bestValue = minEvalBoard
    for y in range(n):
        for x in range(n):
            if ValidMove(board, (x, y), player):
                boardTemp, _ = MakeMove(copy.deepcopy(board), (x, y), player)
                v = -NegamaxAB(boardTemp, player, depth - 1, -beta, -alpha, -color)
                bestValue = max(bestValue, v)
                alpha = max(alpha, v)
                if alpha >= beta:
                    break
    return bestValue

# Negamax with Alpha-beta Pruning and Sorted Nodes
def NegamaxABSN(board, player, depth, alpha, beta, color):
    if depth == 0 or IsTerminalNode(board, player):
        return color * EvalBoard(board, player)
    sortedNodes = GetSortedNodes(board, player)
    bestValue = minEvalBoard
    for boardTemp in sortedNodes:
        v = -NegamaxABSN(boardTemp, player, depth - 1, -beta, -alpha, -color)
        bestValue = max(bestValue, v)
        alpha = max(alpha, v)
        if alpha >= beta:
            break
    return bestValue

# Negascout
# https://en.wikipedia.org/wiki/Principal_variation_search
def Negascout(board, player, depth, alpha, beta, color):
    if depth == 0 or IsTerminalNode(board, player):
        return color * EvalBoard(board, player)
    firstChild = True
    for y in range(n):
        for x in range(n):
            if ValidMove(board, (x, y), player):
                boardTemp, _ = MakeMove(copy.deepcopy(board), (x, y), player)
                if not firstChild:
                    score = -Negascout(boardTemp, player, depth - 1, -alpha - 1, -alpha, -color)
                    if alpha < score and score < beta:
                        score = -Negascout(boardTemp, player, depth - 1, -beta, -score, -color)
                else:
                    firstChild = False
                    score = -Negascout(boardTemp, player, depth - 1, -beta, -alpha, -color)
                alpha = max(alpha, score)
                if alpha >= beta:
                    break
    return alpha

# Negascout with Sorted Nodes
def NegascoutSN(board, player, depth, alpha, beta, color):
    if depth == 0 or IsTerminalNode(board, player):
        return color * EvalBoard(board, player)
    sortedNodes = GetSortedNodes(board, player)
    firstChild = True
    for boardTemp in sortedNodes:
        if not firstChild:
            score = -NegascoutSN(boardTemp, player, depth - 1, -alpha - 1, -alpha, -color)
            if alpha < score and score < beta:
                score = -NegascoutSN(boardTemp, player, depth - 1, -beta, -score, -color)
        else:
            firstChild = False
            score = -NegascoutSN(boardTemp, player, depth - 1, -beta, -alpha, -color)
        alpha = max(alpha, score)
        if alpha >= beta:
            break
    return alpha

# compute the best move by a player
def BestMove(board, player):
    maxPoints = 0
    mx, my = (-1, -1)
    for y in range(n):
        for x in range(n):
            if ValidMove(board, (x, y), player):
                boardTemp, _ = MakeMove(copy.deepcopy(board), (x, y), player)
                match option:
                    case 0: points = EvalBoard(boardTemp, player)
                    case 1: points = Minimax(boardTemp, player, depth, True)
                    case 2: points = AlphaBeta(board, player, depth, minEvalBoard, maxEvalBoard, True)
                    case 3: points = Negamax(boardTemp, player, depth, 1)
                    case 4: points = NegamaxAB(boardTemp, player, depth, minEvalBoard, maxEvalBoard, 1)
                    case 5: points = Negascout(boardTemp, player, depth, minEvalBoard, maxEvalBoard, 1)
                    case 6: points = AlphaBetaSN(board, player, depth, minEvalBoard, maxEvalBoard, True)
                    case 7: points = NegamaxABSN(boardTemp, player, depth, minEvalBoard, maxEvalBoard, 1)
                    case 8: points = NegascoutSN(boardTemp, player, depth, minEvalBoard, maxEvalBoard, 1)
                if points > maxPoints:
                    maxPoints = points
                    mx, my = (x, y)

    return (mx, my)

#########################
# The GUI Interface     #
#########################
from time import sleep

# a record of board changes
history = []

# state mapping between the two versions
state = {'empty': '0', 'black': '1', 'white': '2'}

# neighbours of a piece
directions = [(1, 1), (-1, 1), (0, 1), (1, -1), (-1, -1), (0, -1), (1, 0), (-1, 0)]

# get cell (x,y)
def cell(x, y):
    return document.getElementById(f'{x}_{y}')

# get shape (x,y)
def shape(x, y):
    return document.getElementById(f'img{x}_{y}')

# flip color
def flip(color):
    return 'black' if color == 'white' else 'white'

# put a piece at (x,y) with color
def do_flip(x, y, color):
    old_color = cell(x, y).color
    cell(x, y).color = color
    board[y][x] = state[color] # update board with flip
    change_total(color, 1) # update color total
    if old_color != 'empty': change_total(old_color, -1) # update color total of opponent
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
    count = 0 # how many flipped
    mx, my = move
    for direction in directions:
        if flip_in_direction(mx, my, direction):
             dx, dy = direction
             x, y = mx + dx, my + dy
             while cell(x, y).color != color:
                 do_flip(x, y, color)  # color = current player
                 count += 1
                 x, y = x + dx, y + dy

    do_flip(mx, my, color) # this is the empty cell
    count += 1
    return count

# check if a move (x,y) is possible
def possible_move(move):
    x, y = move
    c = cell(x, y)
    if c.color == 'empty':
        for direction in directions:
            if flip_in_direction(x, y, direction):
                return True

# check if valid move
def valid_move(move):
    x, y = move
    return not (x == -1 and y == -1)

# message area
message = document.getElementById('message')

# to say something to target
def say(something, target):
    where = document.getElementById(target)
    where.innerHTML = something

# give tell someting with color
def tell(something, color = 'white'):
    message.innerHTML = something
    message.style.background = color

# change the total of color
def change_total(color, amount):
    span = document.getElementById(f'{color[0]}count')
    total = int(span.innerHTML) + amount
    span.innerHTML = str(total)

# make a move
def make_move(move):
    global board, color # for update
    if debug: print(f'move: {move} by {color} = player {state[color]}')
    say(f'{move}', color)
    history.append(f'{color[0]} {move[0]} {move[1]}')
    count = flip_stones(move)
    if debug: PrintBoard()
    if debug: print(f'{color} flipped over {count} cells.')
    color = flip(color)
    if debug: print(f'current player: {color} = player {state[color]}')

# handle click on a cell
def on_click(e):
    if e.target.id.startswith('img'):
        tell('Cell is occupied!', 'pink')
    else:
        if debug: print(f'click cell id = {e.target.id}')
        move = tuple(int(i) for i in e.target.id.split('_'))
        if possible_move(move):
            tell('Message') # remove warning
            make_move(move)
            if nplayer == 2:
                tell(f'Next: {color}')
            else:
                # AI to move
                move = BestMove(board, state[color])
                if valid_move(move):
                    make_move(move)
                    tell(f'Next: {color}')
                else:
                    tell('Game Over!', 'green')
                    game_over()
        else:
            tell('Cell is ILLEGAL!', 'red')

# single proxy for add and remove listener
click_proxy = create_proxy(on_click)

# auto play the game
def auto_play():
    global board
    print('Players: 1 = User,  2 = AI\n')
    max = 100 # max number of steps
    end = False
    step = 0
    while not end:
        step += 1
        print(f'auto_play: step = {step}')
        end = (step == max)
        for color in ['black', 'white']:
            tell(f'PLAYER: {color}', 'yellow')
            player = state[color]
            if IsTerminalNode(board, player):
                end = True
                break
            # keep playing 
            move = BestMove(board, player)
            if valid_move(move):
                make_move(move)
            else: # Game over
                end = True
                break

    tell(f'steps: {step}')
    sleep(3)
    game_over()

# make the board cells (with flip id for consistency)
def make_board():
    cells = document.createElement('table')
    cells.id = 'board'
    for i in range(n):
        tr = document.createElement('tr')
        for j in range(n):
            td = document.createElement('td')
            td.id = f'{j}_{i}' # flip id
            td.classList.add('cell')
            td.align = 'center'
            td.color = 'empty'
            img = document.createElement('img')
            img.id = f'img{j}_{i}' # flip id
            td.appendChild(img)
            tr.appendChild(td)

        cells.appendChild(tr)

    return cells

# clean the board
def clean_board():
    history.append(f'g {n} {n}')
    for i in range(n):
        for j in range(n):
            td = cell(j, i)
            td.color = 'empty'
            img = shape(j,i)
            img.classList.remove('black')
            img.classList.remove('white')
            td.removeEventListener('click', click_proxy)
            if nplayer != 0: td.addEventListener('click', click_proxy)
            board[j][i] = state['empty'] # initialize board with flip

    # delete moves and counts
    Element('black').element.innerHTML = 'move'
    Element('bcount').element.innerHTML = '0'
    Element('white').element.innerHTML = 'move'
    Element('wcount').element.innerHTML = '0'
    tell('Message') # clear message

# game over
def game_over():
    # tell the result, innerHtml is read-only
    b = int(Element('bcount').innerHtml) # Black score
    w = int(Element('wcount').innerHtml) # White score
    print(f'Game over,  black score: {b}, white score: {w}')
    history.append(f'x {b} {w}')
    if b > w: tell(f'Black wins!', 'yellow')
    if b < w: tell(f'White wins!', 'yellow')
    if b == w: tell(f'It is a draw!', 'yellow')
    # disable clicks
    for i in range(n):
        for j in range(n):
            td = cell(j, i)
            td.removeEventListener('click', click_proxy)

    return (b, w)        

# stored game moves
games = [
   'g 8 8,b 3 4,w 3 3,b 4 3,w 4 4',   # games[0] = standard opening
   'g 8 8,b 3 4,w 3 3,b 4 3,w 4 4,b 4 5,w 5 5,b 5 4,w 5 3',
   'g 8 8,b 3 4,w 3 3,b 4 3,w 4 4,b 4 5,w 5 5,b 5 4,w 5 3,b 6 5,w 5 6,b 6 3,w 3 5', 
   'g 8 8,b 3 4,w 3 3,b 4 3,w 4 4,b 3 2,w 2 2,b 1 2,w 1 1,b 1 0,w 0 0,x 5 5',    # autoplay 3 steps
   'g 8 8,b 3 4,w 3 3,b 4 3,w 4 4,b 3 2,w 2 2,b 1 2,w 1 1,b 1 0,w 0 0,b 2 3,w 2 0,b 2 1,w 2 4,b 4 5,w 5 4,b 4 2,w 0 1,b 1 4,w 0 4,b 0 2,w 4 1,b 4 0,w 0 3,b 0 5,w 5 2,b 6 3,w 0 6,b 2 5,w 6 4,b 6 5,w 7 6,b 3 1,w 3 0,b 1 3,w 7 4,b 3 5,w 3 6,b 4 6,w 5 7,b 1 5,w 5 5,b 4 7,w 5 0,b 7 2,w 5 3,b 7 3,w 7 1,b 5 1,w 5 6,b 3 7,w 2 7,b 6 2,w 6 1,b 7 0,w 2 6,b 7 5,w 6 6,b 6 7,w 7 7,b 1 7,w 6 0,b 1 6,w 0 7,x 17 47', # autoplay till end, 64 moves
   'g 8 8,b 3 4,w 3 3,b 4 3,w 4 4' # last one alos the standard, no comma
]

# get a game
def get_game():
    return games[int(Element('code').value)]

# play a game
def play(game):
    global color, history
    history = []
    # initial game pieces
    clean_board()
    color = 'black'
    list = game.split(',')
    if debug: print(f'Game: {list}')
    end = False
    for item in list:
        c, x, y = item.split()
        move = (int(x), int(y))
        match c:
           case 'g':
              assert move == (n, n), 'Only 8x8 board'
           case 'b':
              assert color == 'black', 'Black should move'
              make_move(move)
           case 'w':
              assert color == 'white', 'White should move'
              make_move(move)
           case _ :
              b, w = game_over()
              end = True
              assert move == (b, w), 'Scores differ!'

    # continue to play
    if not end:
        if debug: print('Continue to play:\n')
        if debug: PrintBoard()
        if debug: print(f'current player: {color}')
        tell(f'Next: {color}')

        # check auto-play
        if nplayer == 0: auto_play()

# new game
def new_game():
    global color, history
    history = []
    # initial game pieces
    clean_board()
    color = 'black'
    make_move((3,4))  # black moves first
    make_move((3,3))  # white moves second
    make_move((4,3))
    make_move((4,4))

    if debug: print('New Game Board:\n')
    if debug: PrintBoard()

    # black play first
    color = 'black'
    if debug: print(f'first player: {color}')

    # check auto-play
    if nplayer == 0: auto_play()

# reset the game
def reset(event): # event is ignored
    global nplayer, option
    nplayer = int(Element('nplayer').value)
    option = int(Element('option').value)
    if debug: print(f'Number of players: {nplayer}')
    if debug: print(f'Algorithm selected: {option}')
    play(get_game())

# single proxy for reset
reset_proxy = create_proxy(reset)

# get history to clipboard
def save(event):
    text = ','.join(history)
    if debug: print(f'Moves: {text}')
    temp = document.createElement('textarea')
    temp.value = text
    document.body.appendChild(temp)
    temp.select() # no select if temp is hidden
    document.execCommand('copy')
    document.body.removeChild(temp)
    tell('Moves in Clipboard.')

# add game options
def add_options():
    code = document.getElementById('code')
    for j in range(1, len(games)):
        option =  document.createElement('option')
        option.innerHTML = f'Game {j}'
        option.value = f'{j}'
        code.appendChild(option)

# make the GUI game
game = document.getElementById('game')
game.appendChild(make_board())
add_options()

# listen for selections
select = document.getElementById('option')
select.addEventListener('change', reset_proxy)

select = document.getElementById('nplayer')
select.addEventListener('change', reset_proxy)

select = document.getElementById('code')
select.addEventListener('change', reset_proxy)

capture = document.getElementById('save')
capture.addEventListener('click', create_proxy(save))

# start new game
# new_game()
# start with default game 0
play(get_game())

</py-script>
```
:::

---

<!-- pandoc -s demo11.md -o demo11.html -->