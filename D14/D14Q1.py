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
            hexVal += '0'
        result += hexVal

    return result

def solveQuestion(input):
    total = 0
    for i in range(128):
        inputStr = input + '-' + str(i)
        hashString = knotHash(inputStr, 256)
        binaryString = ''
        for i in range(32):
            temp = bin(int(hashString[i], 16))[2:]
            binaryString += temp.zfill(4)

        total += binaryString.count('1')

    return total
    
    
print(solveQuestion('hwlqcszp'))
