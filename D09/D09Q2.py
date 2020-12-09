def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    currentBuffer = []
    totalBuffer = []
    for valueLine in fileLines:
        valueLine = int(valueLine)
        totalBuffer.append(valueLine)
        if len(currentBuffer) < 25:
            currentBuffer.append(valueLine)
        else:
            found = False
            for number in currentBuffer:
                if (valueLine - number) in currentBuffer and valueLine - number != number:
                    found = True
                    break

            if found == True:
                currentBuffer.append(valueLine)        
                currentBuffer.pop(0)
            else:
                notInSeq = valueLine
                break

    currentStartIndex = 0
    while 1:
        currentEndIndex = currentStartIndex
        currentSum = totalBuffer[currentStartIndex]
        while currentSum < notInSeq and currentEndIndex < len(totalBuffer) - 1:
            currentEndIndex += 1
            currentSum = sum(totalBuffer[currentStartIndex:currentEndIndex])
        if currentSum == notInSeq:
            sortedWeaknessSeq = totalBuffer[currentStartIndex:currentEndIndex]
            sortedWeaknessSeq.sort()
            
            return sortedWeaknessSeq[0] + sortedWeaknessSeq[-1]

        currentStartIndex += 1

print(solveQuestion('InputD09Q2.txt'))
