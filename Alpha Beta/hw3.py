
import simpleGreedy
import gamePlay 
import randomPlay 
from copy import deepcopy

ALPHA = float("-inf")
BETA = float("inf")
WHITE = "W"
BLACK = "B"

def value(board):
    value = 0
    for row in board:
    	for elem in row:
    		if elem == WHITE:
    			value = value + 1
    		elif elem == BLACK:
    			value = value - 1
    return value



def Legal_Moves(board, color):
    legal_moves = []
    for i in range(0,8):
        for j in range(0,8):
            if gamePlay.validMove(board, color, (i,j)):
                newBoard = deepcopy(board)
                gamePlay.doMove(newBoard, color, (i,j))
                legal_moves.append((newBoard, (i,j)))
    return legal_moves


def nextMove(board, color):
    moves = Legal_Moves(board, color)
    if color == WHITE:
        notColor = BLACK
    else:
        notColor = WHITE
    bestVal = BETA
    bestPlay = (-1,-1)
    for move in moves:
        value = AlphaBeta(board, color, notColor, bestVal, ALPHA, 3)
        bestVal = max(bestVal, value)
        if bestVal == value or bestPlay == (-1,-1):
            bestPlay = move[1]
    return bestPlay



def AlphaBeta(board, color, colorx, alpha, beta, depth):
    if depth == 0:
        return value(board)
    if colorx == WHITE:
        oppColor = BLACK
    else:
        oppColor = WHITE
    if color == colorx:
        val = alpha
        moves = Legal_Moves(board, colorx)
        for move in moves:
            val = max(val, AlphaBeta(move[0], color, oppColor, alpha, beta, depth - 1))
            if val >= beta:
                return val
            alpha = max(val, alpha)
        return val
    if color != colorx:
        val = beta       
        moves = Legal_Moves(board, oppColor)
        for move in moves:
            val = min(val, AlphaBeta(move[0], color, oppColor, alpha, beta, depth - 1))
            if val <= alpha:
                return val
            beta = min(val, beta)
        return val











