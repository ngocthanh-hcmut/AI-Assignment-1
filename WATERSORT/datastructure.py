from collections import deque

class Stack:
    def __init__(self,list=[]):
        self.stack = deque(list)
    
    def __call__(self):
        print(self.stack)

    def push(self,elem):
        pass
    
    def pop(self):
        pass
    
    def top(self):
        pass

    def isEmpty(self):
        if(self.length() >0):
            return False
        else:
            return  True
    
    def length(self):
        return len(self.stack)
    
# s1 = Stack((1,2,'hehe'))
# s1()
# print(s1.length())
# print(s1.isEmpty())





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
        
# color = 'R'
# length =10
# d1 = Drop(color,length)
# d1()
# print(d1.dropColor['col'])
# d1.dropColor['col']='W'
# d1()
# d1.dropColor['len']=9
# d1()

# d1.changeColor('A')
# d1()
# d1.changeLength(-4)
# d1()
# print(d1.color())
# print(d1.length())



class Glass:
    def __init__(self):
        self.isDone = False
        self.name=''
        self.capacity=0
        self.tube