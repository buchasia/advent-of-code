import hashlib

def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    doorId = fileLines[0]

    password = ''
    counter = 0
    while len(password) != 8:
        counter += 1
        currentString = doorId + str(counter)
        hashString = hashlib.md5(currentString.encode()).hexdigest()
        if hashString[:5] == '00000' and hashString[5] != 0:
            password += hashString[5]
    
    return password

print(solveQuestion('InputD05Q1.txt'))
