import timeit
import re
import copy

# This function reads the input file and prepares the data in the needed format
def getInput(inputPath):
    fileP = open(inputPath, 'r')
    return [line.strip().split() for line in fileP.readlines()]

def assignValue(value, wires, wire):
    if wire in wires:
        return
    if value[0] in '0123456789':
        wires[wire] = int(value)
    else:
        if value in wires:
            wires[wire] = wires[value]

def performInstruction(instruction, wires):
    if instruction[0][0] in '0123456789':
        firstVal = int(instruction[0])
    elif instruction[0] in wires:
        firstVal = wires[instruction[0]]
    else:
        return
    
    if instruction[2][0] in '0123456789':
        secondVal = int(instruction[2])
    elif instruction[2] in wires:
        secondVal = wires[instruction[2]]
    else:
        return

    if instruction[1] == 'OR':
        wires[instruction[4]] = firstVal | secondVal
    elif instruction[1] == 'AND':
        wires[instruction[4]] = firstVal & secondVal
    elif instruction[1] == 'LSHIFT':
        wires[instruction[4]] = firstVal << secondVal
    elif instruction[1] == 'RSHIFT':
        wires[instruction[4]] = firstVal >> secondVal

def processInstructions(inputData, p2 = False, bVal = 0):
    wires = {}
    if p2:
        wires['b'] = bVal
    value16Bit = (1 << 16) - 1
    while len(wires) != len(inputData):
        for instruction in inputData:
            if instruction[-1] in wires:
                continue
            if instruction[1] == '->':
                assignValue(instruction[0], wires, instruction[2])
            elif instruction[0] == 'NOT':
                if instruction[1] in wires:
                    wires[instruction[3]] = value16Bit - wires[instruction[1]]
            else:
                performInstruction(instruction, wires)

    return wires['a']      

def solveParts(inputData):
    aVal = processInstructions(inputData)
    return [
            aVal,
            processInstructions(inputData, p2 = True, bVal = aVal)
           ]

def solve(inputPath):
    inputData = getInput(inputPath)
    print(solveParts(inputData))

#Timer Start
start = timeit.default_timer()

solve("D07.txt")

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
