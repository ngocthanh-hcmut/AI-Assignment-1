import os, os.path
from input import *
from output import *
from depthFirstSearch import *
from ds import *

initState = readInput(2)

states = [initState]
visited = []

while states:
# for i in range(200):
    currentState = states.pop()
    temp = copy.deepcopy(currentState)
    visited.append(temp)
    # visited.append(currentState)
    if currentState.checkGameStatus():
        printPath(currentState)
        print("found")
        break
    
    children = currentState.generateChildren()
    for child in children:
        if child not in visited:
            # print("not in")
            states.append(child)
        # else:
            # print("in")

    printState(currentState)




# print(links)
