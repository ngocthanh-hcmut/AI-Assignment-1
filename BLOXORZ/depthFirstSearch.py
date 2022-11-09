from time import sleep
from ds import *
from output import *

visited = []
def depthFirstSearch(initState):
    states = [initState]
    

    while states:
    # for i in range(10):
        currentState = states.pop()
        visited.append(currentState)

        if currentState.checkGameStatus():
            return currentState
        
        children = currentState.generateChildren()
        for child in children:
            if child not in visited:
                states.append(child)
                

    
