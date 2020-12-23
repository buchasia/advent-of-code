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
    while len(readInput) < 2020:
        counter += 1
        lastNumber = readInput[counter]
        occu = actualOcc[lastNumber]
        occu.sort()
        if len(occu) >= 2:
            diff = occu[-1] - occu[-2]
            readInput.append(diff)
        else:
            diff = 0
            readInput.append(0)
        if diff in actualOcc:
            actualOcc[diff].append(counter + 1)
        else:
            actualOcc[diff] = [counter + 1]

    return readInput[-1]

print(solveQuestion('InputD15Q1.txt'))
