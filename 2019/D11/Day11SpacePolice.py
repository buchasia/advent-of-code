from Program1202 import Program1202
from Operation import Operation

class Robot:

    def __init__(self, inputPath):
        self.gridTravelled = {}
        self.inputPath = inputPath


    def printNumber(self, initialValue):
        program = Program1202(self.inputPath)
        currentX = 0
        currentY = 0
        currentKey = str(currentX) + " " + str(currentY)
        self.gridTravelled[currentKey] = initialValue
        currentDirection = 'U'
        while not program.isFinished():
            currentKey = str(currentX) + " " + str(currentY)
            if currentKey in self.gridTravelled:
                initialValue = self.gridTravelled[currentKey]
            else:
                self.gridTravelled[currentKey] = 0
                initialValue = 0

            program.run(initialValue)

            currentOutput = Operation.getOutput()

            color = currentOutput[0]

            # update the color of the current coordinate in grid
            self.gridTravelled[str(currentX) + " " + str(currentY)] = color

            newDirection = currentOutput[1]
            
            currentDirection = self.getNewDirection(currentDirection, newDirection)

            [currentX, currentY] = self.getNewCurrentXY(currentX, currentY, currentDirection)
            
            Operation.initializeOutput()

        return self.gridTravelled
            
    def getNewCurrentXY(self, x, y, direction):
        if direction == 'U':
            return [x, y + 1]
        elif direction == 'D':
            return [x, y - 1]
        elif direction == 'R':
            return [x + 1, y]
        else:
            return [x - 1, y]
        
    def getNewDirection(self, currentDirection, newDirection):
        if currentDirection == 'U':
            if newDirection == 0:
                currentDirection = 'L'
            else:
                currentDirection = 'R'
        elif currentDirection == 'D':
            if newDirection == 0:
                currentDirection = 'R'
            else:
                currentDirection = 'L'
        elif currentDirection == 'L':
            if newDirection == 0:
                currentDirection = 'D'
            else:
                currentDirection = 'U'
        else:
            if newDirection == 0:
                currentDirection = 'U'
            else:
                currentDirection = 'D'
        return currentDirection

inputPath = 'InputDay11.txt'

robot = Robot(inputPath)
## Question 1
#initialValue = 0
#coordinatesWithColor = robot.printNumber(initialValue)
#print(len(coordinatesWithColor))

## Question 2
initialValue = 1
coordinatesWithColor = robot.printNumber(initialValue)

minX = 0
minY = 0
maxX = -100
maxY = -100    

for coordinates in coordinatesWithColor:
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

for coordinates in coordinatesWithColor:
    [x, y] = coordinates.split()
    x = int(x) - minX
    y = int(y) - minY 
    
    color = coordinatesWithColor[coordinates]
    if coordinatesWithColor[coordinates] == 1:
        signLetters[y][x] = '#'

for i in range(yDim - 1, -1, -1):
    print(''.join(signLetters[i]))

    
    
