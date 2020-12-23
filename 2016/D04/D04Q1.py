def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    allAlphas = 'abcdefghijklmnopqrstuvwxyz'
    
    sumSectorIds = 0
    for fileLine in fileLines:
        infos = fileLine.strip('\n').split('-')
        sectorId, checkSum = infos[-1].split('[')
        checkSum = checkSum[:-1]
        sectorId = int(sectorId)

        name = ''.join(infos[:-1])
        alphaCounts = {}
        for alpha in allAlphas:
            count = name.count(alpha)
            if count != 0:
                if count in alphaCounts:
                    alphaCounts[count].append(alpha)
                else:
                    alphaCounts[count] = [alpha]

        checkString = ''
        for key in sorted(alphaCounts, reverse=True):
            alphas = alphaCounts[key]
            alphas.sort()
            checkString += ''.join(alphas)
            if len(checkString) >= 5:
                checkString = checkString[:5]
                break
        if checkString == checkSum:
            sumSectorIds += sectorId
        
    return sumSectorIds

print(solveQuestion('InputD04Q1.txt'))
