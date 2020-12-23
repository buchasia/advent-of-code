def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    total = 0
    for line in fileLines:
        values = list(map(int, line.strip('\n').split()))
        values.sort()

        total += values[-1] - values[0]

    return total

print(solveQuestion('D02.txt'))
