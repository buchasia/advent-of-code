def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()
    buttonMap = { 1: {'D': 4, 'R': 2},
                  2: {'D': 5, 'R': 3, 'L': 1},
                  3: {'D': 6, 'L': 2},
                  4: {'D': 7, 'R': 5, 'U': 1},
                  5: {'D': 8, 'R': 6, 'U': 2, 'L': 4},
                  6: {'D': 9, 'U': 3, 'L': 5},
                  7: {'U': 4, 'R': 8},
                  8: {'U': 5, 'R': 9, 'L': 7},
                  9: {'U': 6, 'L': 8}
        }
    currentKey = 5
    sequence = ''
    for directions in fileLines:
        directions = directions.strip('\n')
        for direction in directions:
            buttonMapCurrent = buttonMap[currentKey]
            if direction in buttonMapCurrent:
                currentKey = buttonMapCurrent[direction]
        sequence += str(currentKey)

    return sequence

print(solveQuestion('InputD02Q1.txt'))
