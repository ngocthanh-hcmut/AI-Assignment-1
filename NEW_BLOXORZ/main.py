###
# Đây là file trung tâm của chương trình
###
import pygame

from Block.Block import Block
from Floor import Floor
from State import State
from StateGenetic import StateGenetic

print("Input number level you want to play:")
level = int(input())

print("Select mode of the game:")
print("[1] I want to play by myself.")
print("[2] I want to use genetic agorithm.")
print("[3] Developing.")
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

def playByMySelf():
    block = Block(sharedFloor.startSquare.xPosition, sharedFloor.startSquare.yPosition)
    state = State(block, sharedFloor)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    state.moveUp()
                if event.key == pygame.K_DOWN:
                    state.moveDown()
                if event.key == pygame.K_LEFT:
                    state.moveLeft()
                if event.key == pygame.K_RIGHT:
                    state.moveRight()
        
        if state.status == "win" or state.status == "lose":
            running = False
        state.renderFloor(screen)
        state.renderBlock(screen)
        pygame.display.update()

def developing():
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

if gameMode == 1:
    playByMySelf()
if gameMode == 3:
    developing()