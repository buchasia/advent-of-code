import timeit
import json

def getInput(inputPath):
    with open(inputPath) as f:
        return json.load(f)

def getSum(data, isP2 = False):
    sumValid = 0

    # If it is a list, we process each element in the list individually
    if isinstance(data, list):
        for dataPoint in data:
            if isinstance(dataPoint, int):
                sumValid += dataPoint
            elif isinstance(dataPoint, list) or isinstance(dataPoint, dict):
                sumValid += getSum(dataPoint, isP2 = isP2)
        return sumValid
    
    # If it is a dictionary, we process each dictionary value individually
    elif isinstance(data, dict):

        # For Part 2 we need to remove all dictionarys that have a value 'red'
        if isP2 and 'red' in data.values():
            return sumValid
        else:
            sumValid += sum([getSum(data[dataPoint], isP2 = isP2) for dataPoint in data])

    # If it is is an integer, we add it directly to the sum
    elif isinstance(data, int):
        sumValid += data
    
    return sumValid

def solve(inputPath):
    inputData = getInput(inputPath)
    print([getSum(inputData),
           getSum(inputData, isP2 = True)])
    
#Timer Start
start = timeit.default_timer()

solve('D12.txt')

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
