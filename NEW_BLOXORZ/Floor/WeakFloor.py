from Floor.Floor import Floor
import pygame

# class WeakFloor đại diện cho lát gạch yếu của trò chơi
class WeakFloor(Floor):
    
    color = pygame.Color(255, 195, 18)

    def __init__(self, xPosition, yPosition) -> None:
        super().__init__(xPosition, yPosition)
