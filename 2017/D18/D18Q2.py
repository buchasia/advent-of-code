def get(s, register):
    if s in 'abcdefghijklmnopqrstuvwxyz':
        return register[s]
    return int(s)    

def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    instVals = [line.split() for line in fileP.read().strip().split("\n")]
    fileP.close()

    registers = {}
    registers[0] = {}
    registers[1] = {}
    for char in 'abcdefghijklmnopqrstuvwxyz':
        registers[0][char] = 0
        registers[1][char] = 0

    registers[1]['p'] = 1

    indexs = [0, 0]
    sentData = [[], []]
    state = ['ok', 'ok']

    programId = 0
    register = registers[programId]
    index = indexs[programId]

    total = 0
    
    while True:
        if instVals[index][0] == 'set':
            register[instVals[index][1]] = get(instVals[index][2], register)
        elif instVals[index][0] == 'add':
            register[instVals[index][1]] += get(instVals[index][2], register)
        elif instVals[index][0] == 'snd':
            if programId == 1:
                total += 1
            sentData[programId].append(get(instVals[index][1], register))

        elif instVals[index][0] == 'mul':
            register[instVals[index][1]] *= get(instVals[index][2], register)
        elif instVals[index][0] == 'mod':
            register[instVals[index][1]] %= get(instVals[index][2], register)
        elif instVals[index][0] == 'rcv':
            if sentData[1 - programId]: # the other program has sent data
                state[programId] = 'ok'
                register[instVals[index][1]] = sentData[1 - programId].pop(0)
            else: # Switch to other prog
                if state[1 - programId] == 'done':
                    break
                if len(sentData[programId]) == 0 and state[1 - programId] == 'r':
                    break
                indexs[programId] = index
                state[programId] = 'r'
                programId = 1 - programId
                index = indexs[programId] - 1
                register = registers[programId]
        elif instVals[index][0] == 'jgz':
            if get(instVals[index][1], register) > 0:
                index += get(instVals[index][2], register) - 1
                
        index += 1
        
        if not 0 <= index < len(instVals):
            if state[1 - programId] == 'done':
                break
            state[programId] = 'done'
            indexs[programId] = index
            programId = 1 - programId
            index = indexs[programId]
            register = registers[programId]
            
    return total
print(solveQuestion('InputD18Q2.txt'))
