
from Square.XToggleSquare import XToggleSquare
from State import State
from Square.Square import Square
from Square.HoleSquare import HoleSquare
from Square.NoneSquare import NoneSquare
from Square.WeakSquare import WeakSquare
from Square.CircleToggleSquare import CircleToggleSquare


class StateGenetic(State):
    
    def moveUp(self, floor):
        super().moveUp()
        self.checkGameStatus(floor)

    def moveDown(self, floor):
        super().moveDown()
        self.checkGameStatus(floor)
        
    def moveLeft(self, floor):
        super().moveLeft()
        self.checkGameStatus(floor)
        
    def moveRight(self, floor):
        super().moveRight()
        self.checkGameStatus(floor)
    
    def checkGameStatus(self, floor):
        for square in self.block.currentSquare:
            xPosition = square["xPosition"]
            yPosition = square["yPosition"]
            if xPosition < 0 or yPosition < 0 or xPosition >= floor.floorWidth / Square.width or yPosition >= floor.floorHeight/Square.height:
                self.gameLose()
                return False
            if isinstance(self.floor.squares[yPosition][xPosition], NoneSquare):
                self.gameLose()
                return False
            if isinstance(self.floor.squares[yPosition][xPosition], WeakSquare) and self.isStanding():
                self.gameLose()
                return False
            if isinstance(self.floor.squares[yPosition][xPosition], HoleSquare) and self.isStanding():
                self.gameWin()
                return True
            if isinstance(self.floor.squares[yPosition][xPosition], CircleToggleSquare):
                self.floor.squares[yPosition][xPosition].toggle(self.floor)
            if isinstance(self.floor.squares[yPosition][xPosition], XToggleSquare) and self.isStanding():
                self.floor.squares[yPosition][xPosition].toggle(self.floor)

        return None

    def gameWin(self):
        self.status = "win"
        print("You win")

    def gameLose(self):
        self.status = "lose"
        print("You lose")


