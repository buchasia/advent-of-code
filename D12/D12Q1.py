def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    currentDirection = 'E'
    currentEast = 0
    currentNorth = 0
    for line in fileLines:
        line = line.strip('\n')

        if line[0] == 'F':
            [currentEast, currentNorth] = getDistanceUpdate(currentDirection, currentEast, currentNorth, int(line[1:]))
        elif line[0] == 'N':
            currentNorth += int(line[1:])
        elif line[0] == 'S':
            currentNorth -= int(line[1:])
        elif line[0] == 'E':
            currentEast += int(line[1:])
        elif line[0] == 'W':
            currentEast -= int(line[1:])
        else:
            degree = int(line[1:])
            direction = line[0]
            currentDirection = getCurrentDirection(currentDirection, direction, degree)

    return abs(currentEast) + abs(currentNorth)
            
def getDistanceUpdate(direction, currentEast, currentNorth, distance):
    if direction == 'N':
        currentNorth += distance
    elif direction == 'S':
        currentNorth -= distance
    elif direction == 'E':
        currentEast += distance
    elif direction == 'W':
        currentEast -= distance
        
    return [currentEast, currentNorth]

def getCurrentDirection(currentDirection, direction, degree):
    if direction == 'R':
        direction = 'L'
        degree = 360 - degree
    if currentDirection == 'E':
        if direction == 'L' and degree == 90:
            newDirection = 'N'
        elif direction == 'L' and degree == 180:
            newDirection = 'W'
        elif direction == 'L' and degree == 270:
            newDirection = 'S'
        elif direction == 'L' and degree == 360:
            newDirection = 'E'
    elif currentDirection == 'N':
        if direction == 'L' and degree == 90:
            newDirection = 'W'
        elif direction == 'L' and degree == 180:
            newDirection = 'S'
        elif direction == 'L' and degree == 270:
            newDirection = 'E'
        elif direction == 'L' and degree == 360:
            newDirection = 'N'
    elif currentDirection == 'S':
        if direction == 'L' and degree == 90:
            newDirection = 'E'
        elif direction == 'L' and degree == 180:
            newDirection = 'N'
        elif direction == 'L' and degree == 270:
            newDirection = 'W'
        elif direction == 'L' and degree == 360:
            newDirection = 'S'
    elif currentDirection == 'W':
        if direction == 'L' and degree == 90:
            newDirection = 'S'
        elif direction == 'L' and degree == 180:
            newDirection = 'E'
        elif direction == 'L' and degree == 270:
            newDirection = 'N'
        elif direction == 'L' and degree == 360:
            newDirection = 'E'
    return newDirection

print(solveQuestion('InputD12Q1.txt'))
