def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()[0]
    fileP.close()
    directionDict = {'N': {'L':'W', 'R':'E'}, 'S': {'L':'E', 'R':'W'}, 'E': {'L':'N', 'R':'S'}, 'W': {'L':'S', 'R':'N'}}
    distanceSum = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
    currentDirection = 'N'
    currentX = 0
    currentY = 0
    directions = fileLines.strip('\n').split(', ')
    for direction in directions:
        currentDirection = directionDict[currentDirection][direction[0]]
        currentX += distanceSum[currentDirection][0] * int(direction[1:])
        currentY += distanceSum[currentDirection][1] * int(direction[1:])

    return abs(currentX) + abs(currentY)

print(solveQuestion('InputD01Q1.txt'))
