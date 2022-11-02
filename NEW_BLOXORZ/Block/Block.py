import os
import sys



dir =  os.getcwd()
sys.path.insert(0, dir+"/..")

from Floor.Floor import Floor
from Floor.NoneFloor import NoneFloor
from Floor.HoleFloor import HoleFloor
from Floor.WeakFloor import WeakFloor
from Floor.CircleToggleFloor import CircleToggleFloor
import pygame
from Floor.StartFloor import StartFloor
from Map import Map

# class Block đại diện cho một khối bloxorz
class Block:

    color = pygame.Color(238, 82, 83)

    def __init__(self, map: Map):
        self.map = map
        self.currentFloor = [
            dict(xPosition = map.startFloor.xPosition, yPosition = map.startFloor.yPosition)
        ]
        self.win = False
        self.lose = False

    def isStanding(self):
        return True if len(self.currentFloor) == 1 else False

    def isLying(self):
        return True if len(self.currentFloor) == 2 else False
    
    def isLyingHorizontal(self):
        if self.isStanding(): return False
        if self.currentFloor[0]["yPosition"] == self.currentFloor[1]["yPosition"]:
            return True
        else:
            return False
    
    def isLyingVertical(self):
        if self.isStanding(): return False
        if self.currentFloor[0]["xPosition"] == self.currentFloor[1]["xPosition"]:
            return True
        else:
            return False

    def render(self, screen):
        for floor in self.currentFloor:
            pygame.draw.rect(screen, self.color, pygame.rect.Rect(floor["xPosition"]*StartFloor.width, floor["yPosition"]*StartFloor.height, StartFloor.width, StartFloor.height))

    def moveUp(self):
        if self.win or self.lose: return
        if self.isStanding():
            currentFloor = self.currentFloor[0]
            self.currentFloor = [
                dict(xPosition = currentFloor["xPosition"], yPosition = currentFloor["yPosition"]-1),
                dict(xPosition = currentFloor["xPosition"], yPosition = currentFloor["yPosition"]-2)
            ]
        elif self.isLying():
            if self.isLyingHorizontal():
                self.currentFloor[0]["yPosition"] -= 1
                self.currentFloor[1]["yPosition"] -= 1
            elif self.isLyingVertical():
                yPositionMin = min(self.currentFloor[0]["yPosition"], self.currentFloor[1]["yPosition"])
                newFloor = dict(xPosition = self.currentFloor[0]["xPosition"], yPosition = yPositionMin - 1)
                self.currentFloor = [newFloor]
        self.checkBlockStatus()       

    def moveDown(self):
        if self.win or self.lose: return
        if self.isStanding():
            currentFloor = self.currentFloor[0]
            self.currentFloor = [
                dict(xPosition = currentFloor["xPosition"], yPosition = currentFloor["yPosition"]+1),
                dict(xPosition = currentFloor["xPosition"], yPosition = currentFloor["yPosition"]+2)
            ]
        elif self.isLying():
            if self.isLyingHorizontal():
                self.currentFloor[0]["yPosition"] += 1
                self.currentFloor[1]["yPosition"] += 1
            elif self.isLyingVertical():
                yPositionMax = max(self.currentFloor[0]["yPosition"], self.currentFloor[1]["yPosition"])
                newFloor = dict(xPosition = self.currentFloor[0]["xPosition"], yPosition = yPositionMax + 1)
                self.currentFloor = [newFloor]
        self.checkBlockStatus()
        
    def moveLeft(self):
        if self.win or self.lose: return
        if self.isStanding():
            currentFloor = self.currentFloor[0]
            self.currentFloor = [
                dict(xPosition = currentFloor["xPosition"]-1, yPosition = currentFloor["yPosition"]),
                dict(xPosition = currentFloor["xPosition"]-2, yPosition = currentFloor["yPosition"])
            ]
        elif self.isLying():
            if self.isLyingVertical():
                self.currentFloor[0]["xPosition"] -= 1
                self.currentFloor[1]["xPosition"] -= 1
            elif self.isLyingHorizontal():
                xPositionMin = min(self.currentFloor[0]["xPosition"], self.currentFloor[1]["xPosition"])
                newFloor = dict(xPosition = xPositionMin - 1, yPosition = self.currentFloor[0]["yPosition"])
                self.currentFloor = [newFloor]
        self.checkBlockStatus()
        
    def moveRight(self):
        if self.win or self.lose: return;
        if self.isStanding():
            currentFloor = self.currentFloor[0]
            self.currentFloor = [
                dict(xPosition = currentFloor["xPosition"]+1, yPosition = currentFloor["yPosition"]),
                dict(xPosition = currentFloor["xPosition"]+2, yPosition = currentFloor["yPosition"])
            ]
        elif self.isLying():
            if self.isLyingVertical():
                self.currentFloor[0]["xPosition"] += 1
                self.currentFloor[1]["xPosition"] += 1
            elif self.isLyingHorizontal():
                xPositionMax = max(self.currentFloor[0]["xPosition"], self.currentFloor[1]["xPosition"])
                newFloor = dict(xPosition = xPositionMax + 1, yPosition = self.currentFloor[0]["yPosition"])
                self.currentFloor = [newFloor]
        self.checkBlockStatus()
        
    def checkBlockStatus(self):
        for floor in self.currentFloor:
            xPosition = floor["xPosition"]
            yPosition = floor["yPosition"]
            if xPosition < 0 or yPosition < 0 or xPosition >= self.map.mapWidth/Floor.width or yPosition >= self.map.mapHeight/Floor.height:
                self.gameLose()
                return
            if isinstance(self.map.floors[yPosition][xPosition], NoneFloor):
                self.gameLose()
                return
            if isinstance(self.map.floors[yPosition][xPosition], WeakFloor) and self.isStanding():
                self.gameLose()
                return
            if isinstance(self.map.floors[yPosition][xPosition], HoleFloor) and self.isStanding():
                self.gameWin()
                return
            # if isinstance(self.map.floors[yPosition][xPosition], CircleToggleFloor):
            #     self.map.floors[yPosition][xPosition].toggle()

    def gameWin(self):
        self.win = True
        print("You win")

    def gameLose(self):
        self.lose = True
        print("You lose")

    # def showMap(self):
    #     for row in self.map.floors:
    #         for floor in row:
    #             if isinstance(floor, CircleToggleFloor):
    #                 print(floor)

