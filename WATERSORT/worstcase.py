import math
from queue import PriorityQueue
from ds import *

# def showa(priori):
    
#     if priori.empty():
#         print ('rong')
#         return 
#     a = []
#     b = []
#     while not priori.empty():
#         tmp = priori.get()        
#         a.append(tmp) 
#         b.append(tmp.fScore) 
    
#     for t in a:
#         priori.put(t)
#     print(a)
#     print(b)

def show(priori):
    if priori.empty():
        print('rong')
        return
    a = []
    while not priori.empty():
        tmp = priori.get()
        a.append(tmp.fScore)   
    print(a) 

q = PriorityQueue()
s1 = heurState(
    Glass(10,
        ['Red','Green','Blue']
    ),
    None
)
s1.fScore= 1

s2 = heurState(
    Glass(10,
        ['Red','Green','Blue']
    ),
    None
)
s2.fScore= 2

s3 = heurState(
    Glass(10,
        ['Yellow','Gray','Brown']
    ),
    None
)
s3.fScore = 3

s4 = heurState(
    Glass(10,
        ['Gray','Brown']
    ),
    None
)
s4.fScore = 4

s5 = heurState(
    Glass(10,
        ['Gray','Brown']
    ),
    None
)
s5.fScore = 5

q.put(s1)
# a = ''
# for s in q.queue:
#     a+=str(s.fScore)
#     a+= ' '
# print(a)
q.put(s2)
q.put(s3)
q.put(s4)
q.put(s5)
# show(q)
# print(q.queue)
s2.fScore = 50
s3.fScore = 100
s1.fScore = 999
# q.queue[4].fScore=1000
show(q)



# print(q.get().fScore)
# print(q.get().fScore)
# print(q.get().fScore)
# print(q.get().fScore)

# q.put((5,s3) )
# print( q.queue)
# q.get()
# print(q.queue)

# q.put((2,s4) )
# print( q.queue)
