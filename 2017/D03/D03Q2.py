def solveQuestion(value):
    currentValue = 0
    x = 0
    y = 0
    currentLine = 1
    values = {}
    values[(0, 0)] = 1
    while value >= currentValue:
        currentLine += 1
        itemsInLine = 8 * currentLine - 8
        x += 1
        for i in range(2 * (currentLine - 1)):
            currentY = y + i
            currentValue = getSum(values, x, currentY)
            values[(x, currentY)] = currentValue
            if currentValue > value:
                return currentValue

        y = currentY
        
        for i in range(1, 2 * (currentLine - 1) + 1):
            currentX = x - i
            currentValue = getSum(values, currentX, y)
            values[(currentX, y)] = currentValue
            if currentValue > value:
                return currentValue

        x = currentX

        for i in range(1, 2 * (currentLine - 1) + 1):
            currentY = y - i
            currentValue = getSum(values, x, currentY)
            values[(x, currentY)] = currentValue
            if currentValue > value:
                return currentValue

        y = currentY
    
        for i in range(1, 2 * (currentLine - 1) + 1):
            currentX = x + i
            currentValue = getSum(values, currentX, y)
            values[(currentX, y)] = currentValue
            if currentValue > value:
                return currentValue

        x = currentX        

def getSum(values, x, y):
    indexDiffs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    total = 0
    for indexDiff in indexDiffs:
        currentX = x + indexDiff[0]
        currentY = y + indexDiff[1]
        if (currentX, currentY) in values:
            total += values[(currentX, currentY)]
    return total

print(solveQuestion(361527))
