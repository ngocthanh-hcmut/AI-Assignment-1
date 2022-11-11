import copy


class Floor:
    def __init__(self, squares, width, height, hole):
        self.squares = squares
        self.width = width
        self.height = height
        self.hole = hole

    def __eq__(self, other):
        return self.squares == other.squares


class Square:
    def __init__(self): pass

    def __eq__(self, other):
        return type(self) == type(other)

class NormalSquare(Square):
    def __init__(self) -> None:
        super().__init__()
    
    def __eq__(self, other):
        return type(self) == type(other)

class WeakSquare(Square):
    def __init__(self) -> None:
        super().__init__()
        
class XSwitch(Square):
    def __init__(self, action = 'both') -> None:
        super().__init__()
        self.toggleSquares = []
        self.action = action

    def toggle(self):
        for square in self.toggleSquares:
            if self.action == 'open':
                square.isOpen = True
            elif self.action == 'close':
                square.isOpen = False
            elif self.action == 'both':
                square.isOpen = not square.isOpen
    
class OSwitch(Square):
    def __init__(self, action = 'both') -> None:
        super().__init__()
        self.toggleSquares = []
        self.action = action

    def toggle(self):
        for square in self.toggleSquares:
            if self.action == 'open':
                square.isOpen = True
            elif self.action == 'close':
                square.isOpen = False
            elif self.action == 'both':
                square.isOpen = not square.isOpen 

class ToggleSquare(Square):
    def __init__(self, isOpen):
        super().__init__()
        self.isOpen = isOpen
    
    def __eq__(self, other):
        return super().__eq__(other) and self.isOpen == other.isOpen

class Hole(Square):
    def __init__(self) -> None:
        super().__init__()

class NoneSquare(Square):
    def __init__(self) -> None:
        super().__init__()


class Block:
    def __init__(self, position1, position2):
        assert(position1.x <= position2.x and position1.y <= position2.y), "Position of blok is not valid: p1=" + position1 + ", p2=" + position2
        self.position1 = position1
        self.position2 = position2

    def __eq__(self, other):
        return self.position1 == other.position1 and self.position2 == other.position2
    
    def isStanding(self):
        return self.position1 == self.position2

    def isLyingHorizontally(self):
        return (self.position1 != self.position2) and (self.position1.x == self.position2.x)
        
    def isLyingVertically(self):
        return (self.position1 != self.position2) and (self.position1.x != self.position2.x)

    def moveUp(self):
        if self.isStanding():
            self.position1.x -= 2
            self.position2.x -= 1
    
        elif self.isLyingHorizontally():
            self.position1.x -= 1
            self.position2.x -= 1
        
        else:
            self.position1.x -= 1
            self.position2.x -= 2

    def moveDown(self):
        if self.isStanding():
            self.position1.x += 1
            self.position2.x += 2
            
        elif self.isLyingHorizontally():
            self.position1.x += 1
            self.position2.x += 1
        
        else:
            self.position1.x += 2
            self.position2.x += 1

    def moveLeft(self):
        if self.isStanding():
            self.position1.y -= 2
            self.position2.y -= 1
            
        elif self.isLyingHorizontally():
            self.position1.y -= 1
            self.position2.y -= 2
        
        else:
            self.position1.y -= 1
            self.position2.y -= 1

    def moveRight(self):
        if self.isStanding():
            self.position1.y += 1
            self.position2.y += 2
            
        elif self.isLyingHorizontally():
            self.position1.y += 2
            self.position2.y += 1
        
        else:
            self.position1.y += 1
            self.position2.y += 1


class Position:
    # (0,0) -------------> y
    #   |
    #   |
    #   |
    #   |
    #   v
    # 
    #   x

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        

class State:
    def __init__(self, block, floor, parent = None):
        self.block = block
        self.floor = floor
        self.parent = parent

    def __eq__(self, other):
        return self.block == other.block and self.floor == other.floor
        # return self.block == other.block

    def checkBridge(self):
        x1 = self.block.position1.x
        y1 = self.block.position1.y
        
        x2 = self.block.position2.x
        y2 = self.block.position2.y
        
        squares = self.floor.squares

        if not self.block.isStanding():
            if isinstance(squares[x1][y1], OSwitch):
                squares[x1][y1].toggle()
            if isinstance(squares[x2][y2], OSwitch):
                squares[x2][y2].toggle()

        elif isinstance(squares[x1][y1], OSwitch) or isinstance(squares[x1][y1], XSwitch):
            squares[x1][y1].toggle()
            

    def isValidState(self):
        x1 = self.block.position1.x
        y1 = self.block.position1.y
        
        x2 = self.block.position2.x
        y2 = self.block.position2.y

        width = self.floor.width
        height = self.floor.height
        squares = self.floor.squares

        if x1 < 0 or x2 < 0 or x1 >= height or x2 >= height or y1 < 0 or y2 < 0 or y1 >= width or y2 >= width: # Check out of floor
            return False 

        elif isinstance(squares[x1][y1], NoneSquare) or isinstance(squares[x2][y2], NoneSquare): # Check falls
            return False

        elif self.block.isStanding() and isinstance(squares[x1][y1], WeakSquare): # Check stand on weak square
            return False

        elif (isinstance(squares[x1][y1], ToggleSquare) and not squares[x1][y1].isOpen) or (isinstance(squares[x2][y2], ToggleSquare) and not squares[x2][y2].isOpen): # Check falls in closed toggle square
            return False 
        
        return True

    def generateChildren(self):
        up = copy.deepcopy(self)
        up.block.moveUp()

        right = copy.deepcopy(self)
        right.block.moveRight()

        down = copy.deepcopy(self)
        down.block.moveDown()

        left = copy.deepcopy(self)
        left.block.moveLeft()

        children = [up, right, down, left]
        children = [child for child in children if child.isValidState()]
        
        for i in range(len(children)):
            children[i].parent = self
            children[i].checkBridge()

        return children
    
    def checkGameStatus(self):
        return self.block.isStanding() and self.block.position1 == self.floor.hole


class Chromosome:
    def __init__(self, length, DNAs = [], score = 0):
        self.length = length
        self.DNAs = DNAs
        self.score = score
        
    