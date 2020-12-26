import timeit

# This function reads the input file and prepares the data in the needed format
def getInput(inputPath):
    fileP = open(inputPath, 'r')
    return [line.strip() for line in fileP.readlines()]

def countCharactersAfterReplacement(inputData):
    return countCharacters(['"' + line.replace('\\', '\\\\').replace('"', '\\"') + '"' for line in inputData])

def countCharacters(inputPath):
    total = 0
    for line in inputPath:
        total += 2
        counter = 1
        while counter < len(line) - 1:
            if line[counter] == '\\':
                counter += 1
                if line[counter] == '"' or line[counter] == '\\':
                    total += 1
                elif line[counter] == 'x':
                    total += 3
                    counter += 2
            counter += 1
    return total

def solveParts(inputData):
    return [countCharacters(inputData),
            countCharactersAfterReplacement(inputData)]

def solve(inputPath):
    inputData = getInput(inputPath)
    print(solveParts(inputData))

#Timer Start
start = timeit.default_timer()

solve("D08.txt")

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
