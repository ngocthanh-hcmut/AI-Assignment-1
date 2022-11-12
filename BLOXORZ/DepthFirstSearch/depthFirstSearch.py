from time import sleep
from ds import *
from output import *

def depthFirstSearch(initState):
    states = [initState]
    visited = []
    
    while states:
        currentState = states.pop()
        state = copy.deepcopy(currentState)
        visited.append(state)
        
        if currentState.checkGameStatus():
            return currentState
        
        children = currentState.generateChildren()
        for child in children:
            if child not in visited:
                states.append(child)
                
        printS(currentState)
        
    
