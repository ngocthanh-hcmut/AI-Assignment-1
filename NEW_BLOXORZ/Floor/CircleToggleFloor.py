from array import array
from Floor.Floor import Floor
import pygame
from Floor.NoneFloor import NoneFloor
from Floor.NormalFloor import NormalFloor

# class CircleToggleFloor đại diện cho phần nền có dấu hình tròn
class CircleToggleFloor(Floor):

    CircleColor = pygame.Color(255, 255, 255)

    def __init__(self, xPosition, yPosition, map, canOpen:bool = False, canClose:bool = False, target: array = []) -> None:
        super().__init__(xPosition, yPosition)
        self.canOpen = canOpen
        self.canClose = canClose
        self.targets = target # target = [Floor,Floor]
        self.map = map

    def render(self, screen):
        super().render(screen)
        center = dict(x = self.xPosition*self.width + self.width/2, y = self.yPosition*self.height + self.height/2)
        radius = self.width / 3
        pygame.draw.circle(screen, self.CircleColor, (center["x"], center["y"]), radius, 5)

    def isOpened(self):
        floor = self.targets[0]
        if isinstance(floor, NormalFloor):
            return True
        else: 
            return False

    def isClosed(self):
        floor = self.targets[0]
        if isinstance(floor, NoneFloor):
            return True
        else:
            return False

    def open(self):
        if not self.canOpen: return
        for floor in self.targets:
            xPosition = floor.xPosition
            yPosition = floor.yPosition
            self.map.floors[yPosition][xPosition] = NormalFloor(xPosition, yPosition)

    def close(self):
        if not self.canClose: return
        for floor in self.targets:
            xPosition = floor.xPosition
            yPosition = floor.yPosition
            self.map.floors[yPosition][xPosition] = NoneFloor(xPosition, yPosition)

    def toggle(self):
        if self.isOpened():
            self.close()
        if self.isClosed():
            self.open()

    def setProperty(self, canOpen, canClose, target):
        self.canOpen = canOpen
        self.canClose = canClose
        self.target = target

    def __str__(self) -> str:
        string = ''
        for floor in self.target:
            string += "(" + str(floor.xPosition) + "," + str(floor.yPosition) + ")"
        return string