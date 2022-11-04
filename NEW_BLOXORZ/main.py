###
# Đây là file trung tâm của chương trình
###
import threading
from time import sleep
import pygame
from GeneticAgorithm import GeneticAgorithm

from Block.Block import Block
from Floor import Floor
from State import State
from StateGenetic import StateGenetic
from breadthFirstSearch import breadthFirstSearch as bfs

print("Input number level you want to play:")
level = int(input())

print("Select mode of the game:")
print("[2] I want to use genetic agorithm.")
print("[3] Developing.")
print("[4] Bfs.")
print("Your choice: ")
gameMode = int(input())
sharedFloor = Floor(level)

# initial the pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((sharedFloor.floorWidth, sharedFloor.floorHeight))
#title and caption
pygame.display.set_caption("Bloxorz")
icon = pygame.image.load('image/icon.png')
pygame.display.set_icon(icon)
screen.fill(pygame.Color(0, 0, 0))
sharedFloor.render(screen)

def playByMySelf():
    floor = Floor(level)
    block = Block(floor.startSquare.xPosition, floor.startSquare.yPosition)
    state = StateGenetic(block, floor)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    state.moveUp(state.floor)
                if event.key == pygame.K_DOWN:
                    state.moveDown(state.floor)
                if event.key == pygame.K_LEFT:
                    state.moveLeft(state.floor)
                if event.key == pygame.K_RIGHT:
                    state.moveRight(state.floor)
        
        if state.status == "win" or state.status == "lose":
            running = False
        state.renderFloor(screen)
        state.renderBlock(screen)
        pygame.display.update()

def developing():
    floor = Floor(level)
    block = Block(floor.startSquare.xPosition, floor.startSquare.yPosition)
    state = StateGenetic(block, floor)
    state.renderBlock(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                oldSquares = [dict(xPosition=a["xPosition"], yPosition=a["yPosition"]) for a in state.block.currentSquare]
                if event.key == pygame.K_UP:
                    state.moveUp()
                if event.key == pygame.K_DOWN:
                    state.moveDown()
                if event.key == pygame.K_LEFT:
                    state.moveLeft()
                if event.key == pygame.K_RIGHT:
                    state.moveRight()
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    state.render(screen, oldSquares)
                    state.checkGameStatus(screen)
        
        if state.status == "win" or state.status == "lose":
            running = False

def geneticAgorithm(level, screen):
    agorithm = GeneticAgorithm(level)
    thread = threading.Thread(target=agorithm.execute, args=(screen, ))
    thread.start()
    while not(agorithm.stopExecute):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                agorithm.stopExecute = True
        
        if not(thread.is_alive()) and not(agorithm.stopExecute):
            thread = threading.Thread(target=agorithm.execute, args=(screen,))
            thread.start()

state = bfs(level, screen)
def breadthFirstSearch(state):
    if state.parent:
        breadthFirstSearch(state.parent)
    state.renderFloor(screen)
    state.renderBlock(screen)
    
    
    # while not(state.parent == None):
        # state.renderFloor(screen)
        # state.renderBlock(screen)
        # state = state.parent
        # sleep(0.5)
    

if gameMode == 1:
    playByMySelf()
if gameMode == 2:
    geneticAgorithm(level, screen)
if gameMode == 3:
    developing()
if gameMode == 4:
    breadthFirstSearch(level, screen)