def accMagnitude(accValues):
    return int(accValues[0]) ** 2 + int(accValues[1]) ** 2 + int(accValues[2]) ** 2
def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines= fileP.readlines()
    fileP.close()
    minAcc = 10000
    counter = -1
    for line in fileLines:
        counter += 1
        line = line.strip()
        [otherVal, accText] = line.split('a=<')

        accValues = accMagnitude(list(map(int, accText[:-1].split(','))))
        
        if accValues <= minAcc:
            minAcc = accValues
            minIndex = counter
    return minIndex
        
print(solveQuestion('InputD20Q1.txt'))
