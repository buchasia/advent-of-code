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
    diffThree = 0
    for index in range(1, len(fileLines)):
        diff = fileLines[index] - fileLines[index - 1]
        if diff == 1:
            diffOne += 1
        elif diff == 3:
            diffThree += 1

    return diffOne * diffThree
        
print(solveQuestion('InputD10Q1.txt'))
