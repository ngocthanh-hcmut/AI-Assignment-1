import queue
from time import sleep
from State import *
from Block.Block import *
from Floor import *

def breadthFirstSearch(level, screen):
    floor = Floor(level)
    block = Block(floor.startSquare.xPosition, floor.startSquare.yPosition)
    initState = State(block, floor)
    
    states = [initState]
    visited = []
    while states:
        currentState = states.pop()
        visited.append(currentState)

        # currentState.renderFloor(screen)
        # currentState.renderBlock(screen)
        # sleep(1)
        
        if currentState.checkGameStatus(screen) == True and currentState.status == "win":
            print("solution found") 
            return currentState
        
        children = currentState.generateChildren(screen)
        for child in children:
            if child not in visited:
                states.append(child)
                

    