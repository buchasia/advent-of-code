def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()
    buttonMap = { 1: {'D': 3},
                  2: {'D': 6, 'R': 3},
                  3: {'D': 7, 'L': 2, 'U': 1, 'R': 4},
                  4: {'D': 8, 'L': 3},
                  5: {'R': 6},
                  6: {'D': 'A', 'U': 2, 'L': 5, 'R': 7},
                  7: {'D': 'B', 'R': 8, 'L': 6, 'U': 3},
                  8: {'U': 4, 'R': 9, 'L': 7, 'D': 'C'},
                  9: {'L': 8},
                  'A': {'U': 6, 'R': 'B'},
                  'B': {'U': 7, 'L': 'A', 'R': 'C', 'D': 'D'},
                  'C': {'L': 'B', 'U': 8},
                  'D': {'U': 'B' }
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
