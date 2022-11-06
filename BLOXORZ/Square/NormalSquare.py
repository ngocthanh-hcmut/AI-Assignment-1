# class NormalFloor đại diện cho một lát gạch bình thường trên bản đồ
import pygame
from Square.Square import Square

class NormalSquare(Square):
    
    color = pygame.Color(178, 190, 195)

    def __init__(self, xPosition, yPosition):
        super().__init__(xPosition, yPosition)
    
