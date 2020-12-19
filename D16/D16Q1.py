def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    instructions = fileP.readlines()[0].strip().split(',')
    fileP.close()

    dancePos = 'abcdefghijklmnop'
    dancePos = [char for char in dancePos]
    
    for instruction in instructions:
        if instruction[0] == 's':
            spinVal = int(instruction[1:])
            dancePos = dancePos[(len(dancePos) - spinVal):] + dancePos[:(len(dancePos) - spinVal)]
        elif instruction[0] == 'x':
            [firstPos, secondPos] = list(map(int, instruction[1:].split('/')))
            temp = dancePos[firstPos]
            dancePos[firstPos] = dancePos[secondPos]
            dancePos[secondPos] = temp
        elif instruction[0] == 'p':
            [firstProg, secondProg] = instruction[1:].split('/')
            firstPos = dancePos.index(firstProg)
            secondPos = dancePos.index(secondProg)
            temp = dancePos[firstPos]
            dancePos[firstPos] = dancePos[secondPos]
            dancePos[secondPos] = temp

    return ''.join(dancePos)
      
print(solveQuestion('InputD16Q1.txt'))
