def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    readInput = list(map(int, fileLines[0].strip('\n').split(',')))

    counter = -1
    lastNumber = -1
    actualOcc = {}
    for readNumber in readInput:
        counter += 1
        if readNumber not in actualOcc:
            actualOcc[readNumber] = [counter]
        else:
            acutalOcc[readNumber].append(counter)

    counter = len(readInput) - 2
    while len(readInput) < 30000000:
        counter += 1
        lastNumber = readInput[counter]
        occu = actualOcc[lastNumber]
        if len(occu) >= 2:
            diff = occu[1] - occu[0]
            readInput.append(diff)
        else:
            diff = 0
            readInput.append(0)
        if diff in actualOcc:
            currentOcc = actualOcc[diff]
            newOcc = [currentOcc[-1], counter + 1]
            actualOcc[diff] = newOcc
        else:
            actualOcc[diff] = [counter + 1]

    return readInput[-1]

print(solveQuestion('InputD15Q2.txt'))
