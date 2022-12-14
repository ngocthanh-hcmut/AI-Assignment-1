import copy
import math
from queue import PriorityQueue


class Glass:
    
    def __init__(self, capacity, colors):
        self.capacity = capacity
        self.colors = colors
    
    def __lt__(self, other):
        return self.colors < other.colors
        
    def __eq__(self, other):
        return self.colors == other.colors
        
    def isFull(self):
        return (len(self.colors) == self.capacity)
    
    def isEmpty(self):
        return (len(self.colors) == 0)
    
    def isSameColor(self):
        if self.isEmpty(): return True
        
        firstColor = self.colors[0]
        for i in range(1, len(self.colors)) :
            if (firstColor != self.colors[i]):
                return False;
            
        return True
    
    def isComplete(self):
        return (self.isFull() and self.isSameColor()) or self.isEmpty()
    
    def popColor(self):
        return self.colors.pop() if not self.isEmpty() else None
    
    def topColor(self):
        return self.colors[-1] if not self.isEmpty() else None
    
    def appendColor(self, color):
        self.colors.append(color)

def canBePoured(source, destination):
    if (source.isEmpty() or
        destination.isFull() or
        source.topColor() != destination.topColor() and not destination.isEmpty()):

        return False
    
    return True

def pourWater(source, destination):
    if not canBePoured(source, destination):
        return False
    
    while canBePoured(source, destination):
        color = source.popColor()
        destination.appendColor(color)
    
    return True

def getHScore(glass):
    lenColors = len(glass.colors)
    if (lenColors == 0):
        return -1
    elif (lenColors == 1):
        return 0
    score = 0
    for i in range(0,lenColors - 1):
        if glass.colors[i] == glass.colors[i+1]:
            score -= (glass.capacity - i)
        else:
            score += (glass.capacity - i)
    return score


    

class State:
    
    def __init__(self, glasses, parent = None):
        self.glasses = glasses
        self.parent = parent
    
    def __eq__(self, other):
        return (self.glasses == sorted(other.glasses))
        
    def isLevelComplete(self):
        for glass in self.glasses:
            if not glass.isComplete():
                return False            
        return True
    
    def generateChildren(self):
        children = []
        
        for i in range(0, len(self.glasses) - 1):
            for j in range(i + 1, len(self.glasses)):                
                source = self.glasses[i]
                destination = self.glasses[j]                
                if canBePoured(source, destination):                    
                    newState = copy.deepcopy(self)
                    pourWater(newState.glasses[i], newState.glasses[j])
                    newState.parent = self
                    children.append(newState)
                    
                source = self.glasses[j]
                destination = self.glasses[i]                
                if canBePoured(source, destination):
                    newState = copy.deepcopy(self)
                    pourWater(newState.glasses[j], newState.glasses[i])
                    newState.parent = self
                    children.append(newState) 
                    
        return children
    

class heurState(State):
    def __init__(self, glasses):
        super().__init__(glasses,None)
        self.gScore = math.inf
        self.hScore = self.heuristicEvaluate()
        self.fScore = math.inf
        
    def heuristicEvaluate(self):
        sum = 0
        numOfGlasses = len(self.glasses)
        for i in  range(0, numOfGlasses):
            sum += getHScore(self.glasses[i])
        return sum
    
    def updateScores(self, ParentsgScore,disFromParent=0):
        self.gScore = ParentsgScore + disFromParent
        self.hScore = self.heuristicEvaluate()
        self.fScore = self.gScore + self.hScore
            
            
    
    def __lt__(self, other):
        return self.fScore < other.fScore
    
    def __eq__(self, other):
        tmpSelfSortedGlass = sorted(self.glasses)
        tmpOtherSortedGlass = sorted(other.glasses)
        return tmpSelfSortedGlass == tmpOtherSortedGlass
    
    def __ne__(self,other):
        return not self.__eq__(other)
    
    def generateChildren(self):
        children = []
        
        for i in range(0, len(self.glasses) - 1):
            for j in range(i + 1, len(self.glasses)):                
                source = self.glasses[i]
                destination = self.glasses[j]                
                if canBePoured(source, destination):                    
                    newState = copy.deepcopy(self)
                    pourWater(newState.glasses[i], newState.glasses[j])
                    newState.parent = self
                    # newState.glasses.sort()
                    newState.updateScores(math.inf,1)
                    children.append(newState)
                    
                source = self.glasses[j]
                destination = self.glasses[i]                
                if canBePoured(source, destination):
                    newState = copy.deepcopy(self)
                    pourWater(newState.glasses[j], newState.glasses[i])
                    newState.parent = self
                    # newState.glasses.sort()
                    newState.updateScores(math.inf,1)
                    children.append(newState) 
                    
        return children
        

class OpenQueue:
    def __init__(self):
        self.queue = PriorityQueue()
    
    def empty(self):
        return self.queue.empty()
    
    def put(self, state):
        self.queue.put(state)
    
    def get(self):
        return self.queue.get()
    
    def contains(self,state):
        
        return state in self.queue.queue
            
    
        

            
        
    
    
    
    
    
    
    
            
            