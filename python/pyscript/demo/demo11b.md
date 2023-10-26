---
title: Pyscript - Demo 11B
header-includes: |
    <style>
       body { min-width: 90% !important; }
    </style>
    <style>
        .centre {
          text-align: centre
        }
        .board {
          border: 1px solid black
        }
        .hide {
          display: none;
        }
    </style>
include-after: |
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css"/>
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo11b.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo11b.html -->
---

# Pyscript - Game for 2 Players

## Pyscript Othello!{#header .centre}

<table id="board" class="board"></table>

## Output
<py-terminal></py-terminal>

Type your Python code (hover mouse/pointer to bottom right-end for Green arrow to run code):
<py-repl></py-repl>

<!--
REVERSI OTHELLO (PYTHON RECIPE)
Reversi/Othello Board Game using Minimax, Alpha-Beta Pruning, Negamax, Negascout algorithms.
https://code.activestate.com/recipes/580698-reversi-othello/

-->

<!-- pyscript -->
:::{ .hide }
```{=html}
<py-script>
# Reversi/Othello Board Game using Minimax and Alpha-Beta Pruning
# https://en.wikipedia.org/wiki/Reversi
# https://en.wikipedia.org/wiki/Computer_Othello
# https://en.wikipedia.org/wiki/Minimax
# https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
# https://en.wikipedia.org/wiki/Negamax
# https://en.wikipedia.org/wiki/Principal_variation_search
# FB36 - 20160831   31 August 2016

import copy  # for deepcopy

# the board representation as 2x2 matrix
n = 8 # board size (must be even)
board = [['0' for x in range(n)] for y in range(n)]

# 8 directions for any even n
dirx = [-1, 0, 1, -1, 1, -1, 0, 1]
diry = [-1, -1, -1, 0, 0, 1, 1, 1]

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

def Minimax(board, player, depth, maximizingPlayer):
    if depth == 0 or IsTerminalNode(board, player):
        return EvalBoard(board, player)
    if maximizingPlayer:
        bestValue = minEvalBoard
        for y in range(n):
            for x in range(n):
                if ValidMove(board, x, y, player):
                    (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
                    v = Minimax(boardTemp, player, depth - 1, False)
                    bestValue = max(bestValue, v)
    else: # minimizingPlayer
        bestValue = maxEvalBoard
        for y in range(n):
            for x in range(n):
                if ValidMove(board, x, y, player):
                    (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
                    v = Minimax(boardTemp, player, depth - 1, True)
                    bestValue = min(bestValue, v)
    return bestValue

def AlphaBeta(board, player, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or IsTerminalNode(board, player):
        return EvalBoard(board, player)
    if maximizingPlayer:
        v = minEvalBoard
        for y in range(n):
            for x in range(n):
                if ValidMove(board, x, y, player):
                    (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
                    v = max(v, AlphaBeta(boardTemp, player, depth - 1, alpha, beta, False))
                    alpha = max(alpha, v)
                    if beta <= alpha:
                        break # beta cut-off
        return v
    else: # minimizingPlayer
        v = maxEvalBoard
        for y in range(n):
            for x in range(n):
                if ValidMove(board, x, y, player):
                    (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
                    v = min(v, AlphaBeta(boardTemp, player, depth - 1, alpha, beta, True))
                    beta = min(beta, v)
                    if beta <= alpha:
                        break # alpha cut-off
        return v

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

def Negamax(board, player, depth, color):
    if depth == 0 or IsTerminalNode(board, player):
        return color * EvalBoard(board, player)
    bestValue = minEvalBoard
    for y in range(n):
        for x in range(n):
            if ValidMove(board, x, y, player):
                (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
                v = -Negamax(boardTemp, player, depth - 1, -color)
                bestValue = max(bestValue, v)
    return bestValue

def NegamaxAB(board, player, depth, alpha, beta, color):
    if depth == 0 or IsTerminalNode(board, player):
        return color * EvalBoard(board, player)
    bestValue = minEvalBoard
    for y in range(n):
        for x in range(n):
            if ValidMove(board, x, y, player):
                (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
                v = -NegamaxAB(boardTemp, player, depth - 1, -beta, -alpha, -color)
                bestValue = max(bestValue, v)
                alpha = max(alpha, v)
                if alpha >= beta:
                    break
    return bestValue

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

def Negascout(board, player, depth, alpha, beta, color):
    if depth == 0 or IsTerminalNode(board, player):
        return color * EvalBoard(board, player)
    firstChild = True
    for y in range(n):
        for x in range(n):
            if ValidMove(board, x, y, player):
                (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
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
            if ValidMove(board, x, y, player):
                boardTemp, _ = MakeMove(copy.deepcopy(board), x, y, player)
                ''' for now
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
othello(3)

# modify input (This works, prompt with text!)
input = js.prompt

# Algorithm selection
algos = 'REVERSI/OTHELLO BOARD GAME\n' +\
        '0: EvalBoard\n' +\
        '1: Minimax\n' +\
        '2: Minimax w/ Alpha-Beta Pruning\n' +\
        '3: Negamax\n' +\
        '4: Negamax w/ Alpha-Beta Pruning\n' +\
        '5: Negascout (Principal Variation Search)\n' +\
        '6: Minimax w/ Alpha-Beta Pruning w/ Sorted Nodes\n' +\
        '7: Negamax w/ Alpha-Beta Pruning w/ Sorted Nodes\n' +\
        '8: Negascout (Principal Variation Search) w/ Sorted Nodes\n'

print(algos)

# select an algorithm with depth
opt = int(input(f'{algos}Select AI Algorithm (default 0): ') or '0')
if opt > 0 and opt < 9:
    depth = int(input('Select Search Depth (default 4): ') or '4')

# play the game
print('Players: 1 = User,  2 = AI\nUser first to move (Just press Enter for Exit!)')
InitBoard()
go = True
while go:
    for player in ['1', '2']:
        print()
        PrintBoard()
        print(f'PLAYER: {player}')
        if IsTerminalNode(board, player):
            print('Player cannot play! Game ended!')
            print(f"Score User: {EvalBoard(board, '1')}")
            print(f"Score AI  : {EvalBoard(board, '2')}")
            go = False
            break     
        if player == '1': # user's turn
            while True:
                xy = (input(f'Player {player}, your move X Y: ') or '').split()
                if len(xy) != 2:
                   print('\nGame aborted!')
                   go = False
                   break
                x, y = [int(i) for i in xy] # still Error if non-numeric input
                print(f'You played (X, Y): {x} {y}')
                if ValidMove(board, x, y, player):
                    board, total = MakeMove(board, x, y, player)
                    print(f'# of pieces taken: {total}')
                    break
                else:
                    print('Invalid move! Try again!')
            if not go: break 
        else: # AI's turn
            x, y = BestMove(board, player)
            if not (x == -1 and y == -1):
                board, total = MakeMove(board, x, y, player)
                print(f'AI played (X Y): {x} {y}')
                print(f'# of pieces taken: {total}')

</py-script>
```
:::

---

<!-- pandoc -s demo11b.md -o demo11b.html -->