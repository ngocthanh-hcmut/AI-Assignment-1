
def printState(state, fileName, step):
    glasses = state.glasses
    for glass in glasses:
        while (len(glass.colors) < glass.capacity):
            glass.colors.append("_")
        
        # print("\t".join([str(color) for color in glass.colors]))
    vertical = []
    for i in range(0, glasses[0].capacity):
        vertical.insert(0, [glass.colors[i] for glass in glasses])
    
    print("step: "+ str(step) + "\n",file = fileName)
    for colors in vertical:
        print("".join(["{:<10}" for i in range(0,len(colors))]).format(*colors),file = fileName)        

        
def printPath(state,fileName,step = 0):
    next = step + 1
    if (state.parent):
        next = printPath(state.parent, fileName, step + 1)
    printState(state, fileName,step)
    print("------------------------------------------------------------------------------------------", file = fileName)
    return next