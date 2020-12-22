import timeit

# This function reads the input file and prepares the data in the needed format
def getInput(inputPath):
    fileP = open(inputPath, 'r')
    return fileP.readlines()[0].strip()

# This function removes the reacting units present in the polymer
def reactingPoly(polymer):
    units = str(polymer)
    
    currentLen = len(units)
    previousLen = currentLen + 1

    # Do until we do not find any other reacting units
    while currentLen < previousLen:
        previousLen = currentLen

        # Replace text is a list of possibilities 'aA' or 'Aa' ...
        for replaceText in replaceTexts:
            units = units.replace(replaceText, '')
        currentLen = len(units)

    # Return the length 
    return currentLen

def solveParts(inputData):
    return [
            # Part 1
            # just perform reactingPolymer on the input data
            reactingPoly(inputData),
            
            # Part 2
            # Replace small and capital for each alphabet with empty string and
            # perform reactingPolymer then take the minimum length
            min([reactingPoly(inputData.replace(char, '').replace(char.upper(), ''))
                 for char in 'abcdefghijklmnopqrstuvwxyz'])
           ] 

# This function reads the input data in the format that can be used by solvers        
def solve(inputPath):
    inputData = getInput(inputPath)
    print(solveParts(inputData))

#Timer Start
start = timeit.default_timer()

# Generate possible reacting units, eg. aA, Aa, bB, ...
replaceTexts = [char + char.upper() if j == 1 else char.upper() + char
                for j in (1, 2) for char in 'abcdefghijklmnopqrstuvwxyz']    

solve("D05.txt")

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
