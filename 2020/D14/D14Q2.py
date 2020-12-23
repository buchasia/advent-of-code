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
            continue
        else:
            [mem, value] = line.split(' = ')
            index = int(mem[4:-1])
            value = int(value)
            binaryValue = bin(int(index))[2:]
            while len(binaryValue) != len(initialMemoryMask):
                binaryValue = '0' + binaryValue
            counter = 0
            memoryMask = ''
            for bit in initialMemoryMask:
                if bit == 'X':
                    memoryMask += 'X'
                elif bit == '1':
                    memoryMask += initialMemoryMask[counter]
                else:
                    memoryMask += binaryValue[counter]
                counter += 1

            XCount = memoryMask.count('X')
            counter = 0
            allMemory = [str(memoryMask)]
            while counter < XCount:
                allMemoryNew = []
                for memory in allMemory:
                    indexFirst = memory.find('X')

                    currentStr0 = memory[:indexFirst] + '0' + memory[indexFirst+1:]
                    currentStr1 = memory[:indexFirst] + '1' + memory[indexFirst+1:]

                    allMemoryNew.append(currentStr0)
                    allMemoryNew.append(currentStr1)
                allMemory = list(allMemoryNew)
                counter += 1

            for memory in allMemory:
                index = int(memory, 2)
                memoryValue[index] = value
            
    total = 0
    for index in memoryValue:
        total += memoryValue[index]    

    return total
        


print(solveQuestion('InputD14Q2.txt'))
