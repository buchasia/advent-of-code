def solveQuestion(inputPath, numIteration):
        
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    offset = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    getNewDirection = {'D': {'L': 'R', 'R': 'L', 'reverse': 'U', 'noChange': 'D'},
                       'U': {'L': 'L', 'R': 'R', 'reverse': 'D', 'noChange': 'U'},
                       'L': {'L': 'D', 'R': 'U', 'reverse': 'R', 'noChange': 'L'},
                       'R': {'L': 'U', 'R': 'D', 'reverse': 'L', 'noChange': 'R'}}
    stateChange = {'C': 'W', 'W': 'I', 'I': 'F', 'F': 'C'} #C: Clean, W: Weakened, I: Infected, F: Flagged 
    onGrids = {}
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
                onGrids[(currentY, currentX)] = 'I'

    countOn = 0
    counter = 0
    while counter < numIteration:
        counter += 1
        if (currentVirusY, currentVirusX) not in onGrids:
            onGrids[(currentVirusY, currentVirusX)] = 'C'

        if onGrids[(currentVirusY, currentVirusX)] == 'C':
            currentDirection = getNewDirection[currentDirection]['L']
        elif onGrids[(currentVirusY, currentVirusX)] == 'W':
            currentDirection = getNewDirection[currentDirection]['noChange']
        elif onGrids[(currentVirusY, currentVirusX)] == 'I':
            currentDirection = getNewDirection[currentDirection]['R']
        elif onGrids[(currentVirusY, currentVirusX)] == 'F':
            currentDirection = getNewDirection[currentDirection]['reverse']

        onGrids[(currentVirusY, currentVirusX)] = stateChange[onGrids[(currentVirusY, currentVirusX)]]
        if onGrids[(currentVirusY, currentVirusX)] == 'I':
            countOn += 1

        currentVirusX += offset[currentDirection][1]
        currentVirusY += offset[currentDirection][0]

    return countOn
            
print(solveQuestion('InputD22.txt', 10000000))
