from collections import deque


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
        
    def removeItem(self,index):
        theNumber = self.length()
        if(index >=0):
            if(index>=theNumber):
                raise Exception("index out of range of index to remove")  
                return False
            else:
                del self.stack[index]
                return True
        else:
            if(index<(-1*theNumber)):
                raise Exception("index out of range of index to remove")    
            else:
                del self.stack[index]
                return True
                

        
    
    def length(self):
        """caculate the length of stack"""
        return len(self.stack)
    
    


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
        self.initOperate()
        
    
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
        
    def isEmpty(self):
        if(self.tube.isEmpty()):
            self.isDone=True
            self.isFull = False
            return True
        return False
        

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

            # combine 2 color the same color surrounding
            theNumber = self.numOfColor()
            index = 1
            while(index<theNumber):
                if(self.tube.getItem(index).color() == self.tube.getItem(index-1).color()):
                    lenghOfCol = self.tube.getItem(index-1).lengthColor()
                    lenghOfCol += self.tube.getItem(index).lengthColor()
                    self.tube.getItem(index).changeLength(lenghOfCol)
                    self.tube.removeItem(index-1)
                    theNumber-=1
                    # continue
                else:
                    index+=1      
            
    
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
        
    def fillingColor(self,fillerGlass):
        """filling this glass by color in fillerGlass"""
        if(fillerGlass.levelOfColor==0):
            return False
        elif(self.isFull):
            return False
        if(self.tube.top().color() != fillerGlass.tube.top().color()):
            return False
        
    
        
        
        
        
        
        
        

        
d1=Drop('Green',2)
d2=Drop('Red',3)
d3=Drop('Blue',3)
d4=Drop('Blue',1)
s1 = Stack([d1,d2,d3,d4])
g1 = Glass('ahihi',s1,10)
print(g1.fillingColor(g1))



# s1 = Stack([1,2,3,4,5])
# for i in range(0,s1.length()):
#     print(i,' - ',s1.getStackList()[i])
# s1.removeItem(0)
# print('\n')
# for i in range(0,s1.length()):
#     print(i,' - ',s1.getStackList()[i])    
# g1=Glass('ahihi',s1,10)
# print(s1())
# print("\n")
