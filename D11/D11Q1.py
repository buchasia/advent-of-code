def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    directions = fileP.readlines()[0].strip().split(',')
    fileP.close()

    currentX = 0
    currentY = 0
    directionSteps = {'n': [0, 2], 'ne': [1, 1], 's': [0, -2], 'se': [1, -1], 'nw': [-1, 1], 'sw': [-1, -1]}
    for direction in directions:
        directionStep = directionSteps[direction]
        currentX += directionStep[0]
        currentY += directionStep[1]

    steps = 0
    while currentX != 0 or currentY != 0:
        if currentX > 0 and currentY >= 0:
            steps += currentX
            currentY -= currentX
            currentX = 0
        elif currentX > 0 and currentY <= 0:
            steps += currentX
            currentY += currentX
            currentX = 0
        elif currentX < 0 and currentY >= 0:
            steps += abs(currentX)
            currentY -= abs(currentX)
            currentX = 0
        elif currentX < 0 and currentY <= 0:
            steps += abs(currentX)
            currentY += abs(currentX)
            currentX = 0
        elif currentX == 0 and currentY > 0:
            steps += currentY // 2
            currentY = 0
        elif currentX == 0 and currentY < 0:
            steps += abs(currentY) // 2
            currentY = 0
        
    return steps
    
    
print(solveQuestion('InputD11Q1.txt'))
