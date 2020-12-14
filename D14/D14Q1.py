def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    currentMemoryMask = ''
    memoryValue = {}
    for line in fileLines:
        line = line.strip('\n')
        if line[:4]== 'mask':
            [mask, initialMemoryMask] = line.split(' = ')
            currentMemoryMask = str(initialMemoryMask)
            currentMemoryMask = currentMemoryMask.replace('X', '0')
            continue
        else:
            [mem, value] = line.split(' = ')
            index = int(mem[4:-1])
            binaryValue = bin(int(value))[2:]
            while len(binaryValue) != len(initialMemoryMask):
                binaryValue = '0' + binaryValue
            counter = 0
            memoryMask = ''
            for bit in currentMemoryMask:
                if initialMemoryMask[counter] == 'X':
                    memoryMask += binaryValue[counter]
                elif initialMemoryMask[counter] != 'X':
                    memoryMask += initialMemoryMask[counter]
                counter += 1

            memoryValue[index] = int(memoryMask, 2)
            currentMemoryMask = str(memoryMask)

    total = 0
    for index in memoryValue:
        total += memoryValue[index]    

    return total
        


print(solveQuestion('InputD14Q1.txt'))
