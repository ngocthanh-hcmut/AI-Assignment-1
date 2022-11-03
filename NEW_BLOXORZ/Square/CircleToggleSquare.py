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
        pygame.display.update(pygame.rect.Rect(self.xPosition*Square.width, self.yPosition*Square.height, Square.width, Square.height))

    def isTargetOpened(self):
        return self.targets[0].enabled
        # return True if isinstance(self.targets[0], NormalSquare) else False

    def isTargetClosed(self):
        return not(self.targets[0].enabled)
        # return True if isinstance(self.targets[0], NoneSquare) else False

    def openTarget(self, screen = None):
        if not(self.canOpen): return
        # print("opening")
        for i in range(len(self.targets)):
            self.targets[i].enabled = not(self.targets[i].enabled)
            self.targets[i].render(screen)


    def closeTarget(self, screen = None):
        if not self.canClose: return
        # print("closing")
        for i in range(len(self.targets)):
            self.targets[i].enabled = not(self.targets[i].enabled)
            self.targets[i].render(screen)

            
    def toggle(self, screen = None):
        # print("toggle")
        if self.isTargetOpened():
            # print("is open")
            self.closeTarget(screen)
        elif self.isTargetClosed():
            # print("is close")
            self.openTarget(screen)
            

    def addTarget(self, target):
        self.targets.append(target)
    
    def setProperty(self, char):
        # # print("setting property: ", self.xPosition, ", ", self.yPosition)
        if char == "!":
            self.canOpen = True
            self.canClose = True
            # # print("can open can close")
        if char == "@":
            self.canOpen = True
            # # print("can open")
        if char == "#":
            self.canClose = True
            # # print("can close")
    
