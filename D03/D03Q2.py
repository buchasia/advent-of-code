def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    validCount = 0
    sidesList = []
    for fileLine in fileLines:
        sides = list(map(int, fileLine.strip('\n').split()))
        sidesList.append(sides[0])
        sidesList.append(sides[1])
        sidesList.append(sides[2])

    triangleCount = len(sidesList) // 9

    for triangle in range(triangleCount):
        baseIndex = triangle * 9
        for i in range(3):
            sides = []
            sides.append(sidesList[baseIndex + i])
            sides.append(sidesList[baseIndex + i + 3])
            sides.append(sidesList[baseIndex + i + 6])
            sides.sort()
            if sides[0] + sides[1] > sides[2]:
                validCount += 1

    return validCount

print(solveQuestion('InputD03Q1.txt'))
