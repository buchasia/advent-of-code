import re
def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    instructions = fileP.readlines()
    fileP.close()

    registers = {}
    sound = 0

    pattern = re.compile('^-?\d+$')
    
    for char in 'abcdefghijklmnopqrstuvwxyz':
        registers[char] = 0
    counter = -1
    while counter < len(instructions):
        counter += 1
        instruction = instructions[counter].strip()
        instVals = instruction.split()
        if instVals[0] == 'set':
            if pattern.match(instVals[2]):
                registers[instVals[1]] = int(instVals[2])
            else:
                registers[instVals[1]] = registers[instVals[2]]
        elif instVals[0] == 'add':
            if pattern.match(instVals[2]):
                registers[instVals[1]] += int(instVals[2])
            else:
                registers[instVals[1]] += registers[instVals[2]]
        elif instVals[0] == 'snd':
            if pattern.match(instVals[1]):
                sound = int(instVals[1])
            else:
                sound = registers[instVals[1]]
        elif instVals[0] == 'mul':
            if pattern.match(instVals[2]):
                registers[instVals[1]] *= int(instVals[2])
            else:
                registers[instVals[1]] *= registers[instVals[2]]
        elif instVals[0] == 'mod':
            if pattern.match(instVals[2]):
                registers[instVals[1]] %= int(instVals[2])
            else:
                registers[instVals[1]] %= registers[instVals[2]]
        elif instVals[0] == 'rcv':
            if pattern.match(instVals[1]) and int(instVals[1]) != 0:
                return sound
            elif registers[instVals[1]] != 0:
                return sound
        elif instVals[0] == 'jgz':
            if pattern.match(instVals[1]) and int(instVals[1]) > 0:
                if pattern.match(instVals[2]):
                    counter += int(instVals[2]) - 1
                else:
                    counter += registers[instVals[2]] - 1
            elif registers[instVals[1]] > 0:
                if pattern.match(instVals[2]):
                    counter += int(instVals[2]) - 1
                else:
                    counter += registers[instVals[2]] - 1
                
print(solveQuestion('InputD18Q1.txt'))
