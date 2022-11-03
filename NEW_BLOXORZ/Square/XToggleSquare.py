
import pygame
from Square.NoneSquare import NoneSquare
from Square.NormalSquare import NormalSquare
from Square.Square import Square

class XToggleSquare(Square):

    XColor = pygame.Color(255,255,255)

    def __init__(self, xPosition, yPosition) -> None:
        super().__init__(xPosition, yPosition)
        self.canClose = False
        self.canOpen = False
        self.targets = [] # target = [Square, Square]

    def render(self, screen):
        super().render(screen)
        message = "X"
        font = pygame.font.Font('freesansbold.ttf', 40)
        text = font.render(message, True, self.XColor)
        screen.blit(text, ((self.xPosition+0.15)*self.width, (self.yPosition+0.2)*self.height))
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