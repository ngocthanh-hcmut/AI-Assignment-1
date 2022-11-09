from time import sleep
from ds import *
from output import *

def depthFirstSearch(initState):
    states = [initState]
    visited = []
    
    count = 1
    while states:
        currentState = states.pop()
        temp = copy.deepcopy(currentState)
        visited.append(temp)
        # visited.append(currentState)
        
        if currentState.checkGameStatus():
            return currentState
        
        children = currentState.generateChildren()
        for child in children:
            if child not in visited:
                states.append(child)
        
        print(count)
        count += 1
        printState(currentState)
    
