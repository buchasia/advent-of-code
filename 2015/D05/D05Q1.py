def solveProblem(inputPath):

    nice = 0
    with open(inputPath) as fileP:
        valueLine = str(fileP.readline()).strip('\n')
        
        while valueLine:
            if checkConditionThree(valueLine) and checkConditionOne(valueLine) and checkConditionTwo(valueLine):
                nice += 1

            valueLine = str(fileP.readline()).strip('\n')
            
    return nice

def checkConditionOne(value):
    counter = value.count('a') + value.count('e')+ value.count('i') + value.count('o') + value.count('u')

    if counter >= 3:
        return True
    return False

def checkConditionTwo(value):
    for i in range(len(value) - 1):
        if value[i] == value[i + 1]:
            return True
    return False

def checkConditionThree(value):
    invalidCombination = ['ab', 'cd', 'pq', 'xy']
    for combination in invalidCombination:
        if combination in value:
            return False

    return True    

print(solveProblem('InputD05Q1.txt'))
