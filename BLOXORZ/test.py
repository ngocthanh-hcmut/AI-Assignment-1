import os, os.path
from input import *
from output import *
from depthFirstSearch import *
from ds import *

linkInput = open("Input/" + str(2) + "link", "r")
links = linkInput.readlines()
    
for i in range(len(links)):
    links[i] = links[i].split()

for i in range(len(links)):
    for j in range(len(links[i])):
        links[i][j] = links[i][j].split(',')

print(links)
