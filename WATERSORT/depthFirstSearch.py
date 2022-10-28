import state

def generatePossibleMoves(State state): 
    return []
    
def depthFirstSearch(State initState):
    states = [initState]
    while states: 
        currentState = states.pop()
        if (checkGameStatus(currentState) == WIN): return
        states.append(generatePossibleMoves)
        
        
    