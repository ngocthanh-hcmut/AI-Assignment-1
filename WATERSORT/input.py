from ds import * 

def readInput(fileNum):
    input = open("Input/{}".format(str(fileNum)), "r").readlines()
    
    for i in range(len(input)):
        input[i] = input[i].split(" ")
    
    capacity = len(input[0])
    
    for i in range(len(input)):
        input[i][-1] = input[i][-1].strip()
    
    for i in range(len(input)):
        input[i][:] = (value for value in input[i] if value != "_")
        
    glasses = []
    for glass in input:
        glasses.append(Glass(capacity, glass))
    
    # return State(glasses)
    return heurState(glasses)
        