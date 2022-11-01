from ds import *

def generatePossibleMoves(states): 
    return []
    
def depthFirstSearch(initState):
    states = [initState]
    while states: 
        currentState = states.pop()
        if (checkGameStatus(currentState) == WIN): return
        states.append(generatePossibleMoves)
        
        
    