# class Hole thể hiện mục tiêu cần đi đến
import pygame
from Square.Square import Square

class HoleSquare(Square):

    color = pygame.Color(0,0,0) # black

    def __init__(self, xPosition, yPosition) -> None:
        super().__init__(xPosition, yPosition)