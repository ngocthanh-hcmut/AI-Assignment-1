
from Square.HideSquare import HideSquare
from Square.CircleToggleSquare import CircleToggleSquare
from Square.XToggleSquare import XToggleSquare
from Square.Square import Square
from Square.HoleSquare import HoleSquare
from Square.NoneSquare import NoneSquare
from Square.WeakSquare import WeakSquare


class State:
    
    def __init__(self, block, Floor, parent=None) -> None:
        self.block = block
        self.floor = Floor
        self.status = ""
        self.parent = parent

    def isStanding(self):
        return True if len(self.block.currentSquare) == 1 else False

    def isLying(self):
        return True if len(self.block.currentSquare) == 2 else False
    
    def isLyingHorizontal(self):
        if self.isStanding(): return False
        if self.block.currentSquare[0]["yPosition"] == self.block.currentSquare[1]["yPosition"]:
            return True
        else:
            return False
    
    def isLyingVertical(self):
        if self.isStanding(): return False
        if self.block.currentSquare[0]["xPosition"] == self.block.currentSquare[1]["xPosition"]:
            return True
        else:
            return False

    def moveUp(self):
        if self.status == "win" or self.status == "lose":
            return
        if self.isStanding():
            currentSquare = self.block.currentSquare[0]
            self.block.currentSquare = [
                dict(xPosition = currentSquare["xPosition"], yPosition = currentSquare["yPosition"]-1),
                dict(xPosition = currentSquare["xPosition"], yPosition = currentSquare["yPosition"]-2)
            ]
        elif self.isLying():
            if self.isLyingHorizontal():
                self.block.currentSquare[0]["yPosition"] -= 1
                self.block.currentSquare[1]["yPosition"] -= 1
            elif self.isLyingVertical():
                yPositionMin = min(self.block.currentSquare[0]["yPosition"], self.block.currentSquare[1]["yPosition"])
                newSquare = dict(xPosition = self.block.currentSquare[0]["xPosition"], yPosition = yPositionMin - 1)
                self.block.currentSquare = [newSquare]

    def moveDown(self):
        if self.status == "win" or self.status == "lose": return
        if self.isStanding():
            currentSquare = self.block.currentSquare[0]
            self.block.currentSquare = [
                dict(xPosition = currentSquare["xPosition"], yPosition = currentSquare["yPosition"]+1),
                dict(xPosition = currentSquare["xPosition"], yPosition = currentSquare["yPosition"]+2)
            ]
        elif self.isLying():
            if self.isLyingHorizontal():
                self.block.currentSquare[0]["yPosition"] += 1
                self.block.currentSquare[1]["yPosition"] += 1
            elif self.isLyingVertical():
                yPositionMax = max(self.block.currentSquare[0]["yPosition"], self.block.currentSquare[1]["yPosition"])
                newSquare = dict(xPosition = self.block.currentSquare[0]["xPosition"], yPosition = yPositionMax + 1)
                self.block.currentSquare = [newSquare]
        
    def moveLeft(self):
        if self.status == "win" or self.status == "lose": return
        if self.isStanding():
            currentSquare = self.block.currentSquare[0]
            self.block.currentSquare = [
                dict(xPosition = currentSquare["xPosition"]-1, yPosition = currentSquare["yPosition"]),
                dict(xPosition = currentSquare["xPosition"]-2, yPosition = currentSquare["yPosition"])
            ]
        elif self.isLying():
            if self.isLyingVertical():
                self.block.currentSquare[0]["xPosition"] -= 1
                self.block.currentSquare[1]["xPosition"] -= 1
            elif self.isLyingHorizontal():
                xPositionMin = min(self.block.currentSquare[0]["xPosition"], self.block.currentSquare[1]["xPosition"])
                newSquare = dict(xPosition = xPositionMin - 1, yPosition = self.block.currentSquare[0]["yPosition"])
                self.block.currentSquare = [newSquare]
        
    def moveRight(self):
        if self.status == "win" or self.status == "lose": return
        if self.isStanding():
            currentSquare = self.block.currentSquare[0]
            self.block.currentSquare = [
                dict(xPosition = currentSquare["xPosition"]+1, yPosition = currentSquare["yPosition"]),
                dict(xPosition = currentSquare["xPosition"]+2, yPosition = currentSquare["yPosition"])
            ]
        elif self.isLying():
            if self.isLyingVertical():
                self.block.currentSquare[0]["xPosition"] += 1
                self.block.currentSquare[1]["xPosition"] += 1
            elif self.isLyingHorizontal():
                xPositionMax = max(self.block.currentSquare[0]["xPosition"], self.block.currentSquare[1]["xPosition"])
                newSquare = dict(xPosition = xPositionMax + 1, yPosition = self.block.currentSquare[0]["yPosition"])
                self.block.currentSquare = [newSquare]

    def checkGameStatus(self, screen = None):
        for square in self.block.currentSquare:
            xPosition = square["xPosition"]
            yPosition = square["yPosition"]
            if xPosition < 0 or yPosition < 0 or xPosition >= self.floor.floorWidth / Square.width or yPosition >= self.floor.floorHeight/Square.height:
                self.gameLose()
                return False
            if isinstance(self.floor.squares[yPosition][xPosition], WeakSquare) and self.isStanding():
                self.gameLose()
                return False
            if isinstance(self.floor.squares[yPosition][xPosition], HoleSquare) and self.isStanding():
                self.gameWin()
                return True
            if isinstance(self.floor.squares[yPosition][xPosition], CircleToggleSquare):
                self.floor.squares[yPosition][xPosition].toggle(screen)
            if isinstance(self.floor.squares[yPosition][xPosition], XToggleSquare) and self.isStanding():
                self.floor.squares[yPosition][xPosition].toggle(screen)
            if isinstance(self.floor.squares[yPosition][xPosition], HideSquare) and not(self.floor.squares[yPosition][xPosition].enabled):
                self.gameLose()
                return False
            if isinstance(self.floor.squares[yPosition][xPosition], NoneSquare) and not(isinstance(self.floor.squares[yPosition][xPosition], HideSquare)):
                self.gameLose()
                return False
        return None

    def gameWin(self):
        self.status = "win"

    def gameLose(self):
        self.status = "lose"

    def renderBlock(self, screen):
        self.block.render(screen)

    def renderFloor(self, screen):
        for squareRow in self.floor.squares:
            for square in squareRow:
                square.render(screen)

