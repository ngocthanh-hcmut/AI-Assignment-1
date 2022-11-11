from time import sleep
from ds import *
from colored import fg

def matchColor(character):
    if character == '0':
        return fg('black') + character

    elif character == '1':
        return fg('white') + character

    elif character == '#':
        return fg('yellow') + character

    elif character == 'x' or character == 'o':
        return fg('green') + character

    elif character == 'w':
        return fg('light_red') + character

    elif character == 'h':
        return fg('blue') + character

    elif character == '-':
        return fg('white') + character


    
def printPath(state):
    if state.parent:
        printPath(state.parent)
    printStateColor(state)
    sleep(0.2)

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
            
            elif isinstance(squares[x][y], OSwitch):
                squares[x][y] = 'o'

            elif isinstance(squares[x][y], XSwitch):
                squares[x][y] = 'x'

            elif isinstance(squares[x][y], ToggleSquare) and squares[x][y].isOpen:
                squares[x][y] = '1'

            elif isinstance(squares[x][y], ToggleSquare) and not squares[x][y].isOpen:
                squares[x][y] = '0'

    # lines = []
    # for row in squares:
    #     lines.append(' '.join(str(x) for x in row))
    # print('\n'.join(lines))
    
    # seperate = ''
    # for i in range(2*len(squares[0])):
    #     seperate += '-'
    # print(seperate)



def printStateColor(state):
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
            
            elif isinstance(squares[x][y], OSwitch):
                squares[x][y] = 'o'

            elif isinstance(squares[x][y], XSwitch):
                squares[x][y] = 'x'

            elif isinstance(squares[x][y], ToggleSquare) and squares[x][y].isOpen:
                squares[x][y] = '1'

            elif isinstance(squares[x][y], ToggleSquare) and not squares[x][y].isOpen:
                squares[x][y] = '0'

    lines = []
    for row in squares:
        lines.append(' '.join(matchColor(str(x)) for x in row))
    print('\n'.join(lines))

    seperate = ''
    for i in range(2*len(squares[0])):
        seperate += fg('white') + '-'
    print(seperate)