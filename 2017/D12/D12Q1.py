def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    programs = {}
    for line in fileLines:
        line = line.strip()
        [programId, possibleProgramId] = line.split(' <-> ')
        programs[int(programId)] = list(map(int, possibleProgramId.split(', ')))

    toVisit = [0]
    counter = 0
    while counter < len(toVisit):
        currentProgramId = toVisit[counter]
        for programId in programs[currentProgramId]:
            if programId not in toVisit:
                toVisit.append(programId)

        counter += 1

    return len(toVisit)
    
print(solveQuestion('InputD12Q1.txt'))
