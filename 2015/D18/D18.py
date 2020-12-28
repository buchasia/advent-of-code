import timeit
import copy

def getInput(inputPath):
    fileP = open(inputPath, 'r')
    return [[0 if light == '.' else 1 for light in line.strip()]for line in fileP.readlines()]

def getNeighborsOn(lighting, x, y):
    offsets = [[1, 1], [1, 0], [1, -1], [0, 1], [-1, -1], [-1, 0], [0, -1], [-1, 1]]
    neighborsOn = 0
    for offset in offsets:
        currentX = x + offset[0]
        currentY = y + offset[1]
        if currentX < 0 or currentX >= len(lighting) or currentY < 0 or currentY >= len(lighting):
            continue
        if lighting[currentX][currentY] == 1:
            neighborsOn += 1
    return neighborsOn
        
def simulateLights(inputData, numSteps = 100, isP2 = False):
    currentLight = copy.deepcopy(inputData)
    if isP2:
        currentLight[0][0], currentLight[0][-1], currentLight[-1][0], currentLight[-1][-1]  = 1, 1, 1, 1
    for i in range(numSteps):
        lastLight = copy.deepcopy(currentLight)
        currentLight = copy.deepcopy(lastLight)
        for x in range(len(currentLight)):
            for y in range(len(currentLight)):
                if isP2 and (x, y) in [(0, 0), (0, len(inputData) - 1), (len(inputData) - 1, 0), (len(inputData) - 1, len(inputData) - 1)]:
                    continue
                neighborsOn = getNeighborsOn(lastLight, x, y)
                if lastLight[x][y] == 1 and (neighborsOn < 2 or neighborsOn > 3):
                    currentLight[x][y] = 0
                elif lastLight[x][y] == 0 and neighborsOn == 3:
                    currentLight[x][y] = 1
    return currentLight

def solve(inputPath):
    inputData = getInput(inputPath)
    print([sum([sum(line) for line in simulateLights(inputData)]),
           sum([sum(line) for line in simulateLights(inputData, 100, True)])])

#Timer Start
start = timeit.default_timer()

solve('D18.txt')

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
