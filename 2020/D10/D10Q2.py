def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = list(map(int, fileP.readlines()))
    fileP.close()

    # Add Socket
    fileLines.append(0)
    fileLines.sort()

    # Add machine itself
    fileLines.append(fileLines[-1] + 3)
    
    diffOne = 0
    possibility = 1
    for index in range(1, len(fileLines)):
        diff = fileLines[index] - fileLines[index - 1]
        if diff == 1:
            diffOne += 1
        elif diff == 3:
            if diffOne == 2:
                possibility *= 2
            elif diffOne == 3:
                possibility *= 4
            elif diffOne == 4:
                possibility *= 7
            diffOne = 0

    return possibility
        
print(solveQuestion('InputD10Q2.txt'))
