# class Floor đại diện cho một lát gạch trên bản đồ
import pygame

class Square:

    width = 50
    height = 50
    color = pygame.Color(178, 190, 195)
    borderColor = pygame.Color(0,0,0)

    def __init__(self, xPosition, yPosition) -> None:
        self.xPosition = xPosition
        self.yPosition = yPosition

    def __eq__(self, other):
        return self.xPosition == other.xPosition and self.yPosition == other.yPosition
        
    def render(self, screen):
        # vẽ cái nền
        pygame.draw.rect(screen, self.color, pygame.rect.Rect(self.xPosition*self.width, self.yPosition*self.height, self.width, self.height))
        # vẽ cái viền
        pygame.draw.rect(screen, self.borderColor, pygame.rect.Rect(self.xPosition*self.width, self.yPosition*self.height,self.width, self.height), 1)
        pygame.display.update(pygame.rect.Rect(self.xPosition*self.width, self.yPosition*self.height, self.width, self.height))
    