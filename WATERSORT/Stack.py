from collections import deque


class Stack:
    def __init__(self,list=[]):
        self.listElems = deque(list)
    
    def getListElems(self):
        """Return list of elements in stack"""
        return self.listElems
    
    def getSize(self):
        """Return the number of elements that Stack containing"""
        return len(self.listElems)
    
    def isEmpty(self):
        """check whether stack is empty"""
        if(self.getSize() >0):
            return False
        else:
            return True

    def push(self,elem):
        """Push elem to the stack. Param: elem"""
        self.listElems.appendleft(elem)
    
    def pop(self):
        """Pop the top element out of stack"""
        if(self.isEmpty()):
            return None
        else:
            return self.listElems.popleft()
    
    def top(self):
        """get the top element of stack"""
        if(self.isEmpty()):
            return None
        else:
            return self.listElems[0]
   
    def getItem(self,index):
        """---OK---return the element at index of stack"""
        size = self.getSize()
        if(size == 0 or index >=size):
            return None
        else:
            return self.listElems[index]
        
    def removeItem(self,index):
        """---OK---remove the element at index of stack"""
        size = self.getSize()
        if(index >=0):
            if(index>=size):
                raise Exception("index out of range of index to remove")              
            else:
                del self.listElems[index]
                return True
        else:
            if(index<(-1*size)):
                raise Exception("index out of range of index to remove")    
            else:
                del self.listElems[index]
                return True             
    
