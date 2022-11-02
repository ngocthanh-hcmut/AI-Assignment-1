###
# Đây là file trung tâm của chương trình
###
import pygame

from Map import Map
from Block.Block import Block

print("Input number level you want to play:")
level = int(input())

print("Select mode of the game:")
print("[1] I want to play by myself.")
print("[2] I want to use genetic agorithm.")
print("Your choice: ")
gameMode = int(input())
map = Map(level)

# initial the pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((map.mapWidth, map.mapHeight))
#title and caption
pygame.display.set_caption("Bloxorz")
icon = pygame.image.load('image/icon.png')
pygame.display.set_icon(icon)
screen.fill(pygame.Color(0, 0, 0))

def playByMySelf(map):
    block = Block(map)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    block.moveUp()
                if event.key == pygame.K_DOWN:
                    block.moveDown()
                if event.key == pygame.K_LEFT:
                    block.moveLeft()
                if event.key == pygame.K_RIGHT:
                    block.moveRight()
        
        if block.win or block.lose:
            running = False
        map.render(screen)
        block.render(screen)
        pygame.display.update()


if gameMode == 1:
    playByMySelf(map)