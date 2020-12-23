def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = [ int(val.strip()) for val in fileP.readlines()[0].strip().split()]
    fileP.close()

    counter = 0
    states = {}
    states[0] = fileLines
    currentValues = list(fileLines)
    while not combinationFound(states):
        counter += 1
        currentValues = list(currentValues)
        maxValue = max(currentValues)
        index = currentValues.index(maxValue)
        currentValues[index] = 0

        while maxValue > 0:
            index += 1
            index %= len(currentValues)
            maxValue -= 1
            currentValues[index] += 1
            
        states[counter] = currentValues
    return counter

def combinationFound(states):
    for i in range(len(states) - 1):
        if states[i] == states[len(states) - 1]:
            return True

    return False


print(solveQuestion('InputD06Q1.txt'))
