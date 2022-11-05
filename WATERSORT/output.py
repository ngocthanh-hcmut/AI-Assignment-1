
# Import required module
import queue
from colored import fg

def printState(state,  step=0, fileName = None):
    glasses = state.glasses
    for glass in glasses:
        while (len(glass.colors) < glass.capacity):
            glass.colors.append("_")
        
        # print("\t".join([str(color) for color in glass.colors]))
    vertical = []
    for i in range(0, glasses[0].capacity):
        vertical.insert(0, [glass.colors[i] for glass in glasses])
    
    print("step: "+ str(step) + ":\n",file = fileName)
    for colors in vertical:
        print("".join(["{:<10}" for i in range(0,len(colors))]).format(*colors),file = fileName)        
    print("------------------------------------------------------------------------------------------\n", file = fileName)
    
def matchColor(color):
    if color == '___':
        return fg('black')+color
    elif color == 'grey':
        return fg('light_gray')+color
    elif color ==  'orange':
        return fg('light_red')+color
    elif color == 'pink':
        return fg('light_magenta')+color
    else:
        return fg(color)+color

    
    
def printStateColors(state,  step=0):
    glasses = state.glasses
    for glass in glasses:
        while (len(glass.colors) < glass.capacity):
            glass.colors.append("___")
    
    vertical = []
    for i in range(0, glasses[0].capacity):
        vertical.insert(0, [glass.colors[i] for glass in glasses])
    
    print("Step "+ str(step) + ":\n")
    for colors in vertical:
        # print("".join(["{:<20}" for i in range(0,len(colors))]).format(*textWithColors(colors)))     
        print("\t".join([matchColor(color) for color in colors]))
        
    print(fg('black')+"------------------------------------------------------------------------------------------\n")
        

# Initialize LIFO Queue
StackRepo = queue.LifoQueue()
        
def tracePath(state):
    if state is None:
        return 
    else:
        StackRepo.put(state)
        tracePath(state.parent)


def printPath(goalState,fileName):
    
    # trace path and Store in Stack Repo
    tracePath(goalState)
    # print out the path
    step = 0
    while not StackRepo.empty():
        state = StackRepo.get()
        printState(state, step, fileName)
        step += 1
    return step

def printPathColor(goalState):
    # trace path and Store in Stack Repo
    tracePath(goalState)
    # print out the path
    step = 0
    while not StackRepo.empty():
        state = StackRepo.get()
        printStateColors(state, step)
        step += 1
    return step    
    