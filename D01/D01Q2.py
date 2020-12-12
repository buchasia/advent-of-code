def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()[0]
    fileP.close()
    directionDict = {'N': {'L':'W', 'R':'E'}, 'S': {'L':'E', 'R':'W'}, 'E': {'L':'N', 'R':'S'}, 'W': {'L':'S', 'R':'N'}}
    distanceSum = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
    rangeStep = {1: 1, 0: -1}
    currentDirection = 'N'
    currentX = 0
    currentY = 0
    directions = fileLines.strip('\n').split(', ')
    visitedLocations = []
    for direction in directions:
        currentDirection = directionDict[currentDirection][direction[0]]
        oldX = currentX
        oldY = currentY
        currentX += distanceSum[currentDirection][0] * int(direction[1:])
        currentY += distanceSum[currentDirection][1] * int(direction[1:])

        if oldX == currentX:
            step = rangeStep[int(currentY > oldY)]
            counter = 0
            for i in range(oldY, currentY + step, step):
                if counter == 0:
                    counter += 1
                    continue
                if (oldX, i) not in visitedLocations:
                    visitedLocations.append((oldX, i))
                else:
                    return abs(oldX) + abs(i)
        elif oldY == currentY:
            step = rangeStep[int(currentX > oldX)]
            counter = 0
            for i in range(oldX, currentX + step, step):
                if counter == 0:
                    counter += 1
                    continue
                if (i, oldY) not in visitedLocations:
                    visitedLocations.append((i, oldY))
                else:
                    return abs(i) + abs(oldY)
        
print(solveQuestion('InputD01Q1.txt'))
