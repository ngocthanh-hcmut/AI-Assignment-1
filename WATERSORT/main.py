from input import *
from output import *
from depthFirstSearch import *
from aStar import *

initState = readInput(24)
depthResult = depthFirstSearch(initState)
# AStartResult = aStarSearch(initState)
print(depthResult)

# # printState(initState)
# i = 0
# i = printPath(depthResult,i)
# j = 0
# j = printPath(AStartResult,j)
# print('dept: ',i)
# print('A*: ',j)


# for k in range(1, 41):
#     print('\n',k,' ===============================================')
#     initState = readInput(k)
#     AStartResult = aStarSearch(initState)
#     depthResult = depthFirstSearch(initState)
#     i = 0
#     i = printPath(depthResult,i)
#     j = 0
#     j = printPath(AStartResult,j)
#     print('dept: ',i)
#     print('A*: ',j)
