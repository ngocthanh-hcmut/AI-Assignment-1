from Floor.Floor import Floor
from Floor.NormalFloor import NormalFloor
from Floor.NoneFloor import NoneFloor
from Floor.StartFloor import StartFloor
from Floor.HoleFloor import HoleFloor
from Floor.WeakFloor import WeakFloor
from Floor.CircleToggleFloor import CircleToggleFloor
from Floor.XToggleFloor import XToggleFloor


# Khai báo đối tượng Map: lưu thông tin về bản đồ của màn chơi
class Map:

    def __init__(self, level = 0):
        self.level = level
        self.floors = []
        self.mapWidth = 0
        self.mapHeight = 0
        self.startFloor: StartFloor
        self.holeFloor: HoleFloor
        self.toggleFloors = []
        self.loadMap()

    def loadMap(self):
        # đọc dữ liệu từ file input
        file = open("input/Map/level"+str(self.level)+".txt", "r")
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].split()
        
        # tạo đối tượng floor lưu vào thuộc tính self.floors
        for y in range(len(lines)):
            line = lines[y]
            floorRow = []
            for x in range(len(line)):
                if line[x] == "1":
                    floorRow.append(NormalFloor(x, y))
                if line[x] == "0":
                    floorRow.append(NoneFloor(x, y))
                if line[x] == "s":
                    self.startFloor = StartFloor(x, y)
                    floorRow.append(self.startFloor)
                if line[x] == "h":
                    self.holeFloor = HoleFloor(x, y)
                    floorRow.append(self.holeFloor)
                if line[x] == "w":
                    floorRow.append(WeakFloor(x, y))
                if line[x] == 'c':
                    floor = CircleToggleFloor(x, y, self)
                    floorRow.append(floor)
                    self.toggleFloors.append(floor)
                if line[x] == 'x':
                    floor = XToggleFloor(x, y, self)
                    floorRow.append(floor)
                    self.toggleFloors.append(floor)
            self.floors.append(floorRow)


        # lưu thông tin width và height của map
        self.mapWidth = len(self.floors[0]) * Floor.width
        self.mapHeight = len(self.floors) * Floor.height

    def render(self, screen):
        for floorRow in self.floors:
            for floor in floorRow:
                floor.render(screen)
