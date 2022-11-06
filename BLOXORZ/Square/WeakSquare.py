import pygame
from Square.Square import Square

# class WeakFloor đại diện cho lát gạch yếu của trò chơi
class WeakSquare(Square):
    
    color = pygame.Color(255, 195, 18)

    def __init__(self, xPosition, yPosition) -> None:
        super().__init__(xPosition, yPosition)
