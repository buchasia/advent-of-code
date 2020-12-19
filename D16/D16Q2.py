def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    instructions = fileP.readlines()[0].strip().split(',')
    fileP.close()

    dancePos = 'abcdefghijklmnop'
    dancePos = [char for char in dancePos]
    startPos = list(dancePos)
    counter = -1
    instructs = {}
    for instruction in instructions:
        counter += 1
        if instruction[0] == 's':
            instructs[counter] = {'inst': 's', 'spin': int(instruction[1:])}
        elif instruction[0] == 'x':
            [firstPos, secondPos] = list(map(int, instruction[1:].split('/')))
            instructs[counter] = {'inst': 'x', 'values': [firstPos, secondPos]}
        elif instruction[0] == 'p':
            [firstProg, secondProg] = instruction[1:].split('/')
            instructs[counter] = {'inst': 'p', 'values': [firstProg, secondProg]}

    counter = 0
    while counter < 1000000000:
        counter += 1
        for index in instructs:
            if instructs[index]['inst'] == 's':
                spinVal = instructs[index]['spin']
                dancePos = dancePos[(len(dancePos) - spinVal):] + dancePos[:(len(dancePos) - spinVal)]
            elif instructs[index]['inst'] == 'x':
                [firstPos, secondPos] = instructs[index]['values']
                temp = dancePos[firstPos]
                dancePos[firstPos] = dancePos[secondPos]
                dancePos[secondPos] = temp
            elif instructs[index]['inst'] == 'p':
                [firstProg, secondProg] = instructs[index]['values']
                firstPos = dancePos.index(firstProg)
                secondPos = dancePos.index(secondProg)
                temp = dancePos[firstPos]
                dancePos[firstPos] = dancePos[secondPos]
                dancePos[secondPos] = temp

        if startPos == dancePos:
            counter = 1000000000 - (1000000000 % counter)

    return ''.join(dancePos)
      
print(solveQuestion('InputD16Q2.txt'))
