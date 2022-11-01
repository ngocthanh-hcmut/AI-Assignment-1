class Glass:
    
    def __init__(self, name, capacity, colors, size):
        self.name = name
        self.capacity = capacity
        self.colors = colors
        
    def isFull(self):
        return (len(self.colors) == self.capacity)
    
    def isEmpty(self):
        return self.colors
    
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
        return self.colors.pop() if self.colors else None
    
    def topColor(self):
        return self.colors[-1] if self.colors else None
    
    def appendColor(self, color):
        self.colors.append(color)
    
def pourWater(source, destination):
    while (source.topColor() == destination.topColor() and 
           source.topColor() != None and 
           not destination.isFull()):
        
        source.popColor()
        destination.appendColor(source.topColor())
    
    return True

class State:
    
    def __init__(self, glasses):
        self.glasses = glasses
        
    def isLevelComplete(self):
        for glass in self.glasses:
            if not glass.isComplete():
                return False
            
        return True
    
        

            
        
    
    
    
    
    
    
    
            
            