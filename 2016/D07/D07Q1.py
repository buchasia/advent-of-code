import hashlib

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
                outer += character
                continue
            elif character == ']':
                openBracket = False
                inner += character
                continue
            
            
            if openBracket:
                inner += character
            else:
                outer += character

        if isABBA(outer) and not isABBA(inner):
            IPCount += 1

    return IPCount

    
def isABBA(string):
    for i in range(len(string) - 3):
        if string[i] == string[i + 3] and string[i + 1] == string[i + 2] and string[i] != string[i + 1]:
            return True
        
    return False

print(solveQuestion('InputD07Q1.txt'))
