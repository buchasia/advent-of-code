def get(s, register):
    if s in 'abcdefghijklmnopqrstuvwxyz':
        return register[s]
    return int(s)    

def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    instVals = [line.split() for line in fileP.read().strip().split("\n")]
    fileP.close()

    register = {}
    for char in 'abcdefgh':
        register[char] = 0

    index = 0
    total = 0
    while True:
        if instVals[index][0] == 'set':
            register[instVals[index][1]] = get(instVals[index][2], register)
        elif instVals[index][0] == 'sub':
            register[instVals[index][1]] -= get(instVals[index][2], register)
        elif instVals[index][0] == 'mul':
            register[instVals[index][1]] *= get(instVals[index][2], register)
            total += 1
        elif instVals[index][0] == 'jnz':
            if get(instVals[index][1], register) != 0:
                index += get(instVals[index][2], register) - 1
                
        index += 1
        
        if not 0 <= index < len(instVals):
            break

    return total
print(solveQuestion('InputD23.txt'))
