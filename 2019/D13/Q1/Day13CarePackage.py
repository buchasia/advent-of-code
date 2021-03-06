from Program1202 import Program1202
from Operation import Operation

class CarePackageGame:

    def __init__(self, inputPath):
        self.game = {}
        self.inputPath = inputPath


    def getBoard(self):
        program = Program1202(self.inputPath)
        currentX = 0
        currentY = 0
        while not program.isFinished():
            program.run(None)

            currentOutput = Operation.getOutput()
            tiles = len(currentOutput)//3

            for i in range(0, tiles):
                currentX = currentOutput[i * 3]
                currentY = currentOutput[i * 3 + 1]
                tileId = currentOutput[i * 3 + 2]
                self.game[str(currentX) + " " + str(currentY)] = tileId

        return self.game

    def printBoard(self):
        minX = 0
        minY = 0
        maxX = -100
        maxY = -100    

        for coordinates in self.game:
            [x, y] = coordinates.split(" ")
            x = int(x)
            y = int(y)
            if x < minX:
                minX = x
            if y < minY:
                minY = y
            if x > maxX:
                maxX = x
            if y > maxY:
                maxY = y

        xDim = maxX - minX + 1
        yDim = maxY - minY + 1

        print(xDim, yDim)

        signLetters = []
        for i in range(0, yDim):
            signLetters.append([' ']*xDim)

        for coordinates in self.game:
            [x, y] = coordinates.split()
            x = int(x) - minX
            y = int(y) - minY 
    
            tileId = self.game[coordinates]
            if tileId == 0:
                signLetters[y][x] = ' '
            elif tileId == 1:
                signLetters[y][x] = '#'
            elif tileId == 2:
                signLetters[y][x] = 'B'
            elif tileId == 3:
                signLetters[y][x] = '-'
            elif tileId == 4:
                signLetters[y][x] = 'O'

        for i in range(0, yDim):
            print(''.join(signLetters[i]))

    
                

inputPath = 'InputDay13.txt'

robot = CarePackageGame(inputPath)

game = robot.getBoard()

count = 0

for keys in game:
    if game[keys] == 2:
        count += 1

print(count)

robot.printBoard()
