

# class XToggleFloor đại diện cho phần nền có dấu X
from Floor.Floor import Floor
import pygame

class XToggleFloor(Floor):

    XColor = pygame.Color(255,255,255)

    def __init__(self, xPosition, yPosition) -> None:
        super().__init__(xPosition, yPosition)

    def render(self, screen):
        super().render(screen)
        message = "X"
        font = pygame.font.Font('freesansbold.ttf', 40)
        text = font.render(message, True, self.XColor)
        screen.blit(text, ((self.xPosition+0.15)*self.width, (self.yPosition+0.2)*self.height))