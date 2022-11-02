from cmath import sqrt
import copy
from time import sleep
from turtle import heading, width
import globalVariable as const
import random
import threading
import pygame

class SquarePrism:

    DnaLength = const.DNA_LENGTH
    MOVE_LEFT = 1
    MOVE_RIGHT = 2
    MOVE_UP = 3
    MOVE_DOWN = 4

    inputMap = None
    scoreMap = None

    solution = None
    win = False

    def __init__(self, inputMap, scoreMap, DNA=None):
        self.color = const.PRISM_COLOR[random.randint(0,len(const.PRISM_COLOR)-1)]

        self.baseBricks = None
        self.inputMap = None
        self.scoreMap = scoreMap

        self.xPos = None
        self.yPos = None
        self.width = None
        self.height = None
   
        self.DNA = DNA if DNA != None else []
        self.DNA = SquarePrism.solution if SquarePrism.solution != None else []
        self.lost = False
        self.age = 0

        self.selectionRate = 0

        self.fitnessScore = 0
        # get map
        if self.inputMap == None:
            self.inputMap = []
            for line in inputMap:
                newLine = [char for char in line]
                self.inputMap.append(newLine)

        # get initial base bricks
        self.baseBricks = const.INITIAL_BASE_BRICKS

        # set x,y,width, height
        self.xPos = None
        self.yPos = None
        if len(self.baseBricks) == 1:
            self.xPos = self.baseBricks[0][0] * const.BRICK_SIZE
            self.yPos = self.baseBricks[0][1] * const.BRICK_SIZE
            self.width = const.BRICK_SIZE
            self.height = const.BRICK_SIZE
        if len(self.baseBricks) == 2:
            self.xPos = min(self.baseBricks[0][0], self.baseBricks[1][0]) * const.BRICK_SIZE
            self.yPos = min(self.baseBricks[0][1], self.baseBricks[1][1]) * const.BRICK_SIZE
            maxX = max(self.baseBricks[0][0], self.baseBricks[1][0]) * const.BRICK_SIZE
            maxY = max(self.baseBricks[0][1], self.baseBricks[1][1]) * const.BRICK_SIZE
            self.width = maxX - self.xPos
            self.height = maxY - self.yPos

        # generate DNA
        if len(self.DNA) == 0:
            for i in range(0, self.DnaLength):
                self.DNA.append(random.randint(1,4));
         
        # print("Initialized prism. DNA: ", self.DNA)

    def moveUp(self):
        tmpBaseBricks = self.baseBricks
        if len(self.baseBricks) == 1:
            currentPosition = self.baseBricks[0]
            newPosition_1 = [currentPosition[0], currentPosition[1] - 1]
            newPosition_2 = [currentPosition[0], currentPosition[1] - 2]
            self.baseBricks = [newPosition_1, newPosition_2]
            
        elif len(self.baseBricks) == 2:
            brick1 = self.baseBricks[0]
            brick2 = self.baseBricks[1]
            if(brick1[0] == brick2[0]):
                y = min(brick1[1], brick2[1])
                newBrick = [brick1[0], y - 1]
                self.baseBricks = [newBrick]
            elif(brick1[1] == brick2[1]):
                brick1[1] = brick1[1] - 1
                brick2[1] = brick2[1] - 1
                self.baseBricks = [brick1, brick2]
            else:
                print("Error 456")
                return
        else:
            print("Error 444")
            return

        thread = threading.Thread(target=self.transition, args=(self.baseBricks,))
        thread.start()
        # wait for transition to complete
        sleep(0.1)
        while thread.is_alive():
            sleep(0.1)    
        # print("position: ", self.baseBricks)
        self.checkGameStatus()
        if self.lost:
            self.baseBricks = tmpBaseBricks

    def moveDown(self):
        tmpBaseBricks = self.baseBricks
        if len(self.baseBricks) == 1:
            currentPosition = self.baseBricks[0]
            newPosition_1 = [currentPosition[0], currentPosition[1] + 1]
            newPosition_2 = [currentPosition[0], currentPosition[1] + 2]
            self.baseBricks = [newPosition_1, newPosition_2]
        
            
        elif len(self.baseBricks) == 2:
            brick1 = self.baseBricks[0]
            brick2 = self.baseBricks[1]
            if(brick1[0] == brick2[0]):
                y = max(brick1[1], brick2[1])
                newBrick = [brick1[0], y + 1]
                self.baseBricks = [newBrick]
            elif(brick1[1] == brick2[1]):
                brick1[1] = brick1[1] + 1
                brick2[1] = brick2[1] + 1
                self.baseBricks = [brick1, brick2]
            else:
                # print("Error 741")
                return
        else:
            # print("Error 555")
            return

        thread = threading.Thread(target=self.transition, args=(self.baseBricks,))
        thread.start()
        # wait for transition to complete
        sleep(0.1)
        while thread.is_alive():
            sleep(0.1)
        # print("position: ", self.baseBricks)
        self.checkGameStatus()
        if self.lost:
            self.baseBricks = tmpBaseBricks

    def moveLeft(self):
        tmpBaseBricks = self.baseBricks
        if len(self.baseBricks) == 1:
            currentPosition = self.baseBricks[0]
            newPosition_1 = [currentPosition[0] - 1, currentPosition[1]]
            newPosition_2 = [currentPosition[0] - 2, currentPosition[1]]
            self.baseBricks = [newPosition_1, newPosition_2]
            
        elif len(self.baseBricks) == 2:
            brick1 = self.baseBricks[0]
            brick2 = self.baseBricks[1]
            if(brick1[0] == brick2[0]):
                brick1[0] = brick1[0] - 1
                brick2[0] = brick2[0] - 1
                self.baseBricks = [brick1, brick2]
            elif(brick1[1] == brick2[1]):
                x = min(brick1[0], brick2[0])
                newBrick = [x-1, brick1[1]]
                self.baseBricks = [newBrick]
            else:
                # print("Error 741")
                return
        else:
            # print("Error 666")
            return

        thread = threading.Thread(target=self.transition, args=(self.baseBricks,))
        thread.start()
        # wait for transition to complete
        sleep(0.1)
        while thread.is_alive():
            sleep(0.1)
        self.checkGameStatus()
        if self.lost:
            self.baseBricks = tmpBaseBricks

    def moveRight(self):
        tmpBasebricks = self.baseBricks
        if len(self.baseBricks) == 1:
            currentPosition = self.baseBricks[0]
            newPosition_1 = [currentPosition[0] + 1, currentPosition[1]]
            newPosition_2 = [currentPosition[0] + 2, currentPosition[1]]
            self.baseBricks = [newPosition_1, newPosition_2]
            
        elif len(self.baseBricks) == 2:
            brick1 = self.baseBricks[0]
            brick2 = self.baseBricks[1]
            if(brick1[0] == brick2[0]):
                brick1[0] = brick1[0] + 1
                brick2[0] = brick2[0] + 1
                self.baseBricks = [brick1, brick2]
            elif(brick1[1] == brick2[1]):
                x = max(brick1[0], brick2[0])
                newBrick = [x+1, brick1[1]]
                self.baseBricks = [newBrick]
            else:
                # print("Error 741")
                return
        else:
            # print("Error 879")
            return

        thread = threading.Thread(target=self.transition, args=(self.baseBricks,))
        thread.start()
        # wait for transition to complete
        sleep(0.1)
        while thread.is_alive():
            sleep(0.1)   
        self.checkGameStatus()
        #undo position if new position make it lost
        if self.lost:
            self.baseBricks = tmpBasebricks

    def render(self, screen):
        if not self.lost:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.xPos, self.yPos, self.width, self.height))

    def thrive(self):
        if self.solution != None:
            self.DNA = self.solution
        # print("Creature begin to thrive. Thread: ", threading.get_ident())
        for i in range(0, len(self.DNA)):
            if self.lost or self.win: break
            # self.calculateFitnessScore()
            if self.DNA[i] == self.MOVE_LEFT:
                thread = threading.Thread(target=self.moveLeft, args=())
                thread.start()
                while thread.is_alive():
                    sleep(0.2)
            if self.DNA[i] == self.MOVE_RIGHT:
                thread = threading.Thread(target=self.moveRight, args=())
                thread.start()
                while thread.is_alive():
                    sleep(0.2)
            if self.DNA[i] == self.MOVE_UP:
                thread = threading.Thread(target=self.moveUp, args=())
                thread.start()
                while thread.is_alive():
                    sleep(0.2)
            if self.DNA[i] == self.MOVE_DOWN:
                thread = threading.Thread(target=self.moveDown, args=())
                thread.start()
                while thread.is_alive():
                    sleep(0.2)
            if not(self.lost) and not(self.win):
                self.age = self.age + 1
        self.calculateFitnessScore()
        
        return

    def mutate(self):
        if self.solution != None:
            return
        position = random.randint(0, len(self.DNA)-1)
        newGen = random.randint(1,4)
        while newGen == self.DNA[position]:
            newGen = random.randint(1, 4)
        self.DNA[position] = newGen

    def gameOver(self):
        self.color = pygame.Color(255, 255, 255)
        sleep(0.1)
        self.lost = True
    
    
    def gameWin(self):
        self.win = True
        self.solution = copy.deepcopy(self.DNA)
    
    def checkGameStatus(self):
        # # print(self.inputMap)
        # # print(self.baseBricks)
        standing = True if len(self.baseBricks) == 1 else False
        for brick in self.baseBricks:
            x = brick[0]
            y = brick[1]
            if x < 0 or x >= len(self.inputMap[0]): 
                # print("Game over")
                self.gameOver()
            elif y < 0 or y >= len(self.inputMap): 
                # print("Game over")
                self.gameOver()
            # check for empty brick
            elif(self.inputMap[y][x] == '0'):
                # print("Game over")
                self.gameOver()
            elif(self.inputMap[y][x] == '9' and standing):
                self.gameWin()

    def transition(self, newBaseBricks):
        newX = None
        newY = None
        newWidth = None
        newHeight = None
        if len(newBaseBricks) == 1:
            newX = newBaseBricks[0][0] * const.BRICK_SIZE
            newY = newBaseBricks[0][1] * const.BRICK_SIZE
            newWidth = const.BRICK_SIZE
            newHeight = const.BRICK_SIZE
        if len(newBaseBricks) == 2:
            newX = min(newBaseBricks[0][0], newBaseBricks[1][0]) * const.BRICK_SIZE
            newY = min(newBaseBricks[0][1], newBaseBricks[1][1]) * const.BRICK_SIZE
            maxNewX = (max(newBaseBricks[0][0], newBaseBricks[1][0]) + 1) * const.BRICK_SIZE
            maxNewY = (max(newBaseBricks[0][1], newBaseBricks[1][1]) + 1) * const.BRICK_SIZE
            newWidth = abs(maxNewX - newX)
            newHeight = abs(maxNewY - newY)

        distanceX = (newX - self.xPos)
        distanceY = (newY - self.yPos)
        deltaWidth = (newWidth - self.width)
        deltaHeight = (newHeight - self.height)

        ax = (2 * distanceX) / (const.MOVE_TIME ** 2)
        ay = (2 * distanceY) / (const.MOVE_TIME ** 2)
        aw = (2 * deltaWidth) / (const.MOVE_TIME ** 2)
        ah = (2 * deltaHeight) / (const.MOVE_TIME ** 2)

        t = 0
        x0 = self.xPos
        y0 = self.yPos
        w0 = self.width
        h0 = self.height
        while t <= const.MOVE_TIME:
            self.xPos = x0 + 0.5 * ax * (t ** 2)
            self.yPos = y0 + 0.5 * ay * (t ** 2)
            self.width = w0 + 0.5 * aw * (t ** 2)
            self.height = h0 + 0.5 * ah * (t ** 2)
            sleep(0.025)
            t = t + 0.025
        self.xPos = x0 + distanceX
        self.yPos = y0 + distanceY
        self.width = w0 + deltaWidth
        self.height = h0 + deltaHeight
        
    # khoảng cách ngắn nhất từ khối trụ tới mục tiêu
    def calculateFitnessScore(self):
        
        # maxScore = len(self.inputMap) + len(self.inputMap[0])
        # destinationBrick = None

        # # find destination brick
        # for i in range(0, len(self.inputMap)):
        #     for j in range(0, len(self.inputMap[0])):
        #         if self.inputMap[i][j] == '9':
        #             destinationBrick = [j, i]

        # #calculate distance
        # a = self.calculateDistance(const.INITIAL_BASE_BRICKS, destinationBrick);
        # goHowFar = self.calculateDistance(self.baseBricks, const.INITIAL_BASE_BRICKS[0], True)
        # reachHowLong = self.calculateDistance(self.baseBricks, destinationBrick)
        # distanceScore = maxScore - reachHowLong

        score = 0
        for brick in self.baseBricks:
            score = score + self.scoreMap[brick[1], brick[0]]
        
        print(self.scoreMap)
        self.fitnessScore = 100
        
        

    def calculateDistance(self, baseBrick, destination, max=False):
        distance = None
        for brick in baseBrick:
            tempDistance = abs(destination[0] - brick[0]) + abs(destination[1] - brick[1])
            if not max:
                distance = tempDistance if distance == None or distance > tempDistance else distance
            else:
                distance = tempDistance if distance == None or distance < tempDistance else distance

        return 2

    def destinationLookable(self, baseBrick, destinationBrick):
        pass