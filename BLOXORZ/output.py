from ds import *

def printPath(state):
    if state.parent:
        printPath(state.parent)
    printState(state)

def printState(state):
    pos1 = state.block.position1
    pos2 = state.block.position2

    squares = state.floor.squares
    squares[pos1.x][pos1.y] = '#'
    squares[pos2.x][pos2.y] = '#'

    for x in range(state.floor.height):
        for y in range(state.floor.width):
            if isinstance(squares[x][y], NormalSquare):
                squares[x][y] = '1'
            elif isinstance(squares[x][y], NoneSquare):
                squares[x][y] = '0'
            elif isinstance(squares[x][y], Hole):
                squares[x][y] = 'h'
            elif isinstance(squares[x][y], WeakSquare):
                squares[x][y] = 'w'

    lines = []
    for row in squares:
        lines.append(' '.join(str(x) for x in row))
    print('\n'.join(lines))
    print("---------------------------")

    # squares[pos1.x][pos1.y] = NormalSquare()
    # squares[pos2.x][pos2.y] = NormalSquare()
