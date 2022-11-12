import os, os.path
from input import *
from output import *
from depthFirstSearch import *

dir_path = os.path.dirname(os.path.realpath(__file__))
DIR = dir_path + '/Input'
numOfInput = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

print("You are using Depth First Search to solve BLOXORZ")
print("Available levels: 1,2,3,4,5,6,7,11,12,13,14,18,19.")

testcase = input("\nPlease select a level: ")
initState = readInput(testcase)

import time

start = time.time()
print("Running...")
result = depthFirstSearch(initState) 
if (result):
    print("Here is my solution:")
    printPath(result)

else:
    print('No solution found!') 
end = time.time()

print("Running time =", end - start)
  
        