# class NoneFloor đại diện cho khoản trống trên bảng đồ


import pygame
from Square.Square import Square

class NoneSquare(Square):

    color = pygame.Color(0, 0, 0)

    def __init__(self, xPosition, yPosition) -> None:
        super().__init__(xPosition, yPosition)
