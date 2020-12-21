import re
def getInput(inputPath):
    fileP = open(inputPath, 'r')
    regex = re.compile('#(\d*) @ (\d*),(\d*): (\d*)x(\d*)')
    return [list(map(int, list(regex.findall(value.strip())[0])))
            for value in fileP.readlines()]

def solvePart1(inputData):
    fabric = {}
    for dataLine in inputData:
        fabric.update({ (i, j):  '*' if (i, j) in fabric else '#'
                for j in range(dataLine[2], dataLine[2] + dataLine[4])
                for i in range(dataLine[1], dataLine[1] + dataLine[3]) })

    return list(fabric.values()).count('*')
    
def solvePart2(inputData):
    pass

def solve(inputPath):
    inputData = getInput(inputPath)
    print(solvePart1(inputData))
    print(solvePart2(inputData))
            
solve('D03.txt')
