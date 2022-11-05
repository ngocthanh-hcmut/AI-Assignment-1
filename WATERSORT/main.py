import os, os.path
from input import *
from output import *
from depthFirstSearch import *
from aStar import *

dir_path = os.path.dirname(os.path.realpath(__file__))
DIR = dir_path + '/Input'
numOfInput = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
prompt = "Choose the output you want to: \n \t Press 1: Export to txt file in folder Output\n \t Press 2: Export to terminal\n \t Press any key else to quit.\n Your choice:"
running = True

choice = input(prompt)
if choice == '1':
    
    for inputNum in range(1, numOfInput + 1):
        print('\n ===============================================','\n\nCase-{}:\n'.format(str(inputNum)))
        depthFile = open('Output/Depth/{}.txt'.format(str(inputNum)),'w')
        aStartFile = open('Output/AStart/{}.txt'.format(str(inputNum)),'w')
        
        initState = readInput(inputNum)
        AStartResult = aStarSearch(initState)
        depthResult = depthFirstSearch(initState)
        depthStep = 0
        if(depthResult):
            depthStep = printPath(depthResult,depthFile)
        AStartStep = 0
        if(AStartResult):
            AStartStep = printPath(AStartResult,aStartFile)
        print('A* Search Step: ',AStartStep)
        print('depth-first Search Step: ',depthStep)
    
elif choice == '2':
    inp = input("\nthe number of input is 1 to 40. Enter: ")
    inp = int(inp)
    searchMethod = input("press 1 A* search\n press 2 depth-first search:")
    searchMethod = int(searchMethod)
    initState = readInput(inp)
    result = None
    if(searchMethod == 1):
        result = aStarSearch(initState)
    else:
        result = depthFirstSearch(initState)
    
    if(result):
        AStartStep = printPathColor(result)
        
    
    
    
    
else:
    running = False
        






