from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
import random
from time import sleep
from Block.Block import Block
from Floor import Floor
from Square.NoneSquare import NoneSquare
from Square.HideSquare import HideSquare
from StateGenetic import StateGenetic


class GeneticAgorithm:
    DNA_LENGTH = 100  
    PUPOLATION = 100
    MUTATE_RATE = 5

    def __init__(self, level, floor) -> None:
        self.states = []
        self.scoreMap = []
        self.level = level
        self.stopExecute = False
        self.generation = 0
        self.makeScoreMap(floor)
        self.setSquareScore(floor)
        # self.setButtonScore(floor)
        self.generatePopulation()
        self.totalScore = 0
        self.solution = None

    def generatePopulation(self):
        # print("genetic: generating population")
        for i in range(self.PUPOLATION):
            floor = Floor(self.level)
            block = Block(floor.startSquare.xPosition, floor.startSquare.yPosition)
            DNA = [random.randint(1, 4) for i in range(self.DNA_LENGTH)]
            state = StateGenetic(block, floor, self.scoreMap, DNA, i)
            self.states.append(state)

    def execute(self, screen=None):
        if self.solution != None: 
            self.stopExecute = True
            return
        self.generation += 1
        # print("Thriving in generation ", self.generation)
        executor = ThreadPoolExecutor(max_workers=self.PUPOLATION)
        futures = [executor.submit(state.thrive, screen) for state in self.states]
        done, not_done = wait(futures, return_when=ALL_COMPLETED)
        for future in done:
            if future.result():
                print("Solution found at generation:", self.generation)
                self.solution = future.result()
                print(self.solution)
                self.stopExecute = True
                return future.result()

        # print("generation done thriving")
        self.calculateTotalScore()
        self.calculateSelectionRate()
        # print(self.makeSelection())
        self.crossOver(self.makeSelection())


        # print("done thriving gen", self.generation,"with population: ")
        # for state in self.states:
        #     print("state", state.id, "dna:", state.DNA)
        # # self.mutate()

        # sleep(0.25)
        return None
    
    
    def makeScoreMap(self, floor):
        print("genetic: Making score map")
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
        maxScore = (len(floor.squares) + len(floor.squares[0])) + 6
        self.scoreMap[centerY][centerX] = maxScore
        self.setScore(maxScore)

    # def setButtonScore(self, floor):
    #     for square in self.floor.toggleSquares:
    #         x = square.xPosition
    #         y = square.yPosition
    #         self.scoreMap[y][x] = 3
    #         self.setScore

        
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

    def calculateTotalScore(self):
        # print("genetic: calculate total score: ")
        self.totalScore = 0
        for state in self.states:
            # print("state", state.id, "score =", state.fitnessScore)
            self.totalScore += state.fitnessScore
        # print("total =", self.totalScore)

    def calculateSelectionRate(self):
        # print("genetic: calculate selection rate")
        for state in self.states:
            state.selectionRate = round((state.fitnessScore / self.totalScore) * 100)
            # print("state", state.id, "rate =", state.selectionRate)

    def makeSelection(self):
        # print("genetic: making selection")
        selection = []
        for i in range(self.PUPOLATION):
            num = random.randint(0,99)
            count = 0
            for state in self.states:
                if num <= count + state.selectionRate:
                    info = dict(dna=state.DNA, crossIndex=state.longestMove, score=state.fitnessScore)
                    # print("state", state.id, "dna:", info["dna"], "score =", state.fitnessScore)
                    selection.append(info)
                    break
                else:
                    count = count + state.selectionRate
        return selection

    def crossOver(self, selection):
        # print("genetic: crossing")
        i = 0
        while i < len(selection):
            dna1 = []
            dna2 = []

            cha = selection[i]["dna"]
            me = selection[i+1]["dna"] if i+1 < len(selection) else selection[i]["dna"]

            crossIndex1 = selection[i]["crossIndex"]
            crossIndex2 = selection[i+1]["crossIndex"] if i+1 < len(selection) else selection[i]["crossIndex"]

            score1 = selection[i]["score"]
            score2 = selection[i+1]["score"] if i+1 < len(selection) else selection[i]["score"]

            crossPosition = crossIndex1 if score1 > score2 else crossIndex2
            # print("pair", (i/2), "cross position =", crossPosition)
            for j in range(self.DNA_LENGTH):
                if j <= crossPosition:
                    dna1.append(cha[j])
                    dna2.append(me[j])
                else:
                    dna1.append(me[j])
                    dna2.append(cha[j])

            self.states[i].reset(dna1)
            self.states[i].mutate(self.MUTATE_RATE, crossPosition+1)
            if i+1 < len(self.states):
                self.states[i+1].reset(dna2)
            i += 2
        
        
    # def mutate(self):
    #     i = random.randint(0, 99)
    #     if i >= self.MUTATE_RATE:
    #         return
    #     i = random.randint(0, len(self.states)-1)
    #     self.states[i].mutate()

    def round(number):
        afterDot = number % 1
        beforDot = int(number)
        if afterDot >= 0.5: 
            return beforDot + 1
        else:
            return beforDot

    def showSolution(self, screen, level):
        floor = Floor(level)
        block = Block(floor.startSquare.xPosition, floor.startSquare.yPosition)
        state = StateGenetic(block, floor, self.scoreMap, self.solution)
        state.thrive(screen, block = True)

