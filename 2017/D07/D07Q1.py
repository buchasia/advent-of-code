def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    bottoms = []
    tops = []
    for line in fileLines:
        if line.find('->') != -1:
            [nameWeight, overNames] = line.strip().split('->')
            [name, Weight] = nameWeight.strip().split(' ')
            overNames = overNames.strip().split(', ')
            bottoms.append(name)
            for overName in overNames:
                tops.append(overName)

    for bottom in bottoms:
        if bottom in tops:
            continue

        return bottom

print(solveQuestion('InputD07Q1.txt'))
