from ds import *

state1 = State([Glass(4,["orange", "blue", "red"]), Glass(4,["red", "red", "blue"])])
state2 = State([Glass(4,["orange", "blue", "red"]), Glass(4,["red", "red", "red"])])
print(state1 == state2) 