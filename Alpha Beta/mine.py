 def legal_Moves(board, color):


    legalMoves = []
    for i in range (0,8):
        for j in range (0,8):
            if gamePlay.valid(board, color, (i,j)):
                legalMoves.append((i,j))
    return legalMoves

"""def legal_Moves(board, color):
    legalMoves = []
    for i in range (8):
        for j in range (8):
            if gamePlay.valid(board, color, (i,j)):
            	newBoard = deepcopy(board)
            	gamePlay.doMove(newBoard,color, (i,j))
                legalMoves.append((newBoard,(i,j)))
    return legalMoves"""




def alphaBeta(board,color,depth,alpha,beta,player):


	if depth == 0 or gamePlay.gameOver(board):
		return value(board)
	elif player:
		moves = legal_Moves(board,color)
		for move in moves:
			newBoard = deepcopy(board)
			gamePlay.doMove(newBoard,color,move)
			alpha = max(alpha, alphaBeta(newBoard,color,depth-1, alpha, beta, False))
			if beta <= alpha:
				break
		return alpha
	else: 
		moves = legal_Moves(board,color)
		for move in moves:
			newBoard = deepcopy(board)
			gamePlay.doMove(newBoard,color,move)
			beta = min(beta,alphaBeta(newBoard,color,depth-1,alpha,beta,True))
			if beta <= alpha:
				break
			return beta
	

def compare(x, y, color):
    if color == "W":
        val = x > y
    else:
        val = y < x
    return val



def nextMove(board, color):
	moves = legal_Moves(board, color)
	if len(moves) == 0:
		return "No Possible Moves"
	best = None
	for move in moves:
		newBoard = deepcopy(board)
		gamePlay.doMove(newBoard,color,move)
		ab = alphaBeta(newBoard,color,3,ALPHA,BETA,True)
		if best == None or compare(ab,best,color):
			Goal = move
			assist = ab
	return Goal