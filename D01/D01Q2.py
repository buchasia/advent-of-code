def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileLines = fileLines[0].strip('\n')
    fileP.close()

    total = 0
    lengthList = len(fileLines)
    for i in range(lengthList):
        valueCurrent = int(fileLines[i])
        valueNext = int(fileLines[(i + (lengthList // 2)) % lengthList])

        if valueCurrent == valueNext:
            total += valueCurrent

    return total

print(solveQuestion('D01.txt'))
