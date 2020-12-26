import timeit
import re

# This function reads the input file and prepares the data in the needed format
def getInput(inputPath):
    fileP = open(inputPath, 'r')
    regEx = re.compile('(\w*) to (\w*) = (\d*)')
    return {(line[0], line[1]): int(line[2]) for line in regEx.findall(''.join(fileP.readlines()))}

def getAllPaths(inputData, allPlaces, distances = [10000, 0], seen = set(), lastPath = '', currentPath = '', currentDistance = 0):
    if len(seen) == len(allPlaces):
        distances[0] = currentDistance if distances[0] > currentDistance else distances[0]
        distances[1] = currentDistance if distances[1] < currentDistance else distances[1]

    for place in allPlaces:
        if place not in seen:      
            seen.add(place)
            if lastPath == '':
                getAllPaths(inputData, allPlaces, distances, seen, place, place, 0)
            else:
                getAllPaths(inputData, allPlaces, distances, seen, place, currentPath + '->' + place, currentDistance + inputData[(lastPath, place)])
            seen.remove(place)
    return distances

def solve(inputPath):
    inputData = getInput(inputPath)
    allPlaces = set()
    allPlaces.update([line[0] for line in inputData])
    allPlaces.update([line[1] for line in inputData])
    inputData.update({(path[1], path[0]): inputData[path] for path in list(inputData.keys())})

    print(getAllPaths(inputData, allPlaces))

#Timer Start
start = timeit.default_timer()

solve("D09.txt")

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
