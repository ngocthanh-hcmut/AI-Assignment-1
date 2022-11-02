import pygame
from Square.NoneSquare import NoneSquare
from Square.NormalSquare import NormalSquare

from Square.Square import Square

# class CircleToggleFloor đại diện cho phần nền có dấu hình tròn
class CircleToggleSquare(Square):

    CircleColor = pygame.Color(255, 255, 255)

    def __init__(self, xPosition, yPosition) -> None:
        super().__init__(xPosition, yPosition)
        self.canOpen = False
        self.canClose = False
        self.targets = [] # target = [Square,Square]

    def render(self, screen):
        super().render(screen)
        center = dict(x = self.xPosition*self.width + self.width/2, y = self.yPosition*self.height + self.height/2)
        radius = self.width / 3
        pygame.draw.circle(screen, self.CircleColor, (center["x"], center["y"]), radius, 5)

    def isOpened(self):
        return True if isinstance(self.targets[0], NormalSquare) else False

    def isClosed(self):
        return True if isinstance(self.targets[0], NoneSquare) else False

    def open(self, floor):
        if not(self.canOpen): return
        # print("opening")
        for i in range(len(self.targets)):
            x = self.targets[i].xPosition
            y = self.targets[i].yPosition
            newSquare = NormalSquare(x, y)
            floor.squares[y][x] = newSquare
            self.targets[i] = newSquare

    def close(self, floor):
        if not self.canClose: return
        # print("closing")
        for i in range(len(self.targets)):
            x = self.targets[i].xPosition
            y = self.targets[i].yPosition
            newSquare = NoneSquare(x, y)
            floor.squares[y][x] = newSquare
            self.targets[i] = newSquare

    def toggle(self, floor):
        # print("target = ", self.targets[0].xPosition, ",", self.targets[0].yPosition, " - ",self.targets[1].xPosition, ",", self.targets[1].yPosition )
        if self.isOpened():
            # print("is opened")
            self.close(floor)
        elif self.isClosed():
            # print("is closed")
            self.open(floor)
            

    def addTarget(self, target):
        self.targets.append(target)
    
    def setProperty(self, char):
        if char == "!":
            self.canOpen = True
            self.canClose = True
        if char == "@":
            self.canOpen = True
        if char == "#":
            self.canClose = True
    
    def __str__(self) -> str:
        string = ''
        for square in self.targets:
            string += "(" + str(square.xPosition) + "," + str(square.yPosition) + ")"
        if self.canOpen:
            string += "  can open  "
        if self.canClose:
            string += "   can close   "
        return string