# class Hole thể hiện mục tiêu cần đi đến

from Floor.Floor import Floor
import pygame

class HoleFloor(Floor):

    color = pygame.Color(0,0,0) # black

    def __init__(self, xPosition, yPosition) -> None:
        super().__init__(xPosition, yPosition)