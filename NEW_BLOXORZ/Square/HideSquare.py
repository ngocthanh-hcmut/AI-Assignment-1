
import pygame
from Square.NoneSquare import NoneSquare

class HideSquare(NoneSquare):

    def __init__(self, xPosition, yPosition, enable) -> None:
        super().__init__(xPosition, yPosition)
        self.enabled = enable

    def render(self, screen):
        # print("rendering")
        if self.enabled:
            self.color = pygame.Color(47, 53, 66)
        else:
            self.color = pygame.Color(0, 0, 0)
        # vẽ cái nền
        pygame.draw.rect(screen, self.color, pygame.rect.Rect(self.xPosition*self.width, self.yPosition*self.height, self.width, self.height))
        # vẽ cái viền
        pygame.draw.rect(screen, self.borderColor, pygame.rect.Rect(self.xPosition*self.width, self.yPosition*self.height,self.width, self.height), 1)
        pygame.display.update(pygame.rect.Rect(self.xPosition*self.width, self.yPosition*self.height, self.width, self.height))
    