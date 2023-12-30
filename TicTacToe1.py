import random
import sys

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True

# printing the game board 
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
# printBoard(board)

def cleanBoard(board):
    board = cleanBoard

# take player input
def playerInput(board):
    i = input("Enter a number 1-9:")
    inp = int(i)
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = str(currentPlayer)
    else:
        print("Oops, player is already in that spot!")
        switchPlayer()


# check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board [2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board [5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board [8] and board[6] != "-":
        winner = board[6]
        return True


def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    

def checkTie(board):
    global gameRunning
    if gameRunning and "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False


def checkWin(board):
   global gameRunning
   if gameRunning and (checkDiagonal(board) or checkHorizontle(board) or checkVertical(board)):
      print(f"The winner is {winner}")
      gameRunning = False
      printBoard(board)


# switch the player 
def switchPlayer():
    global currentPlayer
    global gameRunning
    if  gameRunning and currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
    


# computer
def computer(board):
    if "-" in board:
        while currentPlayer == "O":
            position = random.randint(0,8)
            if board[position] == "-":
                board[position] = "O"
                switchPlayer()


# check New Game
def checkNewGame():
    global gameRunning
    inp = str(input("Enter 1 for a new Game or 0 for exit:"))
    if inp == "1":
        gameRunning = True
        return True
    elif inp == "0":
        return False
    else:
        print("Please Enter a valid Value!")
        checkNewGame()


# Game Running and check for win or false

def rungame():
    board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
    while gameRunning:
        printBoard(board)
        playerInput(board)
        checkWin(board)
        checkTie(board)
        switchPlayer()
        computer(board)
        checkWin(board)
        checkTie(board)
    


# Call Game Running and check for a new Game
         
repeat = True
while repeat:
    rungame()
    repeat = checkNewGame()

print("End game.")
