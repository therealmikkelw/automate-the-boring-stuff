#! python3
# shebang line for windows above

import pprint # pretty print module

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


# create dictionary representing a blank tictactoe board
theBoard = {'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ', 'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ', 'low-L' : ' ', 'low-M' : ' ', 'low-R' : ' '}

# simulate moves
if 'top-L' in theBoard:
    theBoard['top-L'] = 'X'

if 'mid-M' in theBoard:
    theBoard['mid-M'] = 'O'

if 'top-R' in theBoard:
    theBoard['top-R'] = 'X'

if 'low-R' in theBoard:
    theBoard['low-R'] = 'O'

if 'top-M' in theBoard:
    theBoard['top-M'] = 'X'

if 'mid-L' in theBoard:
    theBoard['mid-L'] = 'O'

# print board using function printBoard()
printBoard(theBoard)
