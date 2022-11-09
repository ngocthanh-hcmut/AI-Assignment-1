from time import sleep
from Floor import *
from State import *
from Block.Block import *

# ------------------------------------------
sharedFloor = Floor(2)

# initial the pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((sharedFloor.floorWidth, sharedFloor.floorHeight), pygame.SHOWN)
#title and caption
pygame.display.set_caption("Bloxorz")
icon = pygame.image.load('image/icon.png')
pygame.display.set_icon(icon)
screen.fill(pygame.Color(0, 0, 0))
# ---------------------------------------------------

floor = Floor(2)
block = Block(floor.startSquare.xPosition, floor.startSquare.yPosition)
state1 = State(block, floor)
state1.moveUp()
state1.checkGameStatus(screen)
state1.renderFloor(screen)
state1.renderBlock(screen)
sleep(2)
state1.moveRight()
state1.checkGameStatus(screen)
state1.renderFloor(screen)
state1.renderBlock(screen)
sleep(3)

state2 = copy.deepcopy(state1)
state2.moveRight()
# state2.checkGameStatus(screen)
state2.renderFloor(screen)
state2.renderBlock(screen)
sleep(3)

print(state1 == state2)

# print([dict{}])