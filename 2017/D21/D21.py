def getFlip(tile):
    return [tile, tile[::-1], [l[::-1] for l in tile], [l[::-1] for l in tile][::-1]]

def getRotation(tile):
    rotation = [tile]
    currentTile = tile
    newTile = tile
    for i in range(3):
        newTile = [l[:] for l in newTile]
        for x in range(len(tile)):
            for y in range(len(tile)): # Is a square
                newTile[x][y] = currentTile[len(tile) - 1 - y][x]
        currentTile = newTile
        rotation.append(currentTile)
    return rotation

def getPossibles(tile):
    possibleTiles = []
    for flippedTile in getFlip(tile):
        possibleTiles.extend(getRotation(flippedTile))
    output = []
    for possibleTile in possibleTiles:
        if possibleTile not in output:
            output.append(possibleTile)
    return output

def getString(tile):
    string = ''
    for row in tile:
        string += ''.join(row) + '/'

    return string[:-1]

def getOnPixel(tile):
    total = 0
    for line in tile:
        total += line.count('#')
    return total

def printGrid(grid):
    for line in grid:
        print(''.join(line))
    print('')

def performEnhancement(tile, enhancementRules):
    if len(tile) % 2 == 0:
        enhancementSize = 2
    else:
        enhancementSize = 3

    y = - 1 * enhancementSize
    outputGrids = {}
    while y < len(tile) - enhancementSize:
        y += enhancementSize
        x = -1 * enhancementSize
        outputGrids[y // enhancementSize] = {}
        while x < len(tile) - enhancementSize:
            x += enhancementSize

            startX = x
            endX = x + enhancementSize
            startY = y
            endY = y + enhancementSize

            currentGrid = []
            for currentY in range(startY, endY):
                currentGrid.append(tile[currentY][startX:endX])

            outputGrids[y // enhancementSize][x // enhancementSize] = enhancementRules[getString(currentGrid)]
            
    newTile = []
    for y in outputGrids:
        for i in range(len(outputGrids[y][0])):
            newRow = []
            for x in outputGrids[y]:
                 newRow += list(outputGrids[y][x][i])
            newTile.append(newRow)
            
    return newTile
    
INPUT = '''.#.
..#
###'''

def solveQuestion(inputPath, numIteration):
        
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    enhancementRules = {}
    for line in fileLines:
        tileStr, outputStr = line.strip().split(' => ')
        tiles = [list(tile) for tile in tileStr.split('/')]
        outputTiles = [list(outTile) for outTile in outputStr.split('/')]

        possTiles = getPossibles(tiles)
        for possTile in possTiles:
            enhancementRules[getString(possTile)] = outputTiles

    currentTile = [list(l) for l in INPUT.split('\n')]

    counter = 0
    while counter < numIteration:
        counter += 1
        currentTile = performEnhancement(currentTile, enhancementRules)
        
    return getOnPixel(currentTile)
    
print(solveQuestion('InputD21.txt', 5))
print(solveQuestion('InputD21.txt', 18))
