def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()
    
    instructions = {}
    toChangeInstructions = []
    counter = 0
    for valueLine in fileLines:
        [instruction, value] = valueLine.strip('\n').split(' ')
        instructions[counter] = [instruction, int(value)]
        if instruction == 'nop' or instruction == 'jmp':
            toChangeInstructions.append(counter)
        counter += 1

    counter = 0
    for index in toChangeInstructions:
        changedInstructions = dict(instructions)
        [instruction, value] = changedInstructions[index]
        if instruction == 'nop':
            instruction = 'jmp'
        else:
            instruction = 'nop'

        changedInstructions[index] = [instruction, value]
        currentIndex = 0
        indexList = []
        accu = 0
        while 1:
            if currentIndex in indexList:
                counter += 1
                accu = 0
                break

            if currentIndex == len(changedInstructions):
                break
                
            indexList.append(currentIndex)
        
            [instruction, value] = changedInstructions[currentIndex]
            if instruction == 'nop':
                currentIndex += 1
            elif instruction == 'acc':
                currentIndex += 1
                accu += value
            elif instruction == 'jmp':
                currentIndex += value
        if accu != 0:
            return accu

        
print(solveQuestion('InputD08Q2.txt'))
