from queue import PriorityQueue

def aStarSearch(start, goal, h):
    Openlst = PriorityQueue()
    Closedlst = list()
    
    start.parent = None
    start.gScore = 0
    start.fScore = h(start)
    
    
    