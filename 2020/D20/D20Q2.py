import math

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

def getBorders(tile):
    return (tile[0], [line[-1] for line in tile], tile[-1], [line[0] for line in tile])
            #Up      #Right                       #Down      #Left

def getPuzzle(puzzle, tileBorderPoss, dimension, processed = set(), x = 0, y = 0):
    if y == dimension:
        return puzzle

    #print(x, y, puzzle)
    
    nextX = x + 1
    nextY = y

    if nextX == dimension:
        nextX = 0
        nextY += 1

    for tileId in tileBorderPoss:
        if tileId in processed:
            continue
        
        processed.add(tileId)
        for transformationId in tileBorderPoss[tileId]:
            top, right, bottom, left = tileBorderPoss[tileId][transformationId]

            if x > 0:
                neighbourId, neighbourTransformId = puzzle[x - 1][y]
                topN, rightN, bottomN, leftN = tileBorderPoss[neighbourId][neighbourTransformId]
                if rightN != left:
                    continue
            if y > 0:
                neighbourId, neighbourTransformId = puzzle[x][y - 1]
                topN, rightN, bottomN, leftN = tileBorderPoss[neighbourId][neighbourTransformId]
                if top != bottomN:
                    continue

            puzzle[x][y] = (tileId, transformationId)
            tempPuzzle = getPuzzle(puzzle, tileBorderPoss, dimension, processed = processed, x = nextX, y = nextY)
            if tempPuzzle is not None:
                return tempPuzzle
        processed.remove(tileId)

    puzzle[x][y] = None
    return None

def getCountWODragon(tilePoss, puzzle):
    dragon = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']
    dragonIndex = []
    for y in range(len(dragon)):
        for x in range(len(dragon[y])):
            if dragon[y][x] == '#':
                dragonIndex.append((y, x))

    maxX = len(dragon[0]) - 1 # Because in the seocnd line the monster is till the end
    maxY = len(dragon) - 1 # because the monster is present in all lines

    puzzleFinal = removeBorders(tilePoss, puzzle)
    
    # We need to get all possible rotation for our Puzzle
    puzzleFinalPoss = getPossibles(puzzleFinal)
    
    countTotal = 0
    for possible in puzzleFinalPoss:
        countDragons = 0
        for y in range(len(possible)):
            if y + maxY >= len(possible):
                break
            for x in range(len(possible[y])):
                if x + maxX >= len(possible[y]):
                    break
                isDragon = True
                for index in dragonIndex:
                    if possible[y + index[0]][x + index[1]] != '#':
                        isDragon = False
                        break
                if isDragon:
                    countDragons += 1
        
        if countDragons != 0:
            for line in possible:
                countTotal += line.count('#')

            countTotal -= countDragons * 15 # Total occupied by monster, did not want to write code for this
            return countTotal

def removeBorders(tilePoss, puzzle):
    tilePossWOBorder = []
    for column in puzzle:
        columnTiles = []
        # Get all tiles in the row, they represent columns of the puzzle
        for tileId, tileTransformationId in column:
            currentTile = tilePoss[tileId][tileTransformationId]
            columnTile = []
            for i in range(1, len(currentTile) - 1):
                columnTile.append(currentTile[i][1:-1])

            columnTiles.append(columnTile)

        # Get all tiles in a single row
        for y in range(len(columnTiles[0][0])):
            newExtendedRow = []
            for index in range(len(columnTiles)):
                for x in range(len(columnTiles[index])):
                    newExtendedRow.append(columnTiles[index][x][y])

            tilePossWOBorder.append(newExtendedRow)
    return tilePossWOBorder

def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    counter = -1
    tiles = {}
    while (counter + 1) * 12 <= len(fileLines):
        counter += 1
        [_, tileId] = fileLines[counter * 12].split('Tile ')
        tileId = int(tileId.strip()[:-1])
        tile = [tileLine.strip() for tileLine in fileLines[(counter * 12 + 1):(counter * 12 + 11)]]
        tile = [list(l) for l in tile]

        tiles[tileId] = tile

    dimension = math.isqrt(len(tiles))

    tilePoss = {id: getPossibles(tile) for id, tile in tiles.items()}
    tileBorderPoss = {}
    
    for tileId in tilePoss:
        for index, tile in enumerate(tilePoss[tileId]):
            if tileId not in tileBorderPoss:
                tileBorderPoss[tileId] = {}
            tileBorderPoss[tileId][index] = getBorders(tile)

    # This will hold the arranged puzzle
    puzzle = [[None] * dimension for i in range(dimension)]

    puzzle = getPuzzle(puzzle, tileBorderPoss, dimension)        

    return getCountWODragon(tilePoss, puzzle)    
    
print(solveQuestion('InputD20Q2.txt'))
