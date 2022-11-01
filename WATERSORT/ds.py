class Glass:
    
    def __init__(self, name, capacity, colors, size):
        self.name = name
        self.capacity = capacity
        self.colors = colors
        
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
        return self.isFull() and self.isSameColor()
    
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
    
    def __init__(self, glasses):
        self.glasses = glasses
        
    def isLevelComplete(self):
        for glass in self.glasses:
            if not glass.isComplete():
                return False
            
        return True
    
        

            
        
    
    
    
    
    
    
    
            
            