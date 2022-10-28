import logging
import threading
import pygame
import globalVariable as const
import map as m
import geneticAgorithm as ga

# initial the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))

#title and caption
pygame.display.set_caption("Bloxorz")
icon = pygame.image.load('image/icon.png')
pygame.display.set_icon(icon)
screen.fill(const.BACKGROUND_COLOR)
mapp = m.Map(screen)
agorithm = ga.GeneticAgorithm(mapp.inputMap)
generationCount = 0

thread = threading.Thread(target=agorithm.thrive, args=())
#game loop
thread.start()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if not(thread.is_alive()) and running:
        thread = threading.Thread(target=agorithm.thrive, args=())
        thread.start()
    
    mapp.render(screen)
    agorithm.updatePosition(screen)
    pygame.display.update()
