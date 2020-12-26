import timeit
import re

# This function reads the input file and prepares the data in the needed format
def getInput(inputPath):
    fileP = open(inputPath, 'r')
    regEx = re.compile('(\w*) would (\w*) (\d*) [ \w]+ (\w*)')
    return {(line[0], line[3]): int(line[2]) if line[1] == 'gain' else -1 * int(line[2])
            for line in regEx.findall(''.join(fileP.readlines()))}

def getAllGuestSeating(inputData, allGuests, happiness = 0, seen = set(), lastGuest = '', currentGuests = '', currentHappiness = 0):
    if len(seen) == len(allGuests):
        currentHappiness += inputData[(lastGuest, currentGuests.split('->')[0])] + inputData[(currentGuests.split('->')[0], lastGuest)]
        happiness = currentHappiness if happiness < currentHappiness else happiness
        return happiness

    for guest in allGuests:
        if guest not in seen:      
            seen.add(guest)
            if lastGuest == '':
                happiness = getAllGuestSeating(inputData, allGuests, happiness, seen, guest, guest, 0)
            else:
                happiness = getAllGuestSeating(inputData, allGuests, happiness, seen, guest, currentGuests + '->' + guest, currentHappiness + inputData[(lastGuest, guest)] + inputData[(guest, lastGuest)])
            seen.remove(guest)
    return happiness

def solve(inputPath):
    inputData = getInput(inputPath)
    allGuests = {guestMap[0] for guestMap in inputData}

    part1Happniess = getAllGuestSeating(inputData, allGuests)

    inputData.update({('Me', guest): 0 for guest in allGuests})
    inputData.update({(guest, 'Me'): 0 for guest in allGuests})
    allGuests.add('Me')

    print([part1Happniess, getAllGuestSeating(inputData, allGuests)])

#Timer Start
start = timeit.default_timer()

solve("D13.txt")

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
