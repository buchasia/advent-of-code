def solveQuestion(inputPath, numIteration):
        
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    offset = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    getNewDirection = {'D': {'L': 'R', 'R': 'L'},
                       'U': {'L': 'L', 'R': 'R'},
                       'L': {'L': 'D', 'R': 'U'},
                       'R': {'L': 'U', 'R': 'D'}}
    onGrids = []
    currentY = -1
    currentVirusX = len(fileLines[0].strip()) // 2
    currentVirusY = len(fileLines) // 2

    currentDirection = 'U'
    
    for line in fileLines:
        currentY += 1
        line = line.strip()
        currentX = -1
        for char in line:
            currentX += 1

            if char == '#':
                onGrids.append((currentY, currentX))

    countOn = 0
    counter = 0
    while counter < numIteration:
        counter += 1
        if (currentVirusY, currentVirusX) in onGrids:
            currentDirection = getNewDirection[currentDirection]['R']
        else:
            currentDirection = getNewDirection[currentDirection]['L']

        if (currentVirusY, currentVirusX) not in onGrids:
            onGrids.append((currentVirusY, currentVirusX))
            countOn += 1
        else:
            onGrids.remove((currentVirusY, currentVirusX))

        currentVirusX += offset[currentDirection][1]
        currentVirusY += offset[currentDirection][0]

    return countOn
            
print(solveQuestion('InputD22.txt', 10000))
