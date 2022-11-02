# class StartFloor thể hiện floor đầu tiên của khổi gạch khi bắt đầu trò chơi


from Floor.Floor import Floor
import pygame

class StartFloor(Floor):

    def __init__(self, xPosition, yPosition) -> None:
        super().__init__(xPosition, yPosition)

    def render(self, screen):
        super().render(screen)
        message = "START"
        font = pygame.font.Font('freesansbold.ttf', 14)
        text = font.render(message, True, (6, 82, 221))
        screen.blit(text, ((self.xPosition+0.05)*self.width, (self.yPosition+0.4)*self.height))
