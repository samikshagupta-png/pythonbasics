import numpy
board = numpy.array([['_','_','_'],['_','_','_'],['_','_','_']])
p1s ='X'
p2s ='O'


def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row = int(input('enter row  - 1 or 2 or 3 '))
        column = int(input('enter col  - 1 or 2 or 3 '))
        if row>0 and row <4 and column>0 and column<4 and board[row-1][column-1]=='_':
            break
        else:
            print("invalid input,please enter again")
    board[row-1][column-1] =symbol


def check_rows(symbols):
    for r in range(3):
        count =0
        for c in range(3):
            if board[r][c] == symbols:
                count=count+1
        if count ==3:
            print(symbols,'won')
            return True
    return False
def check_cols(symbols):
    for c in range(3):
        count =0
        for r in range(3):
            if board[r][c] == symbols:
                count=count+1
        if count ==3:
            print(symbols,'won')
            return True
    return False

def check_diagonal(symbols):
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1]==symbols:
        print(symbols,'won')
        return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1]==symbols:
            print(symbols,'won')
            return True
    return False
    
def won(symbols):
    return check_rows(symbols) or check_cols(symbols) or check_diagonal(symbols)
def play():
    for turn in range(9):
        if turn%2==0:
            print("X turn")
            place(p1s)
            if won(p1s):
                break
        else:
            print('O turn')
            place(p2s)
            if won(p2s):
                break
        if not(won(p1s)) and not(won(p2s)):
            print("draw")
play()