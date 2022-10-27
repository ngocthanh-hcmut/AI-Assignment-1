import globalVariable as const
import bricks.brick as br
import pygame

class DestinationBrick(br.Brick):
    
    def __init__(self, positionX, positionY, screen):
        br.Brick.__init__(self, positionX, positionY, screen)
        self.color = const.DESTINATION_BRICK_COLOR

    def render(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.xPos, self.yPos, self.size, self.size))
        pygame.draw.rect(screen, self.borderColor, pygame.Rect(self.xPos, self.yPos, self.size, self.size), 1)
        starImg = pygame.image.load("image/star.png")
        screen.blit(starImg, (self.xPos + 5, self.yPos + 5))