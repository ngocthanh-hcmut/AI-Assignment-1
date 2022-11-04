from input import *
from output import *
from depthFirstSearch import *

initState = readInput()

resultState = depthFirstSearch(initState)

printPath(resultState)

