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
from breadthFirstSearch import breadthFirstSearch as bfs

print("Input number level you want to play:")
level = int(input())

print("Select mode of the game:")
print("[1] Testing")
print("[2] I want to use genetic agorithm.")
print("[3] Play.")
print("[4] Bfs.")
print("Your choice: ")
gameMode = int(input())
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


def play():
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
                    state.clearAndRender(screen, oldSquares, True)
                    state.checkGameStatus(screen)
        
        if state.status == "win" or state.status == "lose":
            running = False

def geneticAgorithm(level, screen):
    agorithm = GeneticAgorithm(level, sharedFloor)
    thread = ReturnValueThread(target=agorithm.execute, args=(None, ))
    thread.start()
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
                    # agorithm.showSolution(screen, level)
                    # running = False


# state = bfs(level, screen)
def breadthFirstSearch(state):
    if state.parent:
        breadthFirstSearch(state.parent)
    state.renderFloor(screen)
    state.renderBlock(screen)
    # floor = Floor(level)
    # block = Block(floor.startSquare.xPosition, floor.startSquare.yPosition)
    # state = State(block, floor)
    # state.renderFloor(screen)
    # state.renderBlock(screen)
    next = False
    while not next:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                next = True
            if event.type == pygame.KEYDOWN:
                next = True

def test(level, screen):
    agorithm = GeneticAgorithm(level, sharedFloor)
    thread = ReturnValueThread(target=agorithm.execute, args=(None, ))
    thread.start()
    thread.join()
    print("finding solution")
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

if gameMode == 1:
    test(level, screen)
if gameMode == 2:
    geneticAgorithm(level, screen)
if gameMode == 3:
    play()
if gameMode == 4:
    breadthFirstSearch(state)