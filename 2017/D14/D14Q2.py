def knotHash(inputStr, size):
    
    lengths = [ord(char) for char in inputStr]
    lengths.append(17)
    lengths.append(31)
    lengths.append(73)
    lengths.append(47)
    lengths.append(23)

    listN = list(range(size))
    skipSize = 0
    currentPos = 0
    for i in range(64):
        for length in lengths:
            counter = -1
            for index in range(currentPos, currentPos + length // 2):
                counter += 1
                tempVal = listN[index % len(listN)]
                listN[index % len(listN)] = listN[(currentPos + length - counter - 1) % len(listN)]
                listN[(currentPos + length - counter - 1) % len(listN)] = tempVal
        
            currentPos += length + skipSize
            currentPos %= len(listN)
            skipSize += 1

    result = ''
    for index in range(16):
        value = listN[index * 16]
        for indexBlock in range(index * 16 + 1,  (index + 1) * 16):
            value ^= listN[indexBlock]

        hexVal = hex(value)[2:]
        if len(hexVal) == 1:
            hexVal = '0' + hexVal
        result += hexVal

    return result

def solveQuestion(inputS):

    binaryStrings = []

    for i in range(128):
        inputStr = inputS + '-' + str(i)
        hashString = knotHash(inputStr, 256)
        binaryString = ''
        for i in range(32):
            temp = bin(int(hashString[i], 16))[2:]
            binaryString += temp.zfill(4)
        binaryStrings.append(binaryString)
    
    groups = set()
    groupNo = 0
    for i in range(128):
        for j in range(128):
            valueAtIndex = binaryStrings[i][j]
            if valueAtIndex == '0':
                continue
            if (i, j) not in groups:
                groupNo += 1
                groups.add((i, j))
                groups = getGroup((i, j), groups, binaryStrings)
                #print(i, j, groupNo, len(groups))

    return groupNo    

def getGroup(index, groups, binaryStrings):
    indexs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    toVisit = []
    toVisit.append(index)
    counter = 0

    while counter < len(toVisit):
        currentIndex = toVisit[counter]
        for indexi in indexs:
            currentIndexI = currentIndex[0] + indexi[0]
            currentIndexJ = currentIndex[1] + indexi[1]
            if currentIndexI > 127 or currentIndexI < 0 or currentIndexJ > 127 or currentIndexJ < 0:
                continue
            valueAtIndex = binaryStrings[currentIndexI][currentIndexJ]
            if valueAtIndex == '0':
                continue
            if (currentIndexI, currentIndexJ) not in toVisit and (currentIndexI, currentIndexJ) not in groups:
                groups.add((currentIndexI, currentIndexJ))
                toVisit.append((currentIndexI, currentIndexJ))

        counter += 1
    return groups
    
print(solveQuestion('hwlqcszp'))
