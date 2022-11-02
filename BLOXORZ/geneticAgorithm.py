from asyncio import ALL_COMPLETED
from concurrent.futures import ThreadPoolExecutor
import copy as cp
import random
from turtle import pos
import squarePrism as prism
import globalVariable as const
import rounder as r
from concurrent import futures as ftr
import pygame

class GeneticAgorithm:

    population = const.POPULATION
    creatures = []
    selection = []
    inputMap = None
    scoreMap = None
    totalScore = 0
    screen = None

    def __init__(self, inputMap, scoreMap, screen):
        self.inputMap = inputMap
        self.scoreMap = scoreMap
        self.generatePopulation()
        self.generation = 0
        self.screen = screen

    def generatePopulation(self):
        i = 1
        while i <= self.population:
          self.creatures.append(prism.SquarePrism(self.inputMap, self.scoreMap))
          i = i + 1

    def makeSelection(self):
        self.selection = []
        # print("making selection: ")
        for i in range(0, len(self.creatures)):
            a = 0
            num = random.randint(1, 100)
            for individual in self.creatures:
                a = a + individual.selectionRate
                if a >= num:
                    self.selection.append(individual)
                    break

        # for i in range(0, len(self.selection)):
        #     print("DNA: ", self.selection[i].DNA)

    def crossOver(self):
        newGeneration = []
        for i in range(0, len(self.selection), 2):
            # print("Crossing creatures")
            numberToCut = random.randint(1,const.DNA_LENGTH-1) #number of DNA to cut
            # print("Number to cut: ", numberToCut)
            fatherDNA = self.selection[i].DNA
            motherDNA = None
            if i+1 >= len(self.selection):
                motherDNA = fatherDNA
            else:
                motherDNA = self.selection[i+1].DNA
            child1Dna = []
            child2Dna = []
            # print("father dna: ", fatherDNA)
            # print("mother dna: ", motherDNA)
            for j in range(0, const.DNA_LENGTH):
                # print("alo ", j)
                if j+1 <= numberToCut:
                    child1Dna.append(motherDNA[j])
                    child2Dna.append(fatherDNA[j])
                else:
                    child1Dna.append(fatherDNA[j])
                    child2Dna.append(motherDNA[j])
            # print("child 1 dna = ", child1Dna)
            # print("child 2 dna = ", child2Dna)
            child1 = prism.SquarePrism(self.inputMap, self.scoreMap, child1Dna)
            # print("child dna 1: ", child1Dna)
            # print("child dna 2: ", child2Dna)
            child2 = prism.SquarePrism(self.inputMap, self.scoreMap, child2Dna)
            newGeneration.append(child1)
            newGeneration.append(child2)
        
        # apply new generation
        # print("new gen: ",len(newGeneration))
        self.creatures = newGeneration

        # for i in range(0, len(self.creatures)):
        #     print("DNA: ", self.creatures[i].DNA)
        



    def mutate(self):
        if const.NUMBER_OF_GEN_TO_MUTATE > len(self.creatures): return
        for i in range(0, const.NUMBER_TO_MUTATE):
            position = random.randint(0, len(self.creatures)-1)
            self.creatures[position].mutate()

    def fitnessFunction(self):
        pass

    def updatePosition(self, screen):
        for prism in self.creatures:
            prism.render(screen)

    def showGeneration(self, screen):
        background = pygame.image.load('image/background.jpg')
        screen.blit(background, (0,0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        self.generation = self.generation + 1
        message = "Genetic: Thriving in generation: " + str(self.generation)
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render(message, True, (255,255,255))
        self.screen.blit(text, (0, (const.BRICK_SIZE+1)*len(self.inputMap)))

    def thrive(self):
        self.showGeneration(self.screen)
        futures = []
        with ThreadPoolExecutor(max_workers=len(self.creatures)) as executor:
            for creature in self.creatures:
                future = executor.submit(creature.thrive)
                futures.append(future)
        # done, notdone = ftr.wait(futures, return_when=ALL_COMPLETED)
        # print("done: ", done)
        # print("not done: ", notdone)
        self.sortByScore()
        self.calculateTotalScore()
        self.calculateSelectionRate()
        self.makeSelection()
        self.crossOver()
        self.mutate()

    def sortByScore(self):
        # print("sorting creatures")
        for i in range(0, len(self.creatures)):
            for j in range(i, len(self.creatures)):
                if self.creatures[i].fitnessScore < self.creatures[j].fitnessScore:
                    tempCreature = self.creatures[i]
                    self.creatures[i] = self.creatures[j]
                    self.creatures[j] = tempCreature

        # for i in range(0, len(self.creatures)):
        #     print("DNA: ", self.creatures[i].DNA, " score: ", self.creatures[i].fitnessScore, " rate: ", self.creatures[i].selectionRate, "%")

    def calculateSelectionRate(self):
        for creature in self.creatures:
            creature.selectionRate = r.round(creature.fitnessScore * 100 / self.totalScore)


    def calculateTotalScore(self):
        self.totalScore = 0
        for creature in self.creatures:
            self.totalScore = self.totalScore + creature.fitnessScore
        
        # print("Total score: ", self.totalScore)