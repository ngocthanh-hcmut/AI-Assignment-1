import os, os.path
from input import *
from output import *
from depthFirstSearch import *

initState = readInput(1)

# s1 = copy.deepcopy(initState)
# s1.block.moveRight()
# s1.block.moveRight()
# # s1.block.moveDown()

# s2 = copy.deepcopy(initState)
# s2.block.moveDown()
# s2.block.moveRight()
# s2.block.moveRight()
# s2.block.moveRight()
# s2.block.moveUp()


# print(s1 == s2)

depthFirstSearch(initState)

for i in visited:
    printState(i)