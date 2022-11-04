import queue
from State import *
from Block.Block import *
from Floor import *

def breadthFirstSearch(level, screen):
    floor = Floor(level)
    block = Block(floor.startSquare.xPosition, floor.startSquare.yPosition)
    initState = State(block, floor)
    
    states = queue.Queue()
    states.put(initState)
    visited = []
    while states:
        currentState = states.get()
        visited.append(currentState)
        
        if currentState.checkGameStatus() == True and currentState.status == "win": 
            return currentState
        
        children = currentState.generateChildren()
        for child in children:
            if child not in visited:
                states.put(child)
                

    