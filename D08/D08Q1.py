def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()
    
    accu = 0
    instructions = {}
    counter = 0
    for valueLine in fileLines:
        [instruction, value] = valueLine.strip('\n').split(' ')
        instructions[counter] = [instruction, int(value)]
        counter += 1

    currentIndex = 0
    indexList = []
    while 1:
        if currentIndex in indexList:
            return accu

        indexList.append(currentIndex)
        
        [instruction, value] = instructions[currentIndex]
        if instruction == 'nop':
            currentIndex += 1
        elif instruction == 'acc':
            currentIndex += 1
            accu += value
        elif instruction == 'jmp':
            currentIndex += value
        
        
print(solveQuestion('InputD08Q1.txt'))
