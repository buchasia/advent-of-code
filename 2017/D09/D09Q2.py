def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()[0].strip()
    fileP.close()

    index = -1
    openBrackets = []
    isGarbage = False
    isIgnore = False
    total = 0
    while index < len(fileLines) - 1:
        index += 1
        if fileLines[index] == '{':
            if isGarbage == True:
                if isIgnore == True:
                    isIgnore = False
                else:
                    total += 1
            else:
                openBrackets.append('{')
        elif fileLines[index] == '}':
            if isGarbage == True:
                if isIgnore == True:
                    isIgnore = False
                else:
                    total += 1
            else:
                openBrackets.pop(0)
        elif fileLines[index] == '<':
            if isGarbage == True:
                if isIgnore == True:
                    isIgnore = False
                else:
                    total += 1
            else:
                isGarbage = True
        elif fileLines[index] == '>':
            if isGarbage == True:
                if isIgnore == True:
                    isIgnore = False
                else:
                    isGarbage = False
            else:
                isGarbage = False
        elif fileLines[index] == '!':
            if isGarbage == True:
                if isIgnore == True:
                    isIgnore = False
                else:
                    isIgnore = True
        else:
            if isGarbage == True:
                if isIgnore == True:
                    isIgnore = False
                else:
                    total += 1
    return total
print(solveQuestion('InputD09Q2.txt'))
