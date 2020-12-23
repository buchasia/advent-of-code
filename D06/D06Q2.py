import hashlib

def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    characterCount = {}
    message = ''
    for line in fileLines:
        line = line.strip()
        count = 0
        for character in line:
            if count not in characterCount:
                characterCount[count] = {}
            if character in characterCount[count]:
                characterCount[count][character] += 1
            else:
                characterCount[count][character] = 1
            count += 1
    for pos in characterCount:
        minCharacterCount = 0
        minCharacter = ''
        for character in characterCount[pos]:
            if minCharacter == '' or minCharacterCount > characterCount[pos][character]:
                minCharacterCount = characterCount[pos][character]
                minCharacter = character
        message += minCharacter
    return message

print(solveQuestion('InputD06Q2.txt'))
