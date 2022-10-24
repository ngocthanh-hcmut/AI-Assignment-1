from collections import deque

class Stack:
    def __init__(self,list=[]):
        self.stack = deque(list)
    
    def __call__(self):
        print(self.stack)

    def push(self,elem):
        self.stack.appendleft(elem)
    
    def pop(self):
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
        if(self.length() >0):
            return False
        else:
            return  True
    
    def length(self):
        return len(self.stack)
    

class Drop:
    def __init__(self,color,length):
        # self.col = color
        # self.len = length
        self.dropColor={'col':color ,'len':length}
    
    def __call__(self):
        print(self.dropColor)
    
    def changeColor(self,color):
        self.dropColor['col']=color
    
    def changeLength(self,length):
        self.dropColor['len'] = length
    
    def color(self):
        return self.dropColor['col']
    def length(self):
        return self.dropColor['len']
        

class Glass:
    def __init__(self):
        self.isDone = False
        self.name=''
        self.capacity=0
        self.tube