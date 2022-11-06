
# Khai báo đối tượng Map: lưu thông tin về bản đồ của màn chơi
from Square.HideSquare import HideSquare
from Square.Square import Square
from Square.StartSquare import StartSquare
from Square.HoleSquare import HoleSquare
from Square.NormalSquare import NormalSquare
from Square.NoneSquare import NoneSquare
from Square.WeakSquare import WeakSquare
from Square.CircleToggleSquare import CircleToggleSquare
from Square.XToggleSquare import XToggleSquare


class Floor:

    def __init__(self, level = 0):
        self.level = level
        self.squares = []
        self.mapWidth = 0
        self.mapHeight = 0
        self.startSquare: StartSquare
        self.holeSquare: HoleSquare
        self.toggleSquares = []
        self.loadMap()
    
    def reset(self):
        for i in range(len(self.squares)):
            for j in range(len(self.squares[i])):
                if isinstance(self.squares[i][j], HideSquare):
                    # print("reset floor")
                    self.squares[i][j].enabled = self.squares[i][j].enabledAtDefault

    def loadMap(self):
        # đọc dữ liệu từ file input
        file = open("input/Map/level"+str(self.level)+".txt", "r")
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].split()
        
        # tạo đối tượng Square lưu vào thuộc tính self.Squares
        for y in range(len(lines)):
            line = lines[y]
            SquareRow = []
            for x in range(len(line)):    
                if line[x][0] == "1":
                    SquareRow.append(NormalSquare(x, y))
                if line[x][0] == "0":
                    SquareRow.append(NoneSquare(x, y))
                if line[x][0] == "s":
                    self.startSquare = StartSquare(x, y)
                    SquareRow.append(self.startSquare)
                if line[x][0] == "h":
                    self.holeSquare = HoleSquare(x, y)
                    SquareRow.append(self.holeSquare)
                if line[x][0] == "w":
                    SquareRow.append(WeakSquare(x, y))
                if line[x][0] == 'c':
                    square = CircleToggleSquare(x, y)
                    self.toggleSquares.append(square)
                    SquareRow.append(square)
                if line[x][0] == 'x':
                    square = XToggleSquare(x, y)
                    self.toggleSquares.append(square)
                    SquareRow.append(square)
                if line[x][0] == "t":
                    SquareRow.append(HideSquare(x, y, True))
                if line[x][0] == "f":
                    SquareRow.append(HideSquare(x, y, False))

            self.squares.append(SquareRow)
        
        for y in range(len(lines)):
            line = lines[y]
            for x in range(len(line)):
                if len(line[x]) == 2:
                    char = line[x][1]
                    self.squares[y][x].setProperty(char)
                if len(line[x]) >= 3:
                    j = 2
                    while j < len(line[x]):
                        index = int(line[x][j])
                        self.toggleSquares[index].addTarget(self.squares[y][x])
                        j = j + 1


        # lưu thông tin width và height của map
        self.floorWidth = len(self.squares[0]) * Square.width
        self.floorHeight = len(self.squares) * Square.height

    def __eq__(self, other):
        return self.squares == other.squares
        
    def render(self, screen):
        for SquareRow in self.squares:
            for Square in SquareRow:
                Square.render(screen)
