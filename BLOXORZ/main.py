import os, os.path
from input import *
from output import *
from depthFirstSearch import *

dir_path = os.path.dirname(os.path.realpath(__file__))
DIR = dir_path + '/Input'
numOfInput = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

prompt = "Select Algorithm\n 1. Genetic\n 2. Depth first search\nYour select = "
algorithm = input(prompt)

testcase = input("\nSelect testcase 1 -> 33: ")
initState = readInput(testcase)

if algorithm == '1':    
    result = genetic(initState)    
    if (result):
        printPath(result)
    else:
        print('No solution found!')
        
elif algorithm == '2':
    result = depthFirstSearch(initState) 
    if (result):
        printPath(result)
    else:
        print('No solution found!') 
  
else:
    running = False
        