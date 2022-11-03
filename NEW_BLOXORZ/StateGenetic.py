

import copy
from time import sleep
from Square.XToggleSquare import XToggleSquare
from State import State
from Square.Square import Square
from Square.HoleSquare import HoleSquare
from Square.NoneSquare import NoneSquare
from Square.WeakSquare import WeakSquare
from Square.HideSquare import HideSquare
from Square.CircleToggleSquare import CircleToggleSquare
# import pygame


class StateGenetic(State):

    def __init__(self, block, Floor) -> None:
        super().__init__(block, Floor)
        self.selectionRate = 0
        self.fitnessScore = 0
        self.DNA = []

    def thrive(self, screen):
        print("state begin thrive")
        for move in self.DNA:
            oldSquares = [dict(xPosition=a["xPosition"], yPosition=a["yPosition"]) for a in self.block.currentSquare]
            sleep(0.5)
            if move == 1:
                self.moveUp()
            if move == 2:
                self.moveDown()
            if move == 3:
                self.moveLeft()
            if move == 4:
                self.moveRight()
            if self.checkGameStatus() == False:
                self.render(screen, oldSquares)
                self.block.currentSquare = oldSquares
                break
            self.render(screen, oldSquares)
        # print(self.block.currentSquare)
        self.render(screen, self.block.currentSquare, True)
    
    def checkGameStatus(self, screen):
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
        print("You win")

    def gameLose(self):
        self.status = "lose"
        # self.block.color = pygame.Color(255, 255, 255)
        print("You lose")

    def render(self, screen, oldSquares, renderBlock = False):
        for squareDict in oldSquares:
            x = squareDict["xPosition"]
            y = squareDict["yPosition"]
            self.floor.squares[y][x].render(screen)
        if self.status == "lose" or renderBlock: return
        super().renderBlock(screen)


