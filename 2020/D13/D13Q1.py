def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    earlyTime = int(fileLines[0].strip('\n'))
    
    busIDs = fileLines[1].split(',')
    minWaitingTime = earlyTime
    minWaitingBusID = 0
    for busID in busIDs:
        if busID != 'x':
            busID = int(busID)
            waitingTime = earlyTime % busID
            if earlyTime % busID == 0:
                return 0
            else:
                waitingTime = busID - waitingTime
                if minWaitingTime > waitingTime:
                    minWaitingTime = waitingTime
                    minWaitingBusID = busID
    return minWaitingBusID * minWaitingTime

print(solveQuestion('InputD13Q1.txt'))
