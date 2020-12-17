def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = [ int(val.strip()) for val in fileP.readlines()]
    fileP.close()

    currentIndex = 0
    counter = 0

    while currentIndex < len(fileLines):
        counter += 1
        if fileLines[currentIndex] >= 3:
            fileLines[currentIndex] -= 1
            currentIndex += fileLines[currentIndex] + 1
        else:
            fileLines[currentIndex] += 1
            currentIndex += fileLines[currentIndex] - 1

    return counter

print(solveQuestion('InputD05Q1.txt'))
