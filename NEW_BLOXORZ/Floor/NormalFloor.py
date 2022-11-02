# class NormalFloor đại diện cho một lát gạch bình thường trên bản đồ
from Floor.Floor import Floor
import pygame

class NormalFloor(Floor):
    
    color = pygame.Color(178, 190, 195)

    def __init__(self, xPosition, yPosition):
        super().__init__(xPosition, yPosition)
    
