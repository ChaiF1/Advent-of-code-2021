import numpy as np
file = open("day_4_data.txt")
# Might clean up the program later but for now it works.
x = np.fromstring(file.readline().strip('\n'), sep =',', dtype=int) # Numbers drawn
og = np.copy(x) # Copy of original order of all numbers drawn

boards = np.genfromtxt("day_4_data.txt", skip_header=2, dtype=int) # Generate a (n,5,5) array of all the boards where n is the amount of boards,
n = len(boards)//5
board_win = np.empty(n, dtype=bool)
boards = boards.reshape(n, 5, 5)

"""
Here is how my solution works for assignment 1:
Let x be the set represeningt the numbers drawn. Check for the first board at which draw it wins and reduce the set x to x* which removes all numbers drawn after the board has won.
Then move on to board 2 and check if it can win with the numbers drawn in x*. If it can reduce x* in a similar way as in the first step. If it cannot move on to the next board.
Move through all boards in this manner, making an array of booleans marking if a board was able to win with the set it was given. The last value True in this array has the same index as the winning board.
With the winning board and the reduced set it uses to win you can easily calculate the final score of that board.
"""



def reduce_x(row):
"""
Function used for reducing the set x as described in the process for assignment 1.
"""
    global x
    index = np.empty(5, dtype=int)
    for k in range(len(row)):
        index[k] = np.argwhere(x==row[k])
    return x[0:max(index)+1]

def check_board(A): # Input board, return true or false
"""
Horrendously ugly function which checks if any row, column or the diagonal is complete using the drawn numbers from the set x. 
"""
    global x
    for row in A:
        diff = np.setdiff1d(row, x, assume_unique=True) # If the set difference of a row and x is empty then every number in that row has been drawn.
        if len(diff) == 0:
            x = reduce_x(row) # Comment this out for assignment 2
            return True
    for col in np.transpose(A):
        diff = np.setdiff1d(col, x, assume_unique=True)
        if len(diff) == 0:
            x = reduce_x(col) # Comment this out for assignment 2
            return True
    if len(np.setdiff1d(np.diag(A), x, assume_unique=True))==0:
        x = reduce_x(np.diag(A)) # Comment this out for assignment 2
        return True
    return False

for k in range(n):
    board_win[k] = check_board(boards[k])

winning_board = boards[max( np.argwhere(board_win))]
print(np.sum(np.setdiff1d( winning_board, x, assume_unique=True))*x[-1])

"""
For assignment 2:
Comment out lines 52, 53, 55, 56 and the reduce functions used in check_board. Comment in lines 66-73
Given a set of drawn numbers x generate an array of booleans checking if every board can win with that set. Repeat this with a set x^- which is the same as x but has the last draw removed.
Repeat the above process until there is one and only one False in the array showing if a board won. The index of this False is the same as the last board to win.
"""


#for k in range(len(og)-1, 0, -1):
#    x = og[0:k]
#    for l in range(n):
#        board_win[l] = check_board(boards[l])
#    if sum(board_win) == len(board_win)-1:
#        last_win = boards[ np.argwhere(~board_win) ]
#        print(np.sum(np.setdiff1d( last_win, og[:len(x)+1], assume_unique=True))*og[len(x)])
#        break