import sys
board = {'1':' 1 ', '2':' 2 ', '3':' 3 ',
        '4':' 4 ', '5':' 5 ', '6':' 6 ',
        '7':' 7 ', '8':' 8 ', '9':' 9 '}

def printBoard(board):
    print()
    print()
    print()
    print()
    print()
    print(board['1'], '|', board['2'], '|', board['3'], sep='')
    print('---+---+---')
    print(board['4'], '|', board['5'], '|', board['6'], sep='')
    print('---+---+---')
    print(board['7'], '|', board['8'], '|', board['9'], sep='')

def moves():
    turn = '-X-'
    for i in range(9):
        printBoard(board)
        print('Turn for ' + turn + '. Move on which space? (Type number of given spot.)')
        move = input()
        board[move] = turn
        wincheck(board, turn)
        if turn == '-X-':
            turn = '-O-'
        else:
            turn = '-X-'

def wincheck(board, turn):
    checkL = []
    for v in board.values():
        checkL.append(v)

    if checkL[0]==turn and checkL[1]==turn and checkL[2]==turn:
        printBoard(board)
        print(turn, 'Player wins!')
        sys.exit()
    if checkL[3]==turn and checkL[4]==turn and checkL[5]==turn:
        printBoard(board)
        print(turn, 'Player wins!')
        sys.exit()
    if checkL[6]==turn and checkL[7]==turn and checkL[8]==turn:
        printBoard(board)
        print(turn, 'Player wins!')
        sys.exit()
    if checkL[0]==turn and checkL[3]==turn and checkL[6]==turn:
        printBoard(board)
        print(turn, 'Player wins!')
        sys.exit()
    if checkL[1]==turn and checkL[4]==turn and checkL[7]==turn:
        printBoard(board)
        print(turn, 'Player wins!')
        sys.exit()
    if checkL[2]==turn and checkL[5]==turn and checkL[8]==turn:
        printBoard(board)
        print(turn, 'Player wins!')
        sys.exit()
    if checkL[0]==turn and checkL[4]==turn and checkL[8]==turn:
        printBoard(board)
        print(turn, 'Player wins!')
        sys.exit()
    if checkL[2]==turn and checkL[4]==turn and checkL[6]==turn:
        printBoard(board)
        print(turn, 'Player wins!')
        sys.exit()

moves()
printBoard(board)
print('It was a Tie!')