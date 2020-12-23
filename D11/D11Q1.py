def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    newPosition = []

    numRows = len(fileLines)
    numCols = len(fileLines[0].strip('\n'))
    
    for line in fileLines:
        currentLine = []
        for grid in line.strip('\n'):
            currentLine.append(grid)

        newPosition.append(currentLine)

    lastPosition = []
    counter = 0
    while lastPosition != newPosition:
        lastPosition = list(newPosition)
        newPosition =[]
        counter += 1
        for row in range(numRows):
            currentLine = []
            for col in range(numCols):
                if lastPosition[row][col] == '.':
                    currentLine.append('.')
                    continue
                numNeighbors = getNeighbors(lastPosition, row, col, numRows, numCols)
                if numNeighbors == 0 and lastPosition[row][col] == 'L':
                    currentLine.append('#')
                elif numNeighbors >= 4 and lastPosition[row][col] == '#':
                    currentLine.append('L')
                else:
                    currentLine.append(lastPosition[row][col])

            newPosition.append(currentLine)

    totalOccupied = 0
        
    for position in newPosition:
        totalOccupied += ''.join(position).count('#')

    return totalOccupied

def getNeighbors(lastPosition, row, col, maxRow, maxCol):
    indexMove = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    counter = 0
    for index in indexMove:
        rowActual = row + index[0]
        colActual = col + index[1]
        if rowActual < 0 or colActual < 0:
            continue
        if rowActual == maxRow:
            continue
        if colActual == maxCol:
            continue
        if lastPosition[rowActual][colActual] == '#':
            counter += 1

    return counter
    

print(solveQuestion('InputD11Q1.txt'))
