from input import *
from output import *
from depthFirstSearch import *
from aStar import *

# initState = readInput(24)
# depthResult = depthFirstSearch(initState)
# AStartResult = aStarSearch(initState)
# print(depthResult)

# # printState(initState)
# i = 0
# i = printPath(depthResult,i)
# j = 0
# j = printPath(AStartResult,j)
# print('dept: ',i)
# print('A*: ',j)
# for k in range(1, 41):
#     f = open('output/{}.txt'.format(str(k)),'w')
#     f.write("New Content")   

for k in range(1, 41):
    print('\n',k,' ===============================================')
    depthFile = open('Output/Depth/{}.txt'.format(str(k)),'w')
    aStartFile = open('Output/AStart/{}.txt'.format(str(k)),'w')
    
    initState = readInput(k)
    AStartResult = aStarSearch(initState)
    depthResult = depthFirstSearch(initState)
    i = 0
    if(depthResult):
        i = printPath(depthResult,depthFile)
    j = 0
    if(AStartResult):
        j = printPath(AStartResult,aStartFile)
    print('dept: ',i)
    print('A*: ',j)
