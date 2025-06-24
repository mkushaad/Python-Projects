import numpy as numpy

def won(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c]==symbol:
                count += 1
            if count == 3:
                return 1
    for c in range(3):
        count = 0
        for r in range(3):
            if board[r][c]==symbol:
                count += 1
            if count == 3:
                return 1
    if (board[0][0] == board[1][1] == board[2][2] == symbol ) or (board[0][2] == board[1][1] == board[2][0] == symbol ):
        return 1
    return 0
    

def place(symbol):
    print("Current Board:")
    for x in board:
        print(x)
    while(1):
        row = int(input("Enter row: 1 or 2 or 3: "))
        col = int(input("Enter column: 1 or 2 or 3: "))
        if row > 0 and row < 4 and col > 0 and col < 4 and board[row-1][col-1] == '-':
            board[row-1][col-1] = symbol
            break
        else:
            print("Enter valid value!")
    

def play():
    for i in range(9):
        if i%2==0:
            print("X's turn")
            place(p1)
            if won(p1):
                for x in board:
                    print(x)
                print("Player 1 has won!")
                break
        else:
            print("O's turn")
            place(p2)
            if won(p2):
                for x in board:
                    print(x)
                print("Player 2 has won!")
                break 
    if not(won(p1)) and not(won(p2)):
            print("-------Draw------")
            
map = [['-' for x in range(3)] for x in range(3)]
board = map #numpy.array(map)
p1 = 'X'
p2 = 'O'

play() 