from ds import *
from output import *
    
def depthFirstSearch(initState):
    states = [initState]
    visited = []
    while states:
        currentState = states.pop()
        visited.append(currentState)
        
        if currentState.isLevelComplete(): 
            return currentState
        
        children = currentState.generateChildren()
        for child in children:
            if child not in visited:
                states.append(child)
            
           
        
        
    