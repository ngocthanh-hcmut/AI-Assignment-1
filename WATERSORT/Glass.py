from Drop import Drop
from Stack import Stack



# Glass contain color
class Glass:
    def __init__(self,name='',stackColor = Stack(),capacity=2):
        self.name = name                                    # the name of glass
        self.capacity = capacity if capacity >= 2 else 2    # the capacity of glass
        self.isSameColor = False                            # the variable to show this glass is the same color
        self.isFull = False                                 # the variable to show this glass is Full
        self.size = 0                                       # the variable to show the height of color in this glass
        self.stackColor = stackColor                        # store the stack contain all color.

        # self.__call__()
        self.preOperate()
        # self.__call__()
        
    
    def __call__(self):
        print(
            '{',
                '\t','name:',self.name,
                '\n\t','capacity:', self.capacity,
                '\n\t','isSameColor:',self.isSameColor,
                '\n\t','isFull:',self.isFull,
                '\n\t','size:',self.size,
                '\n\t','stackColor: {'
        );
        for drop in self.stackColor.getListElems():
            print('\t     {',drop.getColor(),' - ',drop.getSize(),'}')
        print('\t}\n}')
        
    def isGlassFull(self):
        """---OK---Check where the glass is FUll"""
        numOfColors = self.getNumOfColors()
        size = 0
        for i in range(0,numOfColors):
            size += self.stackColor.getItem(i).getSize()
        # print(size)
        if(size > self.capacity):
            raise Exception("Capacity does not enough space")
        elif(size == self.capacity):
            self.isFull = True
            self.size = size
            return True
        else:
            self.isFull = False
            self.size = size
            return False
        
    def isEmpty(self):
        """---OK---Check whethe the glass is empty"""
        if(self.stackColor.isEmpty()):
            self.isSameColor=True
            self.isFull = False
            self.size = 0
            return True
        return False
        
    def preOperate(self):
        """---OK---"""
        # empty stack.
        numOfColors = self.getNumOfColors()
        if(numOfColors == 0):
            self.isSameColor = True
            self.isFull = False
            self.size = 0
            return
        # stack with 1 color:
        elif(numOfColors == 1):
            self.size = self.stackColor.getItem(0).getSize()
            if(self.size < 0 ):
                raise Exception("the size of the top element wrong")
            elif(self.size == 0):
                self.isSameColor = True
                self.isFull = False
                self.stackColor.pop()
                return
            elif(self.size > self.capacity):
                raise Exception("Capacity does not enough space")
            elif (self.size == self.capacity):
                self.isSameColor=True
                self.isFull=True
            else:
                self.isSameColor=True
                self.isFull=False
            return
        # stack with many colors.
        else:
            # caculate the level
            size = 0
            for color in self.stackColor.getListElems():
                size += color.getSize()
            self.size = size
            if(self.size > self.capacity):
                raise Exception("Capacity does not enough space")
            elif (self.size == self.capacity):
                self.isFull = True
                self.isSameColor = self.isTheSameColor()
            else:
                self.isFull = False
                self.isSameColor = self.isTheSameColor()
            # self.__call__()

            # combine 2 color the same color surrounding
            theNumberOfColors = self.getNumOfColors()
            index = 1
            while(index < theNumberOfColors):
                if(self.stackColor.getItem(index).getColor() == self.stackColor.getItem(index-1).getColor()):
                    sizeOfColor = self.stackColor.getItem(index-1).getSize()
                    sizeOfColor += self.stackColor.getItem(index).getSize()
                    self.stackColor.getItem(index).setSize(sizeOfColor)
                    self.stackColor.removeItem(index-1)
                    theNumberOfColors-=1
                    # continue
                else:
                    index+=1      
             
    def isTheSameColor(self):
        """---OK---check whether all the color in glass is the same color.
        If no color or one color => True
        If all the same color => true
        else => false
        Returns:Bool            
        """
        theNumberOfColors = self.getNumOfColors()      
        if(theNumberOfColors == 0 or theNumberOfColors == 1):
            self.isSameColor =True
            return True
        else:
            for i in range(0,theNumberOfColors-1):
                if(self.stackColor.getItem(i).getColor() !=  self.stackColor.getItem(i+1).getColor()):
                    self.isSameColor =False                    
                    return False
            self.isSameColor =True
            return True
                    
    def getNumOfColors(self):
        """---OK---the number of colors that Glass is containing"""
        return self.stackColor.getSize()
        
    def fillColor(self,sourceGlass):
        """---OK---filling this glass by color in sourceGlass. Return true if filling process succees else return false"""
        if(sourceGlass.getSizeOfGlass()== 0 or sourceGlass.isEmpty()  ):   # tillerGlass does not have any colors.
            # print('\n ---Deleted: filler glass does not have colors')
            return False
        elif(self.isGlassFull()):   # this glass now is full
            # print('\n ---Deleted: glass now is Full')
            return False
        elif(not(self.isEmpty()) and (self.topOfGlass().getColor() != sourceGlass.topOfGlass().getColor()) ):     # this glass is contain colors and available Space but color not match.
            # print('\n ---Deleted: glass contain colors and available space but not match color')
            return False
        elif(not(self.isEmpty()) and (self.topOfGlass().getColor() == sourceGlass.topOfGlass().getColor()) ): 
            availableSpace = self.capacity - self.size
            sizeOfSource = sourceGlass.topOfGlass().getSize()
            if(availableSpace >= sizeOfSource):            
                insertedDrop = sourceGlass.popOutOfGlass()
                return self.pushToGlass(insertedDrop)
            else:       # (availableSpace < sizeOfSource):
                # neededLength = sizeOfSource - availableSpace
                insertedDrop = sourceGlass.popApartOfTopOutOfGlass(availableSpace)
                if (insertedDrop == None):
                    return False
                else:
                    return self.pushToGlass(insertedDrop)    
        
        elif( self.isEmpty() ):     # this glass empty but sourceGlass have colors
            availableSpace = self.capacity          # available space of this Glass 
            sizeOfSource = sourceGlass.topOfGlass().getSize()
            
            if(availableSpace >= sizeOfSource):            
                insertedDrop = sourceGlass.popOutOfGlass()
                return self.pushToGlass(insertedDrop)
            else:       # (availableSpace < sizeOfSource):
                # neededLength = sizeOfSource - availableSpace
                insertedDrop = sourceGlass.popApartOfTopOutOfGlass(availableSpace)
                if (insertedDrop == None):
                    return False
                else:
                    return self.pushToGlass(insertedDrop)
        

    
    def isGlassDone(self):
        """---OK---check whether the glass is done.
        Return True if full and the same or empty 
        Return false if not full or not the same color"""
        if(self.getNumOfColors() == 0):
            return True
        else:
            if(not(self.isTheSameColor())):
                return False
            else:
                sizeOfGlass = self.getSizeOfGlass()
                if(sizeOfGlass > self.capacity):
                    raise Exception("Capacity does not enough space")
                elif(sizeOfGlass == self.capacity):
                    return True
                else:
                    return False            
         
    def getSizeOfGlass(self):
        """---OK---Return the size of colors in glass"""
        numOfColors = self.getNumOfColors();
        if(numOfColors == 0 ):
            self.size = 0
            self.isSameColor = True      # ===========================
            return 0
        elif(numOfColors == 1):
            size = self.stackColor.getItem(0).getSize()
            self.size = size
            self.isSameColor = True      # ===========================
            if(self.size > self.capacity):
                raise Exception("Capacity does not enough space") 
            elif(self.size == self.capacity):
                self.isFull = True
            else:
                self.isFull = False
            return size
        else:
            size = 0
            for i in range(0,numOfColors):
                size += self.stackColor.getItem(i).getSize()
            self.size = size
            if(self.size > self.capacity):
                raise Exception("Capacity does not enough space") 
            elif(self.size == self.capacity):
                self.isFull = True
            else:
                self.isFull = False            
            return size
        
    
    def topOfGlass(self):
        """---OK---get the top element of glass (Drop object).if Empty return None else: return Drop object at top of this Glass """
        return self.stackColor.top()
    
    def popOutOfGlass(self):
        """---OK---pop the top Drop object out of Glass. if empty return None else: return the top Drop object and reupdate params"""
        if(self.isEmpty()):
            return None
        else:
            topObject = self.stackColor.pop();
            self.isSameColor = self.isTheSameColor()
            self.isFull = False
            self.size =self.getSizeOfGlass()      # update the levelofcolor param
            return topObject
    
    def popApartOfTopOutOfGlass(self,length):
        """---OK---Pop a part not whole top Drop. if empty or not success return None else return a part of the top"""
        if(length <= 0 or self.isEmpty() ):
            return None
        elif(length == self.topOfGlass().getSize()):
            return self.popOutOfGlass()
        elif(length > self.topOfGlass().getSize()):
            return None
        else:
            topColor = self.topOfGlass().getColor()
            topSize = self.topOfGlass().getSize()
            self.topOfGlass().setSize(topSize - length)
            self.isFull=False
            self.size -= length
            neededDrop = Drop(topColor,length)
            return neededDrop
                    
    
    def pushNoCheckNoUpdate(self,insertedDropObject):
        """---OK---push Drop object to Glass. Note that this function is NOT check whether top colors are matching and also space enough and not update params"""
        self.stackColor.push(insertedDropObject)
        
    def pushToGlass(self,insertedDropObject):
        """---OK---push Drop object to glass. 
        return True if push success
        return false if push fail"""
        if(insertedDropObject.getSize()<=0):
            # print('\n ---Deleted: Drop with length <= 0')            
            return False
        elif(self.isGlassFull()):       # glass does not having any space to store color of insertedDropObject        
            # print('\n ---Deleted: glass is full to inserted')
            return False        
        elif(self.isEmpty()):     # glass now is empty
            if(insertedDropObject.getSize()> self.capacity):
                # glass does not enough space to store color of insertedDropObject
                # print('\n ---Deleted: glass is empty but drop too large')
                return False
            elif (insertedDropObject.getSize() == self.capacity): 
                # print('\n ---Deleted: glass is empty and drop = capacity')
                self.pushNoCheckNoUpdate(insertedDropObject)
                self.isSameColor = True
                self.isFull=True 
                self.size= self.capacity
                return True
            else:
                # print('\n ---Deleted: glass is empty and drop < capacity')
                self.pushNoCheckNoUpdate(insertedDropObject)
                self.isSameColor = True
                self.isFull=False   
                self.size= insertedDropObject.getSize()   
                return True
        else:       #glass have color but not full
            if(self.topOfGlass().getColor() != insertedDropObject.getColor()):    # color not match
                # print('\n ---Deleted: glass have color and Space available but color No match')
                return False
            else:   # color match
                availableSpace = self.capacity - self.getSizeOfGlass()
                if(insertedDropObject.getSize()> availableSpace):
                    # glass does not enough space to store color of insertedDropObject
                    # print('\n ---Deleted: glass have color match and Space available but Drop too large')
                    return False
                elif (insertedDropObject.getSize() == availableSpace ):
                    # print('\n ---Deleted: glass have color match and Space available = Drop')
                    newSize = self.topOfGlass().getSize() + insertedDropObject.getSize()
                    self.topOfGlass().setSize(newSize)
                    self.isFull=True
                    self.size= self.capacity
                    return True
                else:
                    # print('\n ---Deleted: glass have color match and Space available > Drop')
                    newSize = self.topOfGlass().getSize() + insertedDropObject.getSize()
                    self.topOfGlass().setSize(newSize)
                    self.isFull=False
                    self.size += insertedDropObject.getSize()
                    return True
                    
            
            
d1=Drop('Red',1)
d2=Drop('Blue',2)
d3=Drop('Blue',4)
d4=Drop('White',4)
d5=Drop('pink',5)

s1 = Stack([d1,d2])
g1 = Glass('ahii',s1,11)
g1()