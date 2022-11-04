from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
import random
from Block.Block import Block
from Floor import Floor
from Square.NoneSquare import NoneSquare
from Square.HideSquare import HideSquare
from StateGenetic import StateGenetic


class GeneticAgorithm:
    DNA_LENGTH = 30
    PUPOLATION = 40
    MUTATE_NUMBER = 10
    DNA_LENGTH_TO_MUTATE = 5

    def __init__(self, level, floor) -> None:
        self.states = []
        self.scoreMap = []
        self.level = level
        self.stopExecute = False
        self.generation = 0
        self.makeScoreMap(floor)
        self.setSquareScore(floor)
        self.generatePopulation()
        self.totalScore = 0

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
        self.calculateFitnessScore()
        self.calculateSelectionRate()
        # print(self.scoreMap)
        # for i in range(len(self.states)):
        #     print("state ", i, ": score=", self.states[i].fitnessScore, "DNA= ", self.states[i].DNA , "selectionRate=", self.states[i].selectionRate)
        # self.crossOver(self.makeSelection())
        # print("crossover")
        # for i in range(len(self.states)):
        #     print("state ", i, ": score=", self.states[i].fitnessScore, "DNA= ", self.states[i].DNA , "selectionRate=", self.states[i].selectionRate, "position=", self.states[i].block.currentSquare, "status=", self.states[i].status)
        # print("make selection")
        # for dna in self.makeSelection():
        #     print(dna)
        self.crossOver(self.makeSelection())
        self.mutate()
    
    
    def makeScoreMap(self, floor):
        scoreMap = []
        for squareRow in floor.squares:
            scoreRow = []
            for square in squareRow:
                if isinstance(square, NoneSquare) and not(isinstance(square, HideSquare)):
                    scoreRow.append(-2)
                else:
                    scoreRow.append(-1)
            scoreMap.append(scoreRow)
        self.scoreMap = scoreMap

    def checkScoreMapFilled(self):
        for row in self.scoreMap:
            for value in row:
                if value == -1:
                    return False
        return True

    def setSquareScore(self, floor):
        centerX = floor.holeSquare.xPosition
        centerY = floor.holeSquare.yPosition
        maxScore = (len(floor.squares) + len(floor.squares[0])) + 10
        self.scoreMap[centerY][centerX] = maxScore
        self.setScore(maxScore)
        
    def setScore(self, score):
        if self.checkScoreMapFilled(): return
        for i in range(len(self.scoreMap)):
            for j in range(len(self.scoreMap[i])):
                if self.scoreMap[i][j] == score:
                    if i+1 < len(self.scoreMap):
                        if self.scoreMap[i+1][j] == -1:
                            self.scoreMap[i+1][j] = score - 1 
                    if i - 1 >= 0:
                        if self.scoreMap[i-1][j] == -1:
                            self.scoreMap[i-1][j] = score - 1 
                    if j+1 < len(self.scoreMap[i]):
                        if self.scoreMap[i][j+1] == -1:
                            self.scoreMap[i][j+1] = score - 1
                    if j -1 >= 0:
                        if self.scoreMap[i][j-1] == -1:
                            self.scoreMap[i][j-1] = score -1
        self.setScore(score-1)

    def calculateFitnessScore(self):
        self.totalScore = 0
        for state in self.states:
            score = 0
            for position in state.block.currentSquare:
                x = position["xPosition"]
                y = position["yPosition"]
                score = self.scoreMap[y][x] if score < self.scoreMap[y][x] else score
            state.fitnessScore = score * 3
            self.totalScore += score

    def calculateSelectionRate(self):
        for state in self.states:
            state.selectionRate = round((state.fitnessScore / self.totalScore) * 100)

    def makeSelection(self):
        selection = []
        for i in range(self.PUPOLATION):
            num = random.randint(0,99)
            count = 0
            for state in self.states:
                if num <= count + state.selectionRate:
                    selection.append(state.DNA)
                    break
                else:
                    count = count + state.selectionRate
        # while len(selection) < self.PUPOLATION:
        #     selection.append([random.randint(1,3)] for i in range(self.PUPOLATION))
        return selection

    def crossOver(self, selection):
        self.states = []
        i = 0
        # print("cross over")
        while i < len(selection):
            dna1 = []
            dna2 = []
            cha = selection[i]
            me = selection[i+1] if i+1 < len(selection) else selection[i]
            crossPosition = random.randint(1, self.DNA_LENGTH-2)
            for j in range(self.DNA_LENGTH):
                if j <=crossPosition:
                    dna1.append(cha[j])
                    dna2.append(me[j])
                else:
                    dna1.append(me[j])
                    dna2.append(cha[j])
            floor1 = Floor(self.level)
            block1 = Block(floor1.startSquare.xPosition, floor1.startSquare.yPosition)
            state1 = StateGenetic(block1, floor1, dna1)
            floor2 = Floor(self.level)
            block2 = Block(floor2.startSquare.xPosition, floor2.startSquare.yPosition)
            state2 = StateGenetic(block2, floor2, dna2)
            self.states.append(state1)
            self.states.append(state2)
            i += 2
        
        
    def mutate(self):
        for i in range(self.MUTATE_NUMBER):
            positionToMutate = random.randint(0, self.PUPOLATION-1)
            self.states[positionToMutate].mutate(self.DNA_LENGTH_TO_MUTATE, self.DNA_LENGTH)

    def round(number):
        afterDot = number % 1
        beforDot = int(number)
        if afterDot >= 0.5: 
            return beforDot + 1
        else:
            return beforDot