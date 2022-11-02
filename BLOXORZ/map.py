import copy
import globalVariable as const
import bricks.brick as br
import bricks.emptyBrick as ebr
import bricks.destinationBrick as dbr

class Map:

    
    inputMap = open("input/map.txt", "r").readlines()
    bricks = []
    scoreMap = []

    def __init__(self, screen):
        self.readinputMap(screen)
        self.generateScoreMap()
        des = self.getDestinationBrick()
        score = self.getMaxScore(const.INITIAL_BASE_BRICKS[0])
        self.setScoreMap(des[0], des[1], score)

    def readinputMap(self, screen):
        for i in range(0, len(self.inputMap)):
            # loại bỏ ký tự xuống dòng
            self.inputMap[i] = self.inputMap[i].strip()
            brickRows = []
            for j in range(0, len(self.inputMap[i])):
                if self.inputMap[i][j] == "1":
                    brickRows.append(br.Brick(j, i, screen))
                if self.inputMap[i][j] == "0":
                    brickRows.append(ebr.EmptyBrick(j, i, screen))
                if self.inputMap[i][j] == "9":
                    brickRows.append(dbr.DestinationBrick(j, i, screen))
            self.bricks.append(brickRows)
    
    def render(self, screen):
        for brickRow in self.bricks:
            for brick in brickRow:
                brick.render(screen)

    def getDestinationBrick(self):
        for i in range(len(self.inputMap)):
            for j in range(len(self.inputMap[0])):
                if self.inputMap[i][j] == "9":
                    return [i, j]
    
    def getMaxScore(self, input):
        des = self.getDestinationBrick()
        return abs(input[0] - des[0]) + abs(input[1] - des[1])

    def generateScoreMap(self):
        for row in self.inputMap:
            scoreRow = []
            for item in self.inputMap[0]:
                scoreRow.append(-1)
            self.scoreMap.append(scoreRow)

    def setScoreMap(self, i, j, score):
        if i < 0 or j < 0 or i >= len(self.inputMap[0]) or j >= len(self.inputMap):
            return
        score = 0 if score < 0 else score
        self.scoreMap[i][j] = score
        if self.scoreMap[i+1][j] != -1:
            self.setScoreMap(i+1, j, score-5)

        if self.scoreMap[i-1][j] != -1:
            self.setScoreMap(i-1, j, score-5)

        if self.scoreMap[i][j+1] != -1:
            self.setScoreMap(i, j+1, score-5)

        if self.scoreMap[i][j-1] != -1:
            self.setScoreMap(i, j-1, score-5)