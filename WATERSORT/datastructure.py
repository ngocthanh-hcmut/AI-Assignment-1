from collections import deque
from inspect import stack

# stack data structure
class Stack:
    def __init__(self,list=[]):
        self.stack = deque(list)
    
    def __call__(self):
        
        return self.stack

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
    
# Color drop: giọi màu
class Drop:
    def __init__(self,color,length):
        # self.col = color
        # self.len = length
        self.dropColor={'col':color ,'len':length}
    
    def __call__(self):
        return self.dropColor
    
    def changeColor(self,color):
        self.dropColor['col']=color
    
    def changeLength(self,length):
        self.dropColor['len'] = length
    
    def color(self):
        return self.dropColor['col']
    def length(self):
        return self.dropColor['len']
  
d1 = Drop('R',10);
d2 = Drop('B',5);
s1 = Stack([d1,d2])

# Glass contain color
class Glass:
    def __init__(self):
        self.isDone = False
        self.name=''
        self.capacity=0
        self.tube = Stack()
    
    def __call__(self):
        print(
            '{',
                '\t','name:',self.name,
                '\n\t','capacity:', self.capacity,
                '\n\t','Done:',self.isDone,
                '\n\t','tube: {'
        );
        for color in self.tube():
            print('\t     ',color(),',')
        print('\t}\n}')
        
    

g1 = Glass()
g1.tube = s1;
g1()
