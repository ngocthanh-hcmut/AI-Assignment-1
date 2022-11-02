import copy


class Glass:
    
    def __init__(self, capacity, colors):
        self.capacity = capacity
        self.colors = colors
    
    def __eq__(self, other):
        return self.colors == other.colors
        
    def isFull(self):
        return (len(self.colors) == self.capacity)
    
    def isEmpty(self):
        return (len(self.isEmpty) == 0)
    
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
        source.topColor() != destination.topColor()):
        
        return False
    
    return True

def pourWater(source, destination):
    if not canBePoured(source, destination):
        return False
    
    while (canBePoured(source, destination)):
        color = source.popColor()
        destination.appendColor(color)
    
    return True


class State:
    
    def __init__(self, glasses, parent = None):
        self.glasses = glasses
        self.parent = parent
    
    def __eq__(self, other):
        self.glasses
        other.glasses
        return (self.glasses == other.glasses)
        
    def isLevelComplete(self):
        for glass in self.glasses:
            if not glass.isComplete():
                return False            
        return True
    
    def getFScore(self):
        pass
    
    def generateChildren(self):
        children = []
        for i in range(0, len(self.glasses) - 1):
            for j in range(i+1, len(self.glasses)):
                source = self.glasses[i]
                destination = self.glasses[j]                
                if canBePoured(source, destination):
                    newState = copy.deepcopy(self)
                    pourWater(newState.glasses[i], newState.glasses[j])
                    newState.parent = self
                    children.append(newState)     
        return children
    
class heurState(State):
    def ___init__(self, glasses):
        super().__init__(glasses)
        self.gScore = 0
        self.fScore = self.heuristicEvaluate(glasses)
        
    def heuristicEvaluate(self, glasses):
        pass
    
        

            
        
    
    
    
    
    
    
    
            
            