def printState(state):
    glasses = state.glasses
    for glass in glasses:
        while (len(glass.colors) < glass.capacity):
            glass.colors.append("_")
        
        print("\t".join([str(color) for color in glass.colors]))

        
def printPath(state):
    if (state.parent):
        printPath(state.parent)
    printState(state)
    print("------------------------------")