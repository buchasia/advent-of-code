def solveProblem(inputPath):

    nice = 0
    with open(inputPath) as fileP:
        valueLine = str(fileP.readline()).strip('\n')
        
        while valueLine:
            if checkConditionOne(valueLine) and checkConditionTwo(valueLine):
                nice += 1

            valueLine = str(fileP.readline()).strip('\n')
            
    return nice

def checkConditionOne(value):
    for i in range(len(value) - 3):
        for j in range(i + 2, len(value) - 1):
            if value[i] == value[j] and value[i + 1] == value[j + 1]:
                return True
                
    return False

def checkConditionTwo(value):
    for i in range(len(value) - 2):
        if value[i] == value[i + 2]:
            return True
    return False

print(solveProblem('InputD05Q2.txt'))
