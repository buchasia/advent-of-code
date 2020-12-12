def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    validCount = 0
    for fileLine in fileLines:
        sides = list(map(int, fileLine.strip('\n').split()))
        sides.sort()
        if sides[0] + sides[1] > sides[2]:
            validCount += 1

    return validCount

print(solveQuestion('InputD03Q1.txt'))
