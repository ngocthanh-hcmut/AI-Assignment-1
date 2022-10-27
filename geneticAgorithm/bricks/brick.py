import pygame
import globalVariable as const

class Brick:
    size = const.BRICK_SIZE
    color = const.NORMAL_BRICK_COLOR
    borderColor = const.BRICK_EDGE_COLOR

    def __init__(self, positionX, positionY, screen):
        self.positionX = positionX
        self.positionY = positionY
        self.xPos = self.size * positionX
        self.yPos = self.size * positionY
        self.render(screen)

    def render(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.xPos, self.yPos, self.size, self.size))
        pygame.draw.rect(screen, self.borderColor, pygame.Rect(self.xPos, self.yPos, self.size, self.size), 1)
