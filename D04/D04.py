import re
def getInput(inputPath):
    fileP = open(inputPath, 'r')
    regex = re.compile('(?:\d*:\d*[\] \w]*#)(\d*)|(?:\d*:(\d*)[\[\] \w]*\d*-\d*-\d* \d*:(\d*))')
    return [[int(value) if value != '' else 0 for value in line] for line in regex.findall(''.join(sorted([value.strip() for value in fileP.readlines()])))]

def solveParts(inputData):

    guardSleep = {}
    for data in inputData:
        # This is the guard number
        if data[1] == 0 and data[2] == 0:
            guardId = data[0]
            if guardId not in guardSleep:
                guardSleep[guardId] = {}
            continue
        if data[0] == 0:
            guardSleep[guardId].update({ i: guardSleep[guardId][i] + 1
                                         if i in guardSleep[guardId] else 1
                                         for i in range(data[1], data[2])})

    guardSleepDet = {guard: {'total': sum(guardSleep[guard].values()),
                             'maxTimes': max(guardSleep[guard].values()),
                    'maxMin': list(guardSleep[guard].keys())[(list(guardSleep[guard].values()) + [0]).index(max(list(guardSleep[guard].values()) + [0]))]}
                    for guard in guardSleep if guardSleep[guard] != {}}

    strategyOneGuard = sorted(guardSleepDet, reverse=True, key= lambda item: guardSleepDet[item]['total'])[0]
    strategyTwoGuard = sorted(guardSleepDet, reverse=True, key= lambda item: guardSleepDet[item]['maxTimes'])[0]

    return [strategyOneGuard * guardSleepDet[strategyOneGuard]['maxMin'], strategyTwoGuard * guardSleepDet[strategyTwoGuard]['maxMin']]
                
def solve(inputPath):
    inputData = getInput(inputPath)
    print(solveParts(inputData))
            
solve('D04.txt')
