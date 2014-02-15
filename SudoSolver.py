import sys
import collections

# 2d array for sudoku board
# initialize board
size = 4
board = [[0 for i in range(0, size)] for i in range(0, size)]
board = [[3,0,4,0],[0,1,0,2],[0,4,0,3],[2,0,1,0]]

# remainRow values for each row, column or section
remainRow = [[i for i in range(1,size+1)] for i in range(0,size)]
remainCol = [[i for i in range(1,size+1)] for i in range(0,size)]

# zero matrix to fill in empty spaces
zeros = [[0 for i in range(0,size)] for i in range(0, size)]

def printBoard():
    print('Current Sudoku Board:')
    for i in range(len(board)):
        for j in range(len(board[i])):
            sys.stdout.write('%s ' %board[i][j])
        print()

    print('remainRow values:')
    for i in range(len(remainRow)):
        for j in range(len(remainRow[i])):
            sys.stdout.write('%s ' %remainRow[i][j])
        print()

    print('remainCol values:')
    for i in range(len(remainCol)):
        for j in range(len(remainCol[i])):
            sys.stdout.write('%s ' %remainCol[i][j])
        print()


def solve(board):
    if len(remainRow) == 0 and len(remainCol) == 0:
        print("Sudoku Solved")
        printBoard()

    # wherever there is a 0, try a value from "remaining" corresponding to that position
    position = search(board,0)
    
    # for each coordinate pair, find the corresponding "remaining"
    for i in range(len(position)):
        x = int(position[i][0])
        y = int(position[i][1])
        tryValue = remainRow[x][y]
        print(tryValue)
        insert(board, position[i][0], position[i][1], tryValue)

    return 0

def insert(board, row, col, val):
    board[row][col] = val
    position = search(board,0)
    elim()

    if row == len(remainRow) or col == len(remainCol):
        print("Sudoku Solved")
        printBoard()
        return 0
    
    # check board to maintain validity
    if check(board)[0]:
        insert(board, row, col, 0)
        #solve(board)
    #else:
        #insert(board, position[row+1][0], position[col+1][1],
               #remainRow[int(position[row+1][0])][int(position[col+1][1])])
    
def search(board,val):
    print("Searching for:",val)

    returnVal = []

    for i in range(0,size):
        for j in range(0,size):
            if board[i][j] == val:
                # return a list of all coordinates that contain the value
                coordinates = [i,j]
                returnVal.append(coordinates)

    return returnVal

# checks for occurence of all values i.e. in each column w/ second parameter list
def check(board):

    # check columns all at once
    error = False
    errorID = []
    
    # check for input errors
    print("Checking for occurrences...")
    
    for i in range(size):
        tempList = []
        checkList = []
        # populate checkList
        for j in range(size):
            checkList.append(board[j][i])
            
        # ignore/remove zeros & put into new temp list for checking
        tempList = list(filter((0).__ne__, checkList))
        #print("tl:",tempList)
        
        # check for duplicates in the list
        dupes = [x for x, y in collections.Counter(tempList).items() if y > 1]
        if len(dupes) > 0:
            #print("Found:",dupes,"length:",len(tempList))
            error = True
            # return all columns that contain an error
            errorID.append(tempList)
        else:
            print("Not Found")

    returnVal = error,errorID
    return returnVal


def elim():
    print("Attempting to solve...")
    rmv = []
    for i in range(len(board)):
        
        # compare board & remainRow values
        rmv = set(board[i]) & set(remainRow[i])

        # eliminate values from "remainRow" that are also in "board" row
        remainRow[i] = list(set(remainRow[i]) - rmv)

    rmv = []
    for i in range(len(board)):
        for j in range(len(board)):

            if board[j][i] in remainCol[i]:
                remainCol[i].remove(board[j][i])

    print(remainCol)

    remaining = remainRow,remainCol
    return remaining

# inputs for board
def populate(board):
    

    #board = [[0 for i in range(0, size)] for i in range(0, size)]
    
##    print("Initial state:")
##    for i in range(len(board)):
##        error = True
##        while error:
##            tempListRow = []
##            tempListCol = []
##            board[i] = input('row ' + str(i+1) + ': ')
##            board[i] = board[i].split(',')
##            
##            if len(board[i]) == size:
##                error = False
##            else:
##                print("Input error")
##            
##            for j in range(len(board[i])):
##                try:
##                    board[i][j] = int(board[i][j])
##                except:
##                    print("Invalid input")
##                    error = True
##                    break
##                if board[i][j] not in tempListRow:
##                    # don't put zero fillers in checking list
##                    if board[i][j] != 0:
##                        tempListRow.append(board[i][j])
##                        tempListCol.append(board[j][i])
##
##                elif board[i][j] in tempListRow:
##                    print("Invalid Row:", tempListRow)
##                    printBoard()
##                    error = True
##                    break

    board = [[3,0,4,0],[0,1,0,2],[0,4,0,3],[2,0,1,0]]
    
    if not check(board)[0]:
        pass
        
    elif check(board)[0]:
        print("Invalid Column(s):", check(board)[1])
        printBoard()
        populate(board)

populate(board)
printBoard()
solve(board)
printBoard()
elim()
