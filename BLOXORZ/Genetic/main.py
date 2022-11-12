###
# Đây là file trung tâm của chương trình
###
import threading
from ReturnValueThread import ReturnValueThread
from time import sleep
import pygame
from GeneticAgorithm import GeneticAgorithm

from Block.Block import Block
from Floor import Floor
from State import State
from StateGenetic import StateGenetic

print("Possible level: 1,2,3,4")
print("Input number level you want to solve:")
level = int(input())

sharedFloor = Floor(level)

# initial the pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((sharedFloor.floorWidth, sharedFloor.floorHeight), pygame.SHOWN)
#title and caption
pygame.display.set_caption("Bloxorz")
icon = pygame.image.load('Image/icon.png')
pygame.display.set_icon(icon)
screen.fill(pygame.Color(0, 0, 0))
sharedFloor.render(screen)


def run(level, screen):
    agorithm = GeneticAgorithm(level, sharedFloor)
    thread = ReturnValueThread(target=agorithm.execute, args=(None, ))
    thread.start()
    thread.join()
    print("finding solution... It may took a while...")
    while not(agorithm.stopExecute):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                agorithm.stopExecute = True
        
        if not(thread.is_alive()) and not(agorithm.stopExecute):
            thread = threading.Thread(target=agorithm.execute, args=(None,))
            thread.start()
            thread.join()
    
    print("press space bar to see solution")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("showing solution")
                    thread = threading.Thread(target=agorithm.showSolution, args=(screen, level))
                    thread.start()

run(level, screen)