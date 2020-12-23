def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    earlyTime = int(fileLines[0].strip('\n'))
    
    busIDs = fileLines[1].split(',')

    # Compute the next time they all move out together
    firstBusID = 0
    busMinuteDiff = 0
    multiplier = 1
    currentValue = 0
    for busID in busIDs:
        if busID != 'x':
            busID = int(busID)
            if firstBusID == 0:
                firstBusID = busID
                busMinuteDiff += 1
                currentValue = busID
                multiplier *= busID
                continue
            for i in range(0, busID):
                currentValueNew = currentValue + multiplier * i
                if (currentValueNew + busMinuteDiff) % busID == 0:
                    break
        
            multiplier *= busID
            currentValue = currentValueNew
        busMinuteDiff += 1

    return currentValue

print(solveQuestion('InputD13Q2.txt'))
