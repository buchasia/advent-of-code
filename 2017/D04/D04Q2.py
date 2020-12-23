def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    total = 0
    for line in fileLines:
        allValues = []
        values = line.strip('\n').split()
        for value in values:
            characterList = []
            for char in value:
                characterList.append(char)

            characterList.sort()
            newValue = ''.join(characterList)
            if newValue in allValues:
                break
            allValues.append(newValue)

        if len(allValues) == len(values):
            total += 1

    return total

print(solveQuestion('InputD04Q2.txt'))
