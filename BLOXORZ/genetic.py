from ds import *
import random

def genetic(initState):
    population = initPopulation(initState)
    
    while not checkSolution(population):
        evaluate(population)
        select(population)
        makeCrossover(population)
        mutate(population)
        
    return checkSolution(population)
    
    
    
# Phase 1
def initPopulation(initState):
    size = 300
    population = []
    moves = ['up', 'down', 'left', 'right']
    
    for i in range(size):
        chromosome = Chromosome(50)
        DNA = [random.choice(moves) for i in range(chromosome.length)]
        if checkValidDNA(DNA, initState):
            chromosome.DNAs.append(DNA)
        population.append(chromosome)

    
def checkValidDNA(DNA, initState):
    state = copy.deepcopy(initState)
    
    for move in DNA:
        if move == 'up':
            state.block.moveUp()
        elif move == 'down':
            state.block.moveDown()
        elif move == 'right':
            state.block.moveRight()
        elif move == 'left':
            state.block.moveLeft()
        
        if state.isValidState():
            return False
    
    return True

            
def checkSolution(population, initState):
    for chromosome in population:
        for DNA in chromosome.DNAs:
            state = copy.deepcopy(initState)
            for move in DNA:
                if move == 'up':
                    state.block.moveUp()
                elif move == 'down':
                    state.block.moveDown()
                elif move == 'right':
                    state.block.moveRight()
                elif move == 'left':
                    state.block.moveLeft()
                
                if state.checkGameStatus():
                    return state
    
    return False
            
            
            
# Phase 2
def evaluate(population):
    

def fitness(state): pass

def select(): pass

def makeCrossover(): pass

def mutate(): pass
        