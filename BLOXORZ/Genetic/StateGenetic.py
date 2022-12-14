

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

    def __init__(self, block, Floor, scoreMap = None, DNA=None, id = 0) -> None:
        # print("state", id,": making new state. DNA: ", DNA)
        super().__init__(block, Floor)
        self.selectionRate = 0
        self.fitnessScore = 0
        self.DNA = DNA
        self.scoreMap = scoreMap
        self.longestMove = 0
        self.id = id

    def thrive(self, screen=None, block = False):
        # print("state", self.id, "thriving")
        # self.setFitnessScore(0)
        
        # py game ------
        if screen:
            self.clearAndRender(screen, None, True)
        # -------

        for i in range(len(self.DNA)):


            if self.status == "lose" or self.status == "win":
                break

            oldSquares = [dict(xPosition=a["xPosition"], yPosition=a["yPosition"]) for a in self.block.currentSquare]
            #pygame
            if block:
                sleep(0.5)
            # ---
            if self.DNA[i] == 1:
                self.moveUp()
            if self.DNA[i] == 2:
                self.moveRight()
            if self.DNA[i] == 3:
                self.moveLeft()
            if self.DNA[i] == 4:
                self.moveDown()
            self.checkGameStatus()
            if self.status == "" or self.status == "win":
                self.setFitnessScore(i)

            # pygame -----
            if self.status == "" and screen:
                self.clearAndRender(screen, oldSquares, True)
            
            if screen and self.status == "win":
                self.clearAndRender(screen, oldSquares, True)
                sleep(0.5)
            # ----

        if self.status == "win":
            return self.DNA
        else:
            return False
    
    def checkGameStatus(self, screen=None):
        for square in self.block.currentSquare:
            xPosition = square["xPosition"]
            yPosition = square["yPosition"]
            if xPosition < 0 or yPosition < 0 or xPosition >= len(self.floor.squares[0]) or yPosition >= len(self.floor.squares):
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
        # print("You win")

    def gameLose(self):
        self.status = "lose"
        # print("state", self.id, "lose")
        # self.block.color = pygame.Color(255, 255, 255)
        # # print("You lose")

    def clearAndRender(self, screen, oldSquares, renderBlock):
        if oldSquares != None:
            for squareDict in oldSquares:
                x = squareDict["xPosition"]
                y = squareDict["yPosition"]
                self.floor.squares[y][x].render(screen)
        if self.status == "lose" or not(renderBlock): return
        super().renderBlock(screen)

    def moveUp(self):
        # print("state", self.id, "moving up")
        if self.status == "win" or self.status == "lose":
            return
        return super().moveUp()
    
    def moveDown(self):
        # print("state", self.id, "moving down")
        if self.status == "win" or self.status == "lose":
            return
        return super().moveDown()

    def moveLeft(self):
        # print("state", self.id, "moving left")
        if self.status == "win" or self.status == "lose":
            return
        return super().moveLeft()

    def moveRight(self):
        # print("state", self.id, "moving right")
        if self.status == "win" or self.status == "lose":
            return
        return super().moveRight()

    def mutate(self, rate, index):
        if index >= len(self.DNA):
            lenght = len(self.DNA)
            self.DNA = [random.randint(1,4) for i in range(lenght)]
        else:
            i = random.randint(1, 100)
            if i > rate:
                return
            pad = random.randint(0,2)
            # pad = 0
            newIndex = index - pad if index - pad >= 0 else index
            move = self.DNA[newIndex]
            while move == self.DNA[newIndex]:
                move = random.randint(1,4)
            self.DNA[newIndex] = move
            # print("state:", self.id," mutate at position:", newIndex, "by", move)


    def reset(self, dna):
        self.fitnessScore = 0
        self.crossPosition = 0
        self.floor.reset()
        self.block.currentSquare = [
            dict(xPosition=self.floor.startSquare.xPosition, yPosition=self.floor.startSquare.yPosition)
        ]
        self.status = ""
        self.DNA = dna

    def setFitnessScore(self, moveIndex):
        # print("state", self.id, "setting finess score")
        score = 0
        for position in self.block.currentSquare:
            # print(position)
            tmp = self.scoreMap[position["yPosition"]][position["xPosition"]]
            score = tmp if tmp > score else score
            score = score * 4
        if self.fitnessScore < score:
            # print("state", self.id, "applying score:", score)
            self.fitnessScore = score
        self.longestMove = moveIndex
