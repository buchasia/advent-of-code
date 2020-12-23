def solveQuestion(inputPath, size):
    
    fileP = open(inputPath, 'r')
    fileLines = list(map(int, fileP.readlines()[0].strip().split(',')))
    fileP.close()

    listN = list(range(size))
    skipSize = 0
    currentPos = 0
    newArray = list(listN)
    for length in fileLines:
        counter = -1
        for index in range(currentPos, currentPos + length // 2):
            counter += 1
            tempVal = newArray[index % len(listN)]
            newArray[index % len(listN)] = newArray[(currentPos + length - counter - 1) % len(listN)]
            newArray[(currentPos + length - counter - 1) % len(listN)] = tempVal
        
        currentPos += length + skipSize
        currentPos %= len(newArray)
        skipSize += 1

    return newArray[0] * newArray[1]
    
print(solveQuestion('InputD10Q1.txt', 256))
