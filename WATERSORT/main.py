import os, os.path
from input import *
from output import *
from depthFirstSearch import *
from aStar import *

dir_path = os.path.dirname(os.path.realpath(__file__))
DIR = dir_path + '/Input'
numOfInput = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

prompt = "Select Algorithm\n 1. A*\n 2. Depth first search\nYour select = "
algorithm = input(prompt)

testcase = input("\nSelect testcase 1 - 40: ")
testcase = int(testcase)
initState = readInput(testcase)

if algorithm == '1':    
    result = aStarSearch(initState)    
    if(result):
        aStarStep = printPathColor(result)
    else:
        print('No solution found!')
        
elif algorithm == '2':
    result = depthFirstSearch(initState) 
    if(result):
        dfsStep = printPathColor(result)
    else:
        print('No solution found!') 
  
else:
    running = False
        






