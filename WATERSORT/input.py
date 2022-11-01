from ds import * 

def readInput():
    input = open("Input/1.txt", "r").readlines()
    
    for i in range(len(input)):
        input[i] = input[i].split(" ")
    
    capacity = len(input[0])
    
    for i in range(len(input)):
        input[i][:] = (value for value in input[i] if (value != "_" and value != "_\n"))
        
    glasses = []
    for glass in input:
        glasses.append(Glass(capacity, glass))
    
    return State(glasses)
        