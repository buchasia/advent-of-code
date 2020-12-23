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
                openBrackets.append('{')
        elif fileLines[index] == '}':
            if isGarbage == True:
                if isIgnore == True:
                    isIgnore = False
            else:
                total += len(openBrackets)
                openBrackets.pop(0)
        elif fileLines[index] == '<':
            if isGarbage == True:
                if isIgnore == True:
                    isIgnore = False
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
            if isIgnore == True:
                isIgnore = False
    return total
print(solveQuestion('InputD09Q1.txt'))
