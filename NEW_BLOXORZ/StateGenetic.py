

import copy
import random
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

    def __init__(self, block, Floor, DNA=None) -> None:
        super().__init__(block, Floor)
        self.selectionRate = 0
        self.fitnessScore = 0
        self.DNA = DNA

    def thrive(self, screen):
        self.clearAndRender(screen, None, True)
        for move in self.DNA:
            oldSquares = [dict(xPosition=a["xPosition"], yPosition=a["yPosition"]) for a in self.block.currentSquare]
            
            if self.status == "win":
                self.clearAndRender(screen, None, True)
                continue
            if  self.status == "lose":
                continue
            
            sleep(0.25)
            
            if move == 1:
                # print("moving up")
                self.moveUp()
            if move == 2:
                # print("moving down")
                self.moveDown()
            if move == 3:
                # print("moving left")
                self.moveLeft()
            if move == 4:
                # print("moving right")
                self.moveRight()
            
            self.checkGameStatus(screen)
            
            if self.status == "":
                self.clearAndRender(screen, oldSquares, True)
            
            if  self.status == "lose":
                self.clearAndRender(screen, oldSquares, False)
                self.block.currentSquare = oldSquares
                continue


        # print(self.block.currentSquare)
        self.clearAndRender(screen, self.block.currentSquare, False)
    
    def checkGameStatus(self, screen):
        for square in self.block.currentSquare:
            xPosition = square["xPosition"]
            yPosition = square["yPosition"]
            # print("current square: ", square, "xy=", xPosition, yPosition )
            # print("width=",len(self.floor.squares[0]), "height=", len(self.floor.squares))
            if xPosition < 0 or yPosition < 0 or xPosition >= len(self.floor.squares[0]) or yPosition >= len(self.floor.squares):
                self.gameLose()
                # print("111111111111")
                return False
            if isinstance(self.floor.squares[yPosition][xPosition], WeakSquare) and self.isStanding():
                self.gameLose()
                # print("22222222222")
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
                # print("33333333333333")
                return False
            if isinstance(self.floor.squares[yPosition][xPosition], NoneSquare) and not(isinstance(self.floor.squares[yPosition][xPosition], HideSquare)):
                self.gameLose()
                # print("444444444444")
                return False
            
        return None

    def gameWin(self):
        self.status = "win"
        print("You win")

    def gameLose(self):
        self.status = "lose"
        # self.block.color = pygame.Color(255, 255, 255)
        print("You lose")

    def clearAndRender(self, screen, oldSquares, renderBlock):
        if oldSquares != None:
            for squareDict in oldSquares:
                x = squareDict["xPosition"]
                y = squareDict["yPosition"]
                self.floor.squares[y][x].render(screen)
        if self.status == "lose" or not(renderBlock): return
        super().renderBlock(screen)

    def moveUp(self):
        if self.status == "win" or self.status == "lose":
            return
        return super().moveUp()
    
    def moveDown(self):
        if self.status == "win" or self.status == "lose":
            return
        return super().moveDown()

    def moveLeft(self):
        if self.status == "win" or self.status == "lose":
            return
        return super().moveLeft()

    def moveRight(self):
        if self.status == "win" or self.status == "lose":
            return
        return super().moveRight()

    def mutate(self, numberToMutate, dnaLength):
        for i in range(numberToMutate):
            positionToMutate = random.randint(0, dnaLength-1)
            self.DNA[positionToMutate] = random.randint(1, 4)


