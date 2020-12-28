import timeit

def getInput(inputPath):
    fileP = open(inputPath, 'r')
    lines = fileP.readlines()
    molecule = lines[-1].strip()
    possReplacements = [lines[i].strip().split(' => ') for i in range(len(lines) - 2)]

    return [molecule, possReplacements]

def getMinimumSteps(startingMolecule, possReplacements, molecule):
    count = 0
    while molecule != startingMolecule:
        for possReplacement in possReplacements:
            if possReplacement[1] in molecule:
                molecule = molecule.replace(possReplacement[1], possReplacement[0], 1)
                break
        count += 1
    return count
        
def createMolecule(possReplacements, molecule):
    molecules = set()
    for possReplacement in possReplacements:
        possCount = molecule.count(possReplacement[0])
        position = -1
        for i in range(possCount):
            position = molecule.index(possReplacement[0], position + 1)
            newMolecule = molecule[:position] + possReplacement[1] + molecule[(position + len(possReplacement[0])):]
            if newMolecule in molecules:
                continue
            
            molecules.add(newMolecule)
    return molecules
    
            
def solve(inputPath):
    [molecule, possReplacements] = getInput(inputPath)
    print([len(createMolecule(possReplacements, molecule)),
           getMinimumSteps('e', possReplacements, molecule)])

#Timer Start
start = timeit.default_timer()

solve('D19.txt')

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
