from collections import Counter

def getInput(inputPath):
    fileP = open(inputPath, 'r')
    return [value.strip() for value in fileP.readlines()]

def solvePart1(inputData):

    return ([max([boxId.count(char) == 2  for char in set(boxId)]) for boxId in inputData].count(True) *
            [max([boxId.count(char) == 3 for char in set(boxId)]) for boxId in inputData].count(True))
        
    
def solvePart2(inputData):
    for i in range(len(inputData) - 1):
        for j in range(1, len(inputData)):
            compValue = ''.join([inputData[i][k] if inputData[j][k] == inputData[i][k] else '' for k in range(len(inputData[i]))])
            if len(compValue) == len(inputData[i]) - 1:
                return compValue

def solve(inputPath):
    inputData = getInput(inputPath)
    print(solvePart1(inputData))
    print(solvePart2(inputData))
            
solve('D02.txt')
