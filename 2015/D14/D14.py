import timeit
import re

# This function reads the input file and prepares the data in the needed format
def getInput(inputPath):
    fileP = open(inputPath, 'r')
    regEx = re.compile('(\w*)[ a-z*]+(\d*) km\/s for (\d*)[ \w,]+ (\d*) seconds.')
    return [line for line in regEx.findall(''.join(fileP.readlines()))]

def simulateRace(inputData, isP2 = False, seconds = 2503):
    resting = {}
    for i in range(seconds):
        if i == 0:
            running = {info[0]: int(info[2]) for info in inputData}
            distance = {info[0]: 0 for info in inputData}
            points = {info[0]: 0 for info in inputData}
        for info in inputData:
            if info[0] in resting:
                resting[info[0]] -= 1
                if resting[info[0]] == 0:
                    del resting[info[0]]
                    running[info[0]] = int(info[2])
            elif info[0] in running:
                running[info[0]] -= 1
                distance[info[0]] += int(info[1])
                if running[info[0]] == 0:
                    del running[info[0]]
                    resting[info[0]] = int(info[3])
        if isP2:
            maxDistance = max(distance.values())
            for deer in distance:
                points[deer] += 1 if distance[deer] == maxDistance else 0

    if isP2:
        return sorted(points.values())[-1]
    else:
        return sorted(distance.values())[-1]

def solve(inputPath):
    inputData = getInput(inputPath)

    print([simulateRace(inputData),
           simulateRace(inputData, isP2 = True)])

#Timer Start
start = timeit.default_timer()

solve("D14.txt")

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
