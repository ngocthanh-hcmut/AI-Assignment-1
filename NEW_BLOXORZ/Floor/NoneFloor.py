# class NoneFloor đại diện cho khoản trống trên bảng đồ


from Floor.Floor import Floor
import pygame

class NoneFloor(Floor):

    color = pygame.Color(0, 0, 0)

    def __init__(self, xPosition, yPosition) -> None:
        super().__init__(xPosition, yPosition)
