import timeit

# This methods reads the input file and prepares the data in the needed format
def getInput(inputPath):
    fileP = open(inputPath, 'r')
    return [[int(x) for x in line.strip().split(', ')] for line in fileP.readlines()]

def getDistanceList(inputData, x, y):
    return [abs(x - InputX) + abs(y - InputY) for [InputX, InputY] in inputData]

def getClosestPointWithDistanceSum(inputData, x, y):
    distances = getDistanceList(inputData, x, y)
    return [distances.index(min(distances)), sum(distances)]


def solveParts(inputData):

    # We will use the min and max of each axis to compute the next data
    minY = min(inputData, key=lambda inputC: inputC[1])[1]
    maxY = max(inputData, key=lambda inputC: inputC[1])[1]
    minX = min(inputData, key=lambda inputC: inputC[0])[0]
    maxX = max(inputData, key=lambda inputC: inputC[0])[0]

    # Instead of using minX, maxX and minY, maxY in the computing closestMap, we could
    # actually use avgX and avgY and in the case I had we would still get the correct answer
    #avgX, avgY = [avg // len(inputData) for avg in map(sum, zip(*inputData))]
    closestMap = { (x, y): getClosestPointWithDistanceSum(inputData, x, y)
                    for y in range(minY - 200, maxY + 201)
                    for x in range(minX - 200, maxX + 201) }

    # Get the points on the borders, they will have infinite lengths
    infinitePoints = ({closestMap[(x, minY)][0] for x in range(minX, maxX + 1)} |
                      {closestMap[(x, maxY)][0] for x in range(minX, maxX + 1)} |
                      {closestMap[(minX, y)][0] for y in range(minY, maxY + 1)} |
                      {closestMap[(maxX, y)][0] for y in range(minY, maxY + 1)} )

    # Find the coordinate with the maximum number of nearest other coordinates
    part1 = max([list(map(lambda x: x[0], closestMap.values())).count(i)
                 for i in range(len(inputData)) if i not in infinitePoints])

    # Find the total number of coordinates less than a total distance of 10000 from the
    # coordinates in list
    part2 = sum([1 for coordinate in closestMap if closestMap[coordinate][1] < 10000])

    return [part1, part2]

# This method reads the input data in the format that can be used by solvers        
def solve(inputPath):
    inputData = getInput(inputPath)
    print(solveParts(inputData))

#Timer Start
start = timeit.default_timer()

solve("D06.txt")

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
