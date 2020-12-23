import hashlib

def solveProblem(inputPath):

    currentNumber = 1
    currentNumberStr = '1'
    step = 1
    
    with open(inputPath) as fileP:

        valueLine = str(fileP.readline()).strip('\n')

        md5Value = hashlib.md5((valueLine + currentNumberStr).encode('utf-8')).hexdigest()
        
        while md5Value[:6] != '000000':
            currentNumber += step
            currentNumberStr = str(currentNumber)
            md5Value = hashlib.md5((valueLine + currentNumberStr).encode('utf-8')).hexdigest()
            
    return currentNumber

print(solveProblem('InputD04Q2.txt'))
