def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    programs = {}
    for line in fileLines:
        line = line.strip()
        [programId, possibleProgramId] = line.split(' <-> ')
        programs[int(programId)] = list(map(int, possibleProgramId.split(', ')))

    groups = 0
    while len(programs) > 0:
        groups += 1

        for key in programs.keys():
            toVisit = [key]
            break
        counter = 0
        while counter < len(toVisit):
            currentProgramId = toVisit[counter]
            for programId in programs[currentProgramId]:
                if programId not in toVisit:
                    toVisit.append(programId)

            del programs[currentProgramId]
            counter += 1

    return groups
    
print(solveQuestion('InputD12Q2.txt'))
