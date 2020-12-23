def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    possibleIndex = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if i == 0 and j == 0 and k == 0:
                    continue
                possibleIndex.append([i, j, k])

    currentState = {}
    z = 0
    y = -1
    for line in fileLines:
        line = line.strip()
        y += 1
        x = -1
        for state in line:
            x += 1
            if state == '.':
                currentState[(x, y, z)] = '.'
            else:
                currentState[(x, y, z)] = '#'
    cycle = 0
    currentX = x
    currentY = y
    currentZ = 0
    while cycle < 6:
        cycle += 1
        previousState = dict(currentState)
        currentX += 1
        currentY += 1
        currentZ += 1

        for x in range(-1 * cycle, currentX + 1):
            for y in range(-1 * cycle, currentY + 1):
                for z in range(-1 * cycle, currentZ + 1):
                    count = 0
                    for index in possibleIndex:
                        checkIndexX = x + index[0]
                        checkIndexY = y + index[1]
                        checkIndexZ = z + index[2]

                        if (checkIndexX, checkIndexY, checkIndexZ) in previousState:
                            if previousState[(checkIndexX, checkIndexY, checkIndexZ)] == '#':
                                count += 1
                    if (x, y, z) in previousState:
                        if previousState[(x, y, z)] == '#' and (count == 2 or count == 3):
                            currentState[(x, y, z)] = '#'
                        elif previousState[(x, y, z)] == '.' and count == 3:
                            currentState[(x, y, z)] = '#'
                        else:
                            currentState[(x, y, z)] = '.'
                    else:
                        if count == 3:
                            currentState[(x, y, z)] = '#'
                        else:
                            currentState[(x, y, z)] = '.'

    total = 0
    for index in currentState:
        if currentState[index] == '#':
            total += 1

    return total
    
        
print(solveQuestion('InputD17Q1.txt'))
