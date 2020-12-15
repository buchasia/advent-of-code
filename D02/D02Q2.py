def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    total = 0
    for line in fileLines:
        values = list(map(int, line.strip('\n').split()))

        for i in range(len(values)):
            for j in range(len(values)):
                if i == j:
                    continue
                if values[i] % values[j] == 0:
                    total += values[i] // values[j]
                    break

    return total

print(solveQuestion('InputD02Q2.txt'))
