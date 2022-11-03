from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
import random
from Block.Block import Block
from Floor import Floor
from NEW_BLOXORZ.Square.NoneSquare import NoneSquare
from StateGenetic import StateGenetic


class GeneticAgorithm:
    DNA_LENGTH = 20
    PUPOLATION = 2
    MUTATE_NUMBER = 0
    DNA_LENGTH_TO_MUTATE = 0

    def __init__(self, level) -> None:
        self.states = []
        self.scoreMap = []
        self.level = level
        self.stopExecute = False
        self.generation = 0
        self.generatePopulation()

    def generatePopulation(self):
        for i in range(self.PUPOLATION):
            floor = Floor(self.level)
            block = Block(floor.startSquare.xPosition, floor.startSquare.yPosition)
            state = StateGenetic(block, floor)
            state.DNA = [random.randint(1, 4) for i in range(self.DNA_LENGTH)]
            self.states.append(state)

    def execute(self, screen):
        self.generation += 1
        print("Thriving in generation ", self.generation)
        executor = ThreadPoolExecutor(max_workers=self.PUPOLATION)
        futures = [executor.submit(state.thrive, screen) for state in self.states]
        done, not_done = wait(futures, return_when=ALL_COMPLETED)
        print("generation done thriving")
        self.crossOver()
    
    
    def makeScoreMap(self, floor):
        scoreMap = []
        for squareRow in floor.squares:
            scoreRow = []
            for square in squareRow:
                if isinstance(square, NoneSquare):
                    scoreRow.append(-1)
                else:
                    scoreRow.append(0)
            scoreMap.append(scoreRow)

    def setSquareScore(self, x, y, floor):
        centerX = floor.holeSquare.xPosition
        centerY = floor.holeSquare.yPosition
        maxScore = (len(floor.squares) + len(floor.squares[0])) * 2
        

    def calculateFitnessScore(self, floor):
        pass

    def calculateSelectionRate(self):
        pass

    def makeSelection(self):
        pass

    def crossOver(self):
        self.states = []
        self.generatePopulation()

    def mutate(self):
        pass
