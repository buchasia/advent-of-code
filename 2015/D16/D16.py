import timeit
import re

def getInput(inputPath):
    fileP = open(inputPath, 'r')
    regEx = re.compile('Sue (\d*): (\w*): (\d*), (\w*): (\d*), (\w*): (\d*)')
    auntInfo = {}
    for line in regEx.findall(''.join(fileP.readlines())):
        auntInfo[int(line[0])] = {line[i]: int(line[i + 1]) for i in range(1, len(line), 2)}
    return auntInfo

correctAuntSue = { 'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
                   'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1 }

def getCorrectAunty(auntInfo, isP2 = False):
    for auntyNo in auntInfo:
        notFound = False
        for feature in auntInfo[auntyNo]:
            if isP2 and feature in ['cats', 'trees', 'pomeranians', 'goldfish']:
                if feature in ['cats', 'trees']:
                    if auntInfo[auntyNo][feature] <= correctAuntSue[feature]:
                        notFound = True
                else:
                    if auntInfo[auntyNo][feature] >= correctAuntSue[feature]:
                        notFound = True
            else:
                if correctAuntSue[feature] != auntInfo[auntyNo][feature]:
                    notFound = True

        if notFound:
            continue
        return auntyNo
        
def solve(inputPath):
    inputData = getInput(inputPath)

    print([getCorrectAunty(inputData),
           getCorrectAunty(inputData, isP2 = True)])

#Timer Start
start = timeit.default_timer()

solve('D16.txt')

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
