from ds import *
from os.path import exists

def readInput(level):
    floorInput = open("Input/" + str(level), "r")
        
    squares = floorInput.readlines()
    for i in range(len(squares)):
        squares[i] = squares[i].split()

    height = len(squares)
    width = len(squares[0])
    
    for x in range(height):
        for y in range(width):
            if squares[x][y] == '1':
                squares[x][y] = NormalSquare()

            elif squares[x][y] == '0':
                squares[x][y] = NoneSquare()

            elif squares[x][y] == 's':
                position1 = Position(x, y)
                position2 = Position(x, y)
                squares[x][y] = NormalSquare()

            elif squares[x][y] == 'h':
                hole = Position(x, y)
                squares[x][y] = Hole()

            elif squares[x][y] == 'w':
                squares[x][y] = WeakSquare()

            elif squares[x][y] == 'o':
                squares[x][y] = OSwitch('both')
            elif squares[x][y] == 'o1':
                squares[x][y] = OSwitch('open')
            elif squares[x][y] == 'o0':
                squares[x][y] = OSwitch('close')

            elif squares[x][y] == 'x':
                squares[x][y] = XSwitch()
            elif squares[x][y] == 'x1':
                squares[x][y] = XSwitch('open')
            elif squares[x][y] == 'x0':
                squares[x][y] = XSwitch('close')

            elif squares[x][y] == 't0':
                squares[x][y] = ToggleSquare(False)
            elif squares[x][y] == 't1':
                squares[x][y] = ToggleSquare(True)
    

    if exists("Input/" + str(level) + "link"):

        linkInput = open("Input/" + str(level) + "link", "r")
        links = linkInput.readlines()
        
        for i in range(len(links)):
            links[i] = links[i].split()

        for i in range(len(links)):
            for j in range(len(links[i])):
                links[i][j] = links[i][j].split(',')
                
        for i in range(len(links)):
            x = int(links[i][0][0])
            y = int(links[i][0][1])
            
            for j in range(1, len(links[i])):
                xToggle = int(links[i][j][0])
                yToggle = int(links[i][j][1])
                squares[x][y].toggleSquares.append(squares[xToggle][yToggle])
            
    floor = Floor(squares, width, height, hole)
    block = Block(position1, position2)

    return State(block, floor)
