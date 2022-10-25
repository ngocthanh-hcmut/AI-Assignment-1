from collections import deque

# stack data structure
class Stack:
    def __init__(self,list=[]):
        self.stack = deque(list)
    
    def __call__(self):
        """return stack List"""        
        return self.stack
    
    def getStackList(self):
        """return stack List"""
        return self.stack

    def push(self,elem):
        """Push to stack"""
        self.stack.appendleft(elem)
    
    def pop(self):
        """Pop out of stack"""
        if(self.isEmpty()):
            return None
        else:
            return self.stack.popleft()
    
    def top(self):
        if(self.isEmpty()):
            return None
        else:
            return self.stack[0]

    def isEmpty(self):
        """get the first element"""
        if(self.length() >0):
            return False
        else:
            return True
        
    def getItem(self,index):
        len = self.length()
        if(len == 0 or index >=len):
            return None
        else:
            return self.stack[index]
    
    def length(self):
        """caculate the length of stack"""
        return len(self.stack)
    
    
# Color drop: giọi màu
class Drop:
    def __init__(self,color,length=1):
        self.dropColor={'col':color ,'len':length}
    
    def __call__(self):
        """Return Drop Dictionary"""
        return self.dropColor
    
    def getDrop(self):
        """Return Drop Dictionary"""
        return self.dropColor
    
    def changeColor(self,color):
        """change color of Drop"""
        self.dropColor['col']=color
    
    def changeLength(self,length):
        """change Length of the Drop"""
        self.dropColor['len'] = length
    
    def color(self):
        """get color of Drop"""
        return self.dropColor['col']
    def lengthColor(self):
        """get Length of the Drop"""
        return self.dropColor['len']
  


# Glass contain color
class Glass:
    def __init__(self,name='',stackColor = Stack(),capacity=2):
        self.name=name
        self.capacity =0
        self.isDone = False
        self.isFull=False
        self.levelOfColor=0
        self.tube = stackColor
        
        # init capacity
        if(capacity < 2):
            self.capacity =2
        else:
            self.capacity=capacity
        self.__call__()
        self.initOperate()
        self.__call__()

        
    
    def __call__(self):
        print(
            '{',
                '\t','name:',self.name,
                '\n\t','capacity:', self.capacity,
                '\n\t','Done:',self.isDone,
                '\n\t','Full:',self.isFull,
                '\n\t','Level:',self.levelOfColor,
                '\n\t','tube: {'
        );
        for color in self.tube():
            print('\t     ',color(),',')
        print('\t}\n}')
        

    def initOperate(self):
        # empty stack.
        numOfCol = self.numOfColor()
        if(numOfCol == 0):
            self.isDone=True
            return
        # stack with 1 color:
        elif(numOfCol ==1 ):
            self.levelOfColor = self.tube.getItem(0).lengthColor()
            if(self.levelOfColor > self.capacity):
                raise Exception("Capacity does not enough space")
            elif (self.levelOfColor == self.capacity):
                self.isDone=True
                self.isFull=True
            else:
                self.isDone=False
                self.isFull=False
            return
        # stack with many colors.
        else:
            # caculate the level
            theLevel = 0
            for color in self.tube.getStackList():
                theLevel += color.lengthColor()
            self.levelOfColor = theLevel
            if(self.levelOfColor > self.capacity):
                raise Exception("Capacity does not enough space")
            elif (self.levelOfColor == self.capacity):
                self.isFull=True
                self.isDone=self.isTheSameColor()
            else:
                self.isDone=False
                self.isFull=False                
            
    
    def isTheSameColor(self):
        """check whether all the color in glass is the same color.
        If no color or one color => True
        If all the same color => true
        else => false
        Returns:Bool            
        """
        theSame=True
        theNumber = self.numOfColor()      
        if(theNumber ==0 or theNumber ==1):
            return theSame
        else:
            for i in range(0,theNumber-1):
                if(self.tube.getStackList()[i].color() !=  self.tube.getStackList()[i+1].color()):
                    return False
            return theSame
            
            
    def numOfColor(self):
        """Number of color that Glass contain"""
        return self.tube.length()
        
        
        
        
        
        
        
        
        
        
        
d1=Drop('B',2)
d2=Drop('B',3)
d3=Drop('G',3)
s1 = Stack([d1,d2,d3])
s1=Stack()
s1=Stack([d1,d2])
g1 = Glass('ahihi',s1,5)
# print(g1.isTheSameColor())

