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
        maxCharacterCount = 0
        maxCharacter = ''
        for character in characterCount[pos]:
            if maxCharacterCount < characterCount[pos][character]:
                maxCharacterCount = characterCount[pos][character]
                maxCharacter = character
        message += maxCharacter
    return message

print(solveQuestion('InputD06Q1.txt'))
