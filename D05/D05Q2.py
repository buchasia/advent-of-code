import hashlib

def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    doorId = fileLines[0]

    password = {}
    counter = 0
    while len(password) != 8:
        counter += 1
        currentString = doorId + str(counter)
        hashString = hashlib.md5(currentString.encode()).hexdigest()
        if hashString[:5] == '00000' and hashString[5] != 0:
            print(counter, hashString[5], hashString[6])
            if hashString[5] > '7':
                continue
            if int(hashString[5]) not in password:
                password[int(hashString[5])] = hashString[6]
                

    actualPassword = ''
    for i in range(8):
        actualPassword += password[i]

    return actualPassword

print(solveQuestion('InputD05Q1.txt'))
