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
        currentState = states.pop(0)
        visited.append(currentState)
        
        if currentState.checkGameStatus(screen) == True and currentState.status == "win":
            print("solution found") 
            return currentState
        
        children = currentState.generateChildren(screen)
        for child in children:
            # child.renderFloor(screen)
            # child.renderBlock(screen)
            # sleep(2)
            if child not in visited:
                states.append(child)
                

    