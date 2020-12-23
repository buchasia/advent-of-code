def solveQuestion(inputPath, size):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()[0].strip()
    fileP.close()

    lengths = [ord(char) for char in fileLines]
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
    
print(solveQuestion('InputD10Q2.txt', 256))
