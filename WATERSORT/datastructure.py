from collections import deque


# Color drop: giọi màu
class Drop:
    def __init__(self,color,length=1):
        if(length <=0):
            raise Exception("length of Drop must be larger than 0")
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
        self.name=name              # the name of glass
        self.capacity =0            # the capacity of glass
        self.allTheSame = False     # the variable to show this glass is the same color
        self.isFull=False           # the variable to show this glass is Full
        self.levelOfColor=0         # the variable to show the height of color in this glass
        self.tube = stackColor      # store the stack contain all color.
        
        # init capacity
        if(capacity < 2):
            self.capacity =2
        else:
            self.capacity=capacity
        # self.__call__()
        self.initOperate()
        # self.__call__()
        
    
    def __call__(self):
        print(
            '{',
                '\t','name:',self.name,
                '\n\t','capacity:', self.capacity,
                '\n\t','TheSame:',self.allTheSame,
                '\n\t','Full:',self.isFull,
                '\n\t','Level:',self.levelOfColor,
                '\n\t','tube: {'
        );
        for color in self.tube():
            print('\t     ',color(),',')
        print('\t}\n}')
        
    def GlassIsFull(self):
        """Check where the glass is FUll"""
        theNumber = self.numOfColor()
        length=0
        for i in range(0,theNumber):
            length += self.tube.getItem(i).lengthColor()
        # print(length)
        if(length> self.capacity):
            raise Exception("Capacity does not enough space")
        elif(length == self.capacity):
            self.isFull = True
            self.levelOfColor = length
            return True
        else:
            self.isFull = False
            self.levelOfColor = length
            return False
        
    def isEmpty(self):
        """Check whethe the glass is empty"""
        if(self.tube.isEmpty()):
            self.allTheSame=True
            self.isFull = False
            self.levelOfColor = 0
            return True
        return False
        
    def initOperate(self):
        # empty stack.
        numOfCol = self.numOfColor()
        if(numOfCol == 0):
            self.allTheSame=True
            self.isFull = False
            return
        # stack with 1 color:
        elif(numOfCol == 1):
            self.levelOfColor = self.tube.getItem(0).lengthColor()
            if(self.levelOfColor > self.capacity):
                raise Exception("Capacity does not enough space")
            elif (self.levelOfColor == self.capacity):
                self.allTheSame=True
                self.isFull=True
            else:
                self.allTheSame=True
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
                self.allTheSame=self.isTheSameColor()
            else:
                self.isFull=False
                self.allTheSame=self.isTheSameColor()
            # self.__call__()

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
        theNumber = self.numOfColor()      
        if(theNumber ==0 or theNumber ==1):
            self.allTheSame =True
            return True
        else:
            for i in range(0,theNumber-1):
                if(self.tube.getStackList()[i].color() !=  self.tube.getStackList()[i+1].color()):
                    self.allTheSame =False                    
                    return False
            self.allTheSame =True
            return True
                    
    def numOfColor(self):
        """the number of colors that Glass is containing"""
        return self.tube.length()
        
    def fillingColor(self,fillerGlass):
        """filling this glass by color in fillerGlass. Return true if filling process succees else return false"""
        if(fillerGlass.getLevelOfColor()== 0 or fillerGlass.isEmpty()  ):   # tillerGlass does not have any colors.
            # print('\n ---Deleted: filler glass does not have colors')
            return False
        elif(self.GlassIsFull()):   # this glass now is full
            # print('\n ---Deleted: glass now is Full')
            return False
        elif(not(self.isEmpty()) and (self.tube.top().color() != fillerGlass.tube.top().color()) ):     # this glass is contain colors and available Space but color not match.
            # print('\n ---Deleted: glass contain colors and available space but not match color')
            return False
        elif(not(self.isEmpty()) and (self.tube.top().color() == fillerGlass.tube.top().color()) ): 
            availableSpace = self.capacity - self.levelOfColor
            lenColorFilling = fillerGlass.tube.top().lengthColor()
            if(availableSpace >= lenColorFilling):            
                insertedDrop = fillerGlass.popOutOfGlass()
                return self.pushToGlass(insertedDrop)
            else:       # (availableSpace < lenColorFilling):
                # neededLength = lenColorFilling - availableSpace
                insertedDrop = fillerGlass.popApartOfTopOutOfGlass(availableSpace)
                if (insertedDrop == None):
                    return False
                else:
                    return self.pushToGlass(insertedDrop)    
        
        elif( self.isEmpty() ):     # this glass empty but fillerGlass have colors
            availableSpace = self.capacity          # available space of this Glass 
            lenColorFilling = fillerGlass.tube.top().lengthColor()
            
            if(availableSpace >= lenColorFilling):            
                insertedDrop = fillerGlass.popOutOfGlass()
                return self.pushToGlass(insertedDrop)
            else:       # (availableSpace < lenColorFilling):
                # neededLength = lenColorFilling - availableSpace
                insertedDrop = fillerGlass.popApartOfTopOutOfGlass(availableSpace)
                if (insertedDrop == None):
                    return False
                else:
                    return self.pushToGlass(insertedDrop)
        
                
        
    
    def checkDone(self):
        """check whether the glass is done.
        Return True if full and the same or empty 
        Return false if not full or not the same color"""
        if(self.numOfColor() == 0):
            return True
        else:
            if(not(self.isTheSameColor())):
                return False
            else:
                thelevel = self.getLevelOfColor()
                if(thelevel> self.capacity):
                    raise Exception("Capacity does not enough space")
                elif(thelevel == self.capacity):
                    return True
                else:
                    return False            
         
    def getLevelOfColor(self):
        numOfCol = self.numOfColor();
        if(numOfCol == 0 ):
            self.levelOfColor = 0
            self.allTheSame = True      # ===========================
            return 0
        elif(numOfCol == 1):
            thelevel = self.tube.getItem(0).lengthColor()
            self.levelOfColor = thelevel
            self.allTheSame = True      # ===========================
            if(self.levelOfColor == self.capacity):
                self.isFull = True
            else:
                self.isFull = False
            return thelevel
        else:
            theLevel = 0
            for i in range(0,numOfCol):
                theLevel += self.tube.getItem(i).lengthColor()
            self.levelOfColor = theLevel
            if(self.levelOfColor == self.capacity):
                self.isFull = True
            else:
                self.isFull = False            
            return theLevel
        
    
    def topOfGlass(self):
        """get the top element of glass (Drop object).if Empty return None else: return Drop object at top of this Glass """
        return self.tube.top()
    
    def popOutOfGlass(self):
        """pop the top Drop object out of Glass. if empty return None else: return the top Drop object and reupdate params"""
        if(self.isEmpty()):
            return None
        else:
            topObject = self.tube.pop();
            self.allTheSame = self.isTheSameColor()
            self.isFull = False
            self.levelOfColor =self.getLevelOfColor()      # update the levelofcolor param
            return topObject
    
    def popApartOfTopOutOfGlass(self,length):
        """Pop a part not whole top Drop. if empty or not success return None else return a part of the top"""
        if(length <= 0 or self.isEmpty() ):
            return None
        elif(length == self.topOfGlass().lengthColor()):
            return self.popOutOfGlass()
        elif(length > self.topOfGlass().lengthColor()):
            return None
        else:
            topColor = self.topOfGlass().color()
            topLength = self.topOfGlass().lengthColor()
            self.topOfGlass().changeLength(topLength - length)
            self.isFull=False
            self.levelOfColor -= length
            neededDrop = Drop(topColor,length)
            return neededDrop
            
            
    
    def pushNoCheckNoUpdate(self,insertedDropObject):
        """push Drop object to Glass. Note that this function is NOT check whether top colors are matching and also space enough and not update params"""
        self.tube.push(insertedDropObject)
        
    def pushToGlass(self,insertedDropObject):
        """push Drop object to glass. 
        return True if push success
        return false if push fail"""
        if(insertedDropObject.lengthColor()<=0):
            print('\n ---Deleted: Drop with length <= 0')            
            return False
        elif(self.GlassIsFull()):       # glass does not having any space to store color of insertedDropObject        
            # print('\n ---Deleted: glass is full to inserted')
            return False        
        elif(self.isEmpty()):     # glass now is empty
            if(insertedDropObject.lengthColor()> self.capacity):
                # glass does not enough space to store color of insertedDropObject
                # print('\n ---Deleted: glass is empty but drop too large')
                return False
            elif (insertedDropObject.lengthColor() == self.capacity): 
                # print('\n ---Deleted: glass is empty and drop = capacity')
                self.pushNoCheckNoUpdate(insertedDropObject)
                self.allTheSame = True
                self.isFull=True 
                self.levelOfColor= self.capacity
                return True
            else:
                # print('\n ---Deleted: glass is empty and drop < capacity')
                self.pushNoCheckNoUpdate(insertedDropObject)
                self.allTheSame = True
                self.isFull=False   
                self.levelOfColor= insertedDropObject.lengthColor()   
                return True
        else:       #glass have color but not full
            if(self.topOfGlass().color() != insertedDropObject.color()):    # color not match
                # print('\n ---Deleted: glass have color and Space available but color No match')
                return False
            else:   # color match
                availableSpace = self.capacity - self.getLevelOfColor()
                if(insertedDropObject.lengthColor()> availableSpace):
                    # glass does not enough space to store color of insertedDropObject
                    # print('\n ---Deleted: glass have color match and Space available but Drop too large')
                    return False
                elif (insertedDropObject.lengthColor() == availableSpace ):
                    # print('\n ---Deleted: glass have color match and Space available = Drop')
                    newLengthOfTop = self.topOfGlass().lengthColor() + insertedDropObject.lengthColor()
                    self.topOfGlass().changeLength(newLengthOfTop)
                    self.isFull=True
                    self.levelOfColor= self.capacity
                    return True
                else:
                    # print('\n ---Deleted: glass have color match and Space available > Drop')
                    newLengthOfTop = self.topOfGlass().lengthColor() + insertedDropObject.lengthColor()
                    self.topOfGlass().changeLength(newLengthOfTop)
                    self.isFull=False
                    self.levelOfColor += insertedDropObject.lengthColor()
                    return True
                    
            
            
        
        
    
        
        
d1=Drop('Red',1)
d2=Drop('Blue',2)
d3=Drop('Blue',4)
d4=Drop('White',4)
d5=Drop('pink',5)

s1=Stack([])
s2=Stack([d3,d4])
# s2=Stack([])

g1=Glass('g1',s1,3)
g2=Glass('g2',s2,9)

g1()
g2()
print('\n')
print('filling:',g1.fillingColor(g2))
print('\n')
g1()
g2()



# d0 = Drop('Red',0)
# d1=Drop('Red',4)
# d2=Drop('Blue',1)
# d3=Drop('Blue',3)
# d4=Drop('Green',1)

# s1 = Stack([d1,d2])
# g1 = Glass('ahihi',s1,7)

# g1()

# print('\n')
# print(g1.popApartOfTopOutOfGlass(5))
# print('\n')
# g1()
# g1()
# print('\nDone:',g1.checkDone())
# print('\ntop: ',g1.topOfGlass())
# s1 = Stack([d1,d2])
# s1 = Stack([d1])
# s1 = Stack([d1,d2,d3,d4])
# print(g1.fillingColor(g1))



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
