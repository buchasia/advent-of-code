import timeit
import re
import copy

# This function reads the input file and prepares the data in the needed format
def getInput(inputPath):
    fileP = open(inputPath, 'r')
    regex = re.compile('(?:([\w ]*) (\d*),(\d*)(?: \w* )(\d*),(\d*))')
    return [line for line in regex.findall(''.join([value.strip() for value in fileP.readlines()]))]

# Simulates lighting for part one
def partOne(x, y, lights, action):
    toogle = {1: 0, 0: 1}
    if action == 'toggle':
        lights[(x, y)] = toogle[lights[(x, y)]]
    elif action == 'turn off':
        lights[(x, y)] = 0
    elif action == 'turn on':
        lights[(x, y)] = 1

# Simulates lighting for part two
def partTwo(x, y, lights, action):
    if action == 'toggle':
        lights[(x, y)] += 2
    elif action == 'turn off':
        lights[(x, y)] = max(0, lights[(x, y)] - 1)
    elif action == 'turn on':
        lights[(x, y)] += 1

def findLightPattern(inputData, p2 = True):
    lights = {}
    for line in inputData:
        for x in range(int(line[1]), int(line[3]) + 1):
            for y in range(int(line[2]), int(line[4]) + 1):
                if (x, y) not in lights:
                    lights[(x, y)] = 0
                if p2 == False:
                    partOne(x, y, lights, line[0])
                else:
                    partTwo(x, y, lights, line[0])
                
    return sum(lights.values())
def solveParts(inputData):
    return [
            findLightPattern(inputData, p2 = False),
            findLightPattern(inputData, p2 = True),
           ]

# This function reads the input data in the format that can be used by solvers        
def solve(inputPath):
    inputData = getInput(inputPath)
    print(solveParts(inputData))

#Timer Start
start = timeit.default_timer()

solve("D06.txt")

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
