def getInput(inputPath):
    fileP = open(inputPath, 'r')
    return [int(value.strip()) for value in fileP.readlines()]

def solvePart1(inputData):
    return sum(inputData)

def solvePart2(inputData):
    currentSum = 0
    seen = set()
    seen.add(0)
    while 1:
        for value in inputData:
            currentSum += value
            if currentSum in seen:
                return currentSum
            else:
                seen.add(currentSum)

def solve(inputPath):
    inputData = getInput(inputPath)
    print(solvePart1(inputData))
    print(solvePart2(inputData))
            
solve('D01.txt')
