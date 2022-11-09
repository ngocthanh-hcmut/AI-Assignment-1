from ds import *

def readInput(level):
    file = open("Input/" + str(level), "r")

    squares = file.readlines()
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
    
    floor = Floor(squares, width, height, hole)
    block = Block(position1, position2)

    return State(block, floor)
