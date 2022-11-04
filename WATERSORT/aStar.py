from ds import *

def aStarSearch(start):
    Openlst = OpenQueue()
    Closedlst = []
    
    start.parent = None
    start.gScore = 0
    start.fScore = start.heuristicEvaluate()
    
    Openlst.put(start)
    while not Openlst.empty():

        cur = Openlst.get()
        if cur.isLevelComplete():
            return cur
        Closedlst.append(cur)
        children = cur.generateChildren()
        for child in children:
            if child in Closedlst:
                continue
            tentative_gScore = cur.gScore + 1 # 1 meaning cost from cur to this child
            if tentative_gScore < child.gScore:
                child.parent = cur
                child.gScore = tentative_gScore
                child.fScore = tentative_gScore + child.heuristicEvaluate()
                if not Openlst.contains(child):
                    Openlst.put(child)                    

                    
    return False
            
        
        
    
    
    
    