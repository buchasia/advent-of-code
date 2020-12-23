def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    registers = {}
    maxValue = -1
    for line in fileLines:
        [register, operation, value, ifStr, conditionRegister, condOperator, valueCondition] = line.strip().split()
        value = int(value)
        valueCondition = int(valueCondition)
        if conditionRegister in registers:
            checkValue = registers[conditionRegister]
        else:
            registers[conditionRegister] = 0
            checkValue = 0

        if condOperator == '>':
            if checkValue <= valueCondition:
                value = 0
        elif condOperator == '==':
            if checkValue != valueCondition:
                value = 0
        elif condOperator == '<':
            if checkValue >= valueCondition:
                value = 0
        elif condOperator == '<=':
            if checkValue > valueCondition:
                value = 0
        elif condOperator == '>=':
            if checkValue < valueCondition:
                value = 0
        elif condOperator == '!=':
            if checkValue == valueCondition:
                value = 0

        if operation == 'inc':
            if register in registers:
                registers[register] += value
            else:
                registers[register] = value
        elif operation == 'dec':
            if register in registers:
                registers[register] -= value
            else:
                registers[register] = -1 * value
        if maxValue < registers[register]:
            maxValue = registers[register]
    return maxValue
    
print(solveQuestion('InputD08Q2.txt'))
