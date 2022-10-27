import globalVariable as const
import bricks.brick as br
import bricks.emptyBrick as ebr
import bricks.destinationBrick as dbr

class Map:

    bricks = []
    
    inputMap = open("input/map.txt", "r").readlines()

    def __init__(self, screen):
        self.readinputMap(screen)

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