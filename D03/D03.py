import re
def getInput(inputPath):
    fileP = open(inputPath, 'r')
    regex = re.compile('#(\d*) @ (\d*),(\d*): (\d*)x(\d*)')
    return [list(map(int, list(regex.findall(value.strip())[0])))
            for value in fileP.readlines()]

def solveParts(inputData):
    fabric = {}
    for dataLine in inputData:
        fabric.update({ (i, j):  '*' if (i, j) in fabric else '#'
                for j in range(dataLine[2], dataLine[2] + dataLine[4])
                for i in range(dataLine[1], dataLine[1] + dataLine[3]) })

    for dataLine in inputData:
        nonOverLapId = dataLine[0] if sum([1 if fabric[(i, j)] == '*' else 0
                               for j in range(dataLine[2], dataLine[2] + dataLine[4])
                               for i in range(dataLine[1], dataLine[1] + dataLine[3])]) == 0 else -1

        if nonOverLapId != -1:
            break                  
    return [list(fabric.values()).count('*'), nonOverLapId]
    
def solve(inputPath):
    inputData = getInput(inputPath)
    print(solveParts(inputData))
            
solve('D03.txt')
