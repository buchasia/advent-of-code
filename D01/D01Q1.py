def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileLines = fileLines[0].strip('\n')
    fileP.close()

    total = 0
    for i in range(len(fileLines)):
        valueCurrent = int(fileLines[i])
        valueNext = int(fileLines[(i + 1) % len(fileLines)])

        if valueCurrent == valueNext:
            total += valueCurrent

    return total

print(solveQuestion('InputD01Q1.txt'))
