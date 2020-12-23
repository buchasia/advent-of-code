import timeit
import re
import copy

# This function reads the input file and prepares the data in the needed format
def getInput(inputPath):
    fileP = open(inputPath, 'r')
    return [int(number) for number in fileP.readlines()[0].strip().split()]

def getValue(inputData, counter = -1):
    counter += 1
    currentChildsLeft = inputData[counter]

    counter += 1
    currentMetadata = inputData[counter]

    childValues = []
    childCounter = 0

    while childCounter < currentChildsLeft:
        childCounter += 1
        [childValue, counter] = getValue(inputData, counter)
        childValues.append(childValue)

    if currentChildsLeft == 0:
        return [sum(inputData[(counter + 1):(counter + currentMetadata + 1)]), counter + currentMetadata]
    else:

        return[sum([childValues[metadata - 1]
                    for metadata in inputData[(counter + 1):(counter + currentMetadata + 1)]
                    if metadata <= len(childValues) and metadata > 0]), counter + currentMetadata]

def getMetadataSum(inputData, counter = -1):

    counter += 1
    currentChildsLeft = inputData[counter]

    counter += 1
    currentMetadata = inputData[counter]

    sumMetadata = 0

    childCounter = 0
    while childCounter < currentChildsLeft:
        childCounter += 1
        [sumChildMetadata, counter] = getMetadataSum(inputData, counter)
            
        sumMetadata += sumChildMetadata

    sumMetadata += sum(inputData[(counter + 1):(counter + currentMetadata + 1)])
    counter += currentMetadata

    return [sumMetadata, counter]
    

def solveParts(inputData):
    return [
            getMetadataSum(inputData)[0],
            getValue(inputData)[0]
           ]

# This function reads the input data in the format that can be used by solvers        
def solve(inputPath):
    inputData = getInput(inputPath)
    print(solveParts(inputData))

#Timer Start
start = timeit.default_timer()

solve("D08.txt")

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
