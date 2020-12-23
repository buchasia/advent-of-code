def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    total = 0
    for line in fileLines:
        allValues = []
        values = line.strip('\n').split()
        for value in values:
            if value in allValues:
                break
            allValues.append(value)

        if len(allValues) == len(values):
            total += 1

    return total

print(solveQuestion('InputD04Q1.txt'))
