from Floor import *
from State import *
from Block.Block import *


state1 = State(Floor(0), Block(1,2))
state2 = State(Floor(0), Block(1,1))

print(state1 == state2)