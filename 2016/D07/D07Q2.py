def solveQuestion(inputPath):
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    IPCount = 0
    for line in fileLines:
        line = line.strip()
        
        openBracket = False
        outer = ''
        inner = ''
        for character in line:
            if character == '[':
                openBracket = True
            elif character == ']':
                openBracket = False
            
            if openBracket:
                inner += character
            else:
                outer += character

        outerABAStrings = getABA(outer, False)
        innerABAStrings = getABA(inner, True)
        for string in innerABAStrings:
            if string in outerABAStrings:
                IPCount += 1
                break
    return IPCount
    
def getABA(string, reverse):
    ABAStrings = []
    for i in range(len(string) - 2):
        if string[i] == string[i + 2] and string[i + 1] != string[i + 2]:
            if reverse == True:
                ABAStrings.append(string[i+1] + string[i] + string[i+1])
            else:
                ABAStrings.append(string[i:i+3])
    return ABAStrings

print(solveQuestion('InputD07Q2.txt'))
