def printState(state):
    glasses = state.glasses
    for glass in glasses:
        while (len(glass.colors) < glass.capacity):
            glass.colors.append("_")
        
        # print("\t".join([str(color) for color in glass.colors]))
    vertical = []
    for i in range(0, glasses[0].capacity):
        vertical.insert(0, [glass.colors[i] for glass in glasses])
        
    for colors in vertical:
        print("\t".join([str(color) for color in colors]))

        
def printPath(state):
    if (state.parent):
        printPath(state.parent)
    printState(state)
    print("--------------------------------------------------------")