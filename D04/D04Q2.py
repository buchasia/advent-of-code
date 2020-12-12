def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    allAlphas = 'abcdefghijklmnopqrstuvwxyz'
    
    for fileLine in fileLines:
        infos = fileLine.strip('\n').split('-')
        sectorId, checkSum = infos[-1].split('[')
        checkSum = checkSum[:-1]
        sectorId = int(sectorId)

        name = ' '.join(infos[:-1])
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
            actualName = ''
            for char in name:
                if char == ' ':
                    actualName += ' '
                    continue
                actualName += chr((ord(char) - 97 + (sectorId % 26)) % 26 + 97)
        if actualName == 'northpole object storage':
            return sectorId
            

print(solveQuestion('InputD04Q1.txt'))
