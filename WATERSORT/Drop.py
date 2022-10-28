class Drop:
    def __init__(self,color,size=1):
        self.color = ''
        self.size = 0
        self.setColor(color)
        self.setSize(size)
    
    def getColor(self):
        """get color of Drop"""
        return self.color
    
    def getSize(self):
        """get size of Drop"""
        return self.size
    
    def setColor(self,color):
        self.color = color
    
    def setSize(self,size = 1):
        if(size <= 0):
            raise Exception("size of Drop must be larger than 0")
        self.size = size
        
        
