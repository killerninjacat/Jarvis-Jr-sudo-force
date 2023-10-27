import random
import math
dup_board = None
bestmove = None
bestScore = -math.inf
winner = None
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

def display_board():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
    print("--------------------------")


def pcplay():
    
    global bestScore
    global bestmove
    global board
    global dup_board
    global winner
    bestScore = -math.inf
    dup_board = list(board)
    for i in findOccurrences(board,"-"):
        board[i] = "Y"
        score = minimax(False , 0 , board)
        board[i] = "-"
        
        if score > bestScore:
            bestScore = score
            bestmove = i

    board[bestmove] = "Y"
    winner = None
    display_board()
    if check_game_over() and winner != None:
        print("winner is ", winner, "/n")
    elif check_game_over():
        print("It is a tie")
    else:
        playeplay()
            



def minimax(ismaximizing, depth, board):
    global dup_board
    
    if tiegame():
        return 0
    elif check_winner():
        if winner == "Y":
            return 1
        else:
            return -1

    
    if ismaximizing:
        bestscore = -math.inf
        for j in findOccurrences(board, "-"):
                board[j] = "Y"
                score = minimax(False, depth+1 ,board)
                board[j] = "-"
                bestscore = max(score, bestscore)
                
        return bestscore 

    else:
            bestscore = math.inf
            for k in findOccurrences(board, "-"):
                board[k] = "X"
                score = minimax( True, depth+1, board)
                board[k] = "-"
                bestscore = min(score, bestscore)
                
            return bestscore 
            
         
def playeplay():
    global winner
    position = int(input("choose a place from 1 to 9"))
    position -= 1
    while board[position] != "-":
        print("invalid input")
        position = int(input("choose a place from 1 to 9"))
        position -= 1

    board[position] = "X"
    winner = None
    display_board()
    if check_game_over() and winner != None:
        print("winner is ", winner)
    elif check_game_over():
        print("It is a tie")
    else:
        pcplay()

def check_game_over():
    if check_winner():
        return True
    elif tiegame():
        return True
    else:
        return False

def check_winner():
    global winner
    if row() or column() or diagonal():
        return True
    else:
        return False

def tiegame():
    global bestScore
    if "-" not in board:
        return True
        
    else:
        return False

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]
    
    
def row():
    global winner
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        if row1 == True:
            winner = board[0]
        elif row2 == True:
            winner = board[3]
        elif row3 == True:
            winner = board[6]
        return True
    else:
        return False

def column():
    global winner
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3:
        if column1 == True:
            winner = board[0]
        elif column2 == True:
            winner = board[1]
        elif column3 == True:
            winner = board[2]
        return True
    else:
        return False

def diagonal():
    global winner
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    if diagonal1 or diagonal2:
        if diagonal == True:
            winner = board[0]
        elif diagonal2 == True:
            winner = board[2]
        return True
    else:
        return False
    

def init():
    display_board()
    playeplay()
    