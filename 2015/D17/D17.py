import timeit
import re
import math

def getInput():
     t = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]
     t.sort()
     return t

def getCount(seen, capacities):
    count = 1
    found = set()
    for capacity in seen:
        if capacity in found:
            continue
        found.add(capacity)
        count *= math.factorial(capacities.count(capacity)) // math.factorial(seen.count(capacity)) 
    return count

def getAllCombination(inputData):
    uniqueCap = list(set(inputData))
    uniqueCap.sort()
    return getPossibleCombination(uniqueCap, inputData)

def getPossibleCombination(uniqueCap, capacities, unitsLeft = 150, counter = 0, seen = [], seenAll = [], countSeen = {}, lastNumber = 0):
    if unitsLeft == 0:
        if seen not in seenAll:
            seenAll.append(list(seen))
            count = getCount(seen, capacities)
            counter += count
            if len(seen) not in countSeen:
                countSeen[len(seen)] = count
            else:
                countSeen[len(seen)] += count
        return [counter, False, countSeen]
    elif unitsLeft < 0:
        return [counter, True, countSeen]
    
    for capacity in uniqueCap:
        if capacities.count(capacity) == seen.count(capacity):
            continue
        seen.append(capacity)
        [counter, isExceed, countSeen] = getPossibleCombination(uniqueCap[uniqueCap.index(capacity):], capacities, unitsLeft - capacity, counter, seen, seenAll, countSeen, capacity)
        seen.remove(capacity)

        if isExceed:
            break
        
    return [counter, False, countSeen]
        
def solve():
    inputData = getInput()
    output = getAllCombination(inputData)
    print([output[0], output[2][min(output[2].keys())]])

#Timer Start
start = timeit.default_timer()

solve()

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
