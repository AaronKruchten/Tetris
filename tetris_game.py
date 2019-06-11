# events-example0.py
# Barebones timer, mouse, and keyboard events
# Aaron Kruchten
# akruchte
# Rafael Marmol
#rmarmol

from tkinter import *
from random import *
import copy

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.cell_size = 25
    data.rows = 15
    data.cols = 10
    data.emptyColor = 'blue'
    data.board = [[data.emptyColor] * data.cols for i in range(data.rows)]
    # taken from tutorial
    # pre-load a few cells with known colors for testing purposes
    data.margin = 30
    data.tetrisPieces = getTetrisPieces()
    # taken from tutorial 
    data.tetrisPieceColors = [ "red", "yellow", "magenta", "pink",
     "cyan", "green", "orange" ]
    data.color = 'blue'
    data.isGameOver = False
    data.score = 0
    newFallingPiece(data)


def getTetrisPieces():
    # function simply returns list of possible tetris pieces
    # tetris piece lists copied from tutorial
    iPiece = [
    [ True,  True,  True,  True]]
    jPiece = [
    [ True, False, False ],[ True, True,  True]]
    lPiece = [
    [ False, False, True],[ True,  True,  True]]
    oPiece = [
    [ True, True],[ True, True]]
    sPiece = [
    [ False, True, True],[ True,  True, False ]]
    tPiece = [
    [ False, True, False ],[ True,  True, True]]
    zPiece = [
    [ True,  True, False ],[ False, True, True]]
    return [iPiece,jPiece,lPiece,oPiece,sPiece,tPiece,zPiece]

'''
def testGetTetrisPieces():
    iPiece = [
    [ True,  True,  True,  True]]
    jPiece = [
    [ True, False, False ],[ True, True,  True]]
    lPiece = [
    [ False, False, True],[ True,  True,  True]]
    oPiece = [
    [ True, True],[ True, True]]
    sPiece = [
    [ False, True, True],[ True,  True, False ]]
    tPiece = [
    [ False, True, False ],[ True,  True, True]]
    zPiece = [
    [ True,  True, False ],[ False, True, True]]
    assert(getTetrisPieces() == [iPiece,jPiece,lPiece,
        oPiece,sPiece,tPiece,zPiece])
'''





def newFallingPiece(data):
    # calculates a new tetris piece choosing a random piece from the list
    # of possible pieces and chooses a random color from a list of possible
    # colors
    if data.isGameOver == False:
        color = choice(data.tetrisPieceColors)
        tetrisPiece = choice(data.tetrisPieces)
        data.fallingPiece = tetrisPiece
        fallingPieceCol = len(tetrisPiece[0])
        data.fallingPieceColor = color
        data.fallingPieceRow = 0
        data.fallingPieceCol = data.cols//2 - fallingPieceCol//2
    


def testNewFallingPiece():
    dummy_string = 'abc'
    # template copied from piazza
    class Struct(object): pass
    data = Struct()
    # populate the data with what you want here
    # color is not important for test so we place blue as a dummy color
    data.isGameOver = False
    data.tetrisPieceColors = ['blue']
    # set to random string so that fucntion will not fail
    data.tetrisPieces = [[dummy_string]]
    data.cols = 10
    data.fallingPiece = [
    [ False, False, True],[ True,  True,  True]]
    # call the function you are testing
    newFallingPiece(data)
    assert(data.fallingPieceCol == 4)
    data.fallingPiece =[
    [ True,  True, False ],[ False, True, True]]
    assert(data.fallingPieceCol == 4)
    
def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # function moves pieces according to key presses
    if data.isGameOver == False:
        if event.keysym == 'Right': 
            moveFallingPiece(data,0,+1)
        if event.keysym == 'Left': moveFallingPiece(data,0,-1)
        if event.keysym == 'Down': moveFallingPiece(data,+1,0)
        if event.keysym == 'Up': 
            rotateFallingPiece(data)
        if fallingPieceIsLegal(data) == False:
            # if a falling piece is not legal we rotate the piece
            # three times thus returning it to its original state
            rotateFallingPiece(data)
            rotateFallingPiece(data)
            rotateFallingPiece(data)
    else:
        if event.keysym == 'r':
            init(data)

def rotateFallingPiece(data):
    new_col = data.fallingPieceRow
    old_piece = copy.deepcopy(data.fallingPiece)
    rows, cols = len(old_piece),len(old_piece[0])
    new_piece = []
    # rotates piece by going backwards through each row by the last columns
    # in the list going backwards
    for col in range(cols-1,-1,-1):
        lst = []
        for row in range(rows):
            lst += [old_piece[row][col]]
        new_piece += [lst]
    data.fallingPiece = new_piece
    # calculates the closest possible new_center after a piece has been rotated
    new_row = data.fallingPieceRow + len(old_piece)//2 - len(old_piece[0])//2
    data.fallingPieceRow = new_row
    # calculates the closes possible new_center col after piece is rotated
    new_col = data.fallingPieceCol + len(old_piece[0])//2 - len(old_piece)//2
    data.fallingPieceCol = new_col

def testRotateFallingPiece():
    # framework copied from piazza
    class Struct(object): pass
    data = Struct()
    # populate the data with what you want here
    data.fallingPieceRow = 5
    data.fallingPiece = [
    [ True, False, False ],[ True, True,  True]]
    data.fallingPieceCol = 7
    # call the function you are testing
    rotateFallingPiece(data)
    # check if data contains the correctly modified values
    assert(data.fallingPiece == [[False,True],[False,True],[True,True]])
    assert(data.fallingPieceRow == 5)
    assert(data.fallingPieceCol == 7)
    data.fallingPiece = [
    [ True,  True, False ],[ False, True, True]]
    rotateFallingPiece(data) 
    assert(data.fallingPiece == 
        [[False, True], [True, True], [True, False]])
    assert(data.fallingPieceRow == 5)
    assert(data.fallingPieceCol == 7)

def moveFallingPiece(data, drow, dcol):
    # moves the falling piece according to the players key press
    # subtracting/adding rows and cols accordingly
    old_falling_piece_row = data.fallingPieceRow
    old_falling_piece_col = data.fallingPieceCol
    data.fallingPieceRow += drow
    data.fallingPieceCol += dcol
    # if the players move would result in a piece out of the board 
    # it return to the old piece
    if fallingPieceIsLegal(data) == False:
        data.fallingPieceRow -= drow
        data.fallingPieceCol -= dcol
        return False
    return True


def fallingPieceIsLegal(data):
    rows, cols = len(data.fallingPiece),len(data.fallingPiece[0])
    for row in range(rows):
        for col in range(cols):
            if data.fallingPiece[row][col] == True:
                # checks to see if falling piece is outside of the board
                if (data.fallingPieceRow + row +1> data.rows or 
                    data.fallingPieceCol + col+1> data.cols or 
                    data.fallingPieceRow < 0 or
                    data.fallingPieceCol < 0):
                    return False
                # checks to see if all pieces under movement are blue
                # if they are another color then there is another piece 
                # there and it returns False
                if (data.board[data.fallingPieceRow+row][data.fallingPieceCol
                    +col]!=
data.emptyColor):
                    return False
    return True




def timerFired(data):
    if moveFallingPiece(data,+1,0) == False:
        # if piece is in illegal position this checks to see if
        # it is at the bottom of the board
        placeFallingPiece(data)
    if moveFallingPiece(data,0,0) == False:
        # if pieces are immediately false
        # game gets set to over
        data.isGameOver = True
    removeFullRows(data)

def removeFullRows(data):
    # function removes full rows adding to the player's score
    newRow = []
    fullRows = 0
    for row in range(data.rows-1,-1,-1):
        if data.emptyColor in data.board[row]:
            newRow += [data.board[row]]
        if data.emptyColor not in data.board[row]:
            fullRows += 1
    newRow += [[data.emptyColor] * data.cols for row in range(fullRows)]
    newRow = newRow[::-1]
    data.board = newRow
    data.score += fullRows**2



def placeFallingPiece(data):
    ## figures out if a falling piece is at the bottom of the board
    # if it is piece stays at bottom
    rows,cols = len(data.fallingPiece),len(data.fallingPiece[0])
    if moveFallingPiece(data,+1,0) == False:
        for row in range(rows):
            for col in range(cols):
                if data.fallingPiece[row][col] == True:
                    data.board[data.fallingPieceRow+
                    row][data.fallingPieceCol+col] = data.fallingPieceColor
    newFallingPiece(data)




def redrawAll(canvas, data):
    # calls three helpers to redraw the entire board
    drawGame(canvas,data)
    drawFallingPiece(canvas,data)
    drawScore(canvas,data)

def drawScore(canvas,data):
    # draws the score in the bottom of the tetris board
    score_margin = 10
    y= data.height - score_margin # bottom of the board
    canvas.create_text(data.width/2,y,text = 'Score:%d' %data.score,
        font = 'Times 12 bold')

def drawFallingPiece(canvas,data):
    # function draws the falling piece
    rows,cols = len(data.fallingPiece),len(data.fallingPiece[0])
    # loops through falling piece
    # if value is true it draws that cell
    for row in range(rows):
        for col in range(cols):
            if data.fallingPiece[row][col] == True:
                drawCell(canvas,data.fallingPieceRow+row,data.fallingPieceCol + 
                    col,data,data.fallingPieceColor)



def drawGame(canvas,data):
    # function draws the board 
    canvas.create_rectangle(0,0,data.width,data.height,fill='orange')
    if data.isGameOver == False:
        drawBoard(canvas,data)
    else:
        # if game is  function draws a orange rectangle in 
        # front of the board
        data.fallingPiece = 'None'
        drawBoard(canvas,data)
        canvas.create_text(data.width/2,data.height/2,
            text="Game Over Press 'r' to restart", font ='Times 15 bold',
            fill = 'white')
        data.mode = 'Restart'





def drawBoard(canvas,data):
    # draws the orange border around the game
    for row in range(data.rows):
        for col in range(data.cols):
            color = data.board[row][col]
            drawCell(canvas,row,col,data,color)






def getCell(row,col,data,color):
    # function gets cell dimensions for drawing each cell
    black_rectangle_margin = 1
    blue_cellR = data.cell_size/2 - black_rectangle_margin
    black_cellR = data.cell_size /2
    cx = data.margin + data.cell_size * col
    cy = data.margin + data.cell_size* row 
    return (black_rectangle_margin,blue_cellR,black_cellR,cx,cy)


    





def drawCell(canvas,row,col,data,color):
    cell_center_x_index = 3
    cell_center_y_index =4
    cellDimensionTuple = getCell(row,col,data,color)
    black_rectangle_margin = cellDimensionTuple[0]
    blue_cellR = cellDimensionTuple[1]
    black_cellR = cellDimensionTuple[2]
    cx = cellDimensionTuple[cell_center_x_index]
    cy = cellDimensionTuple[cell_center_y_index]
    # creates black cells that surround blue cells
    canvas.create_rectangle(cx - black_cellR,cy - black_cellR,cx + 
        black_cellR,cy+black_cellR,fill = 'black')
    canvas.create_rectangle(cx - blue_cellR,cy - blue_cellR,cx + 
        blue_cellR,cy+blue_cellR,fill = color)





####################################
# use the run function as-is
####################################

def playTetris():
    rows,cols = 15,10
    cell_size = 25
    margin = 40
    height = rows * cell_size + margin 
    width = cols * cell_size + margin 
    run(width,height)



def run(width, height):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 400 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


def testAll():
    testNewFallingPiece()
    #testGetTetrisPieces()
    testRotateFallingPiece()
    print('tests passed')



testAll()
playTetris()










