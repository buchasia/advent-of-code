def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    counter = -1
    tileEdges = {}
    while (counter + 1) * 12 <= len(fileLines):
        counter += 1
        [_, tileId] = fileLines[counter * 12].split('Tile ')
        tileId = int(tileId.strip()[:-1])
        tile = [tileLine.strip() for tileLine in fileLines[(counter * 12 + 1):(counter * 12 + 11)]]
        
        addToTileEdge(tileEdges, tile[0], tileId)
        addToTileEdge(tileEdges, tile[0][-1::-1], tileId)
        addToTileEdge(tileEdges, tile[-1], tileId)
        addToTileEdge(tileEdges, tile[-1][-1::-1], tileId)

        edgeLeft = ''
        edgeRight = ''
        for tileEdge in tile:
            edgeLeft += tileEdge[0]
            edgeRight += tileEdge[-1]

        addToTileEdge(tileEdges, edgeLeft, tileId)
        addToTileEdge(tileEdges, edgeLeft[-1::-1], tileId)
        addToTileEdge(tileEdges, edgeRight, tileId)
        addToTileEdge(tileEdges, edgeRight[-1::-1], tileId)

    tileIds = {}
    for tileEdge in tileEdges:
        if len(tileEdges[tileEdge]) == 1:
            if tileEdges[tileEdge][0] not in tileIds:
                tileIds[tileEdges[tileEdge][0]] = [tileEdge]
            else:
                if tileEdge not in tileIds[tileEdges[tileEdge][0]]:
                    if tileEdge[-1::-1] not in tileIds[tileEdges[tileEdge][0]]:
                        tileIds[tileEdges[tileEdge][0]].append(tileEdge)

    total = 1
    for tileId in tileIds:
        if len(tileIds[tileId]) != 1:
            total *= tileId

    return total
              

def addToTileEdge(tileEdges, tileEdge, tileId):
    if tileEdge not in tileEdges and tileEdge[-1::-1] not in tileEdges:
        tileEdges[tileEdge] = [tileId]
    else:
        if tileEdge in tileEdges:
            if tileId not in tileEdges[tileEdge]:
                tileEdges[tileEdge].append(tileId)
        else:
            if tileId not in tileEdges[tileEdge[-1::-1]]:
                tileEdges[tileEdge[-1::-1]].append(tileId)
    
            
        
print(solveQuestion('InputD20Q1.txt'))
