# In this method we implement Program 1202 to get the final
# sequence

from FactoryMethod import getOperation
from Operation import Operation

def getOp(number):
    strNumber = str(number)
    lenNumber = len(strNumber)
    if lenNumber == 1:
        return number
    elif lenNumber > 1:
        return number % 100

def getModes(number):
    strNumber = str(number)
    lenNumber = len(strNumber)
    if lenNumber <= 2:
        return [0, 0, 0]
    elif lenNumber == 3:
        return [number//100, 0, 0]
    elif lenNumber == 4:
        return [int(strNumber[1]), number//1000, 0]
    elif lenNumber == 5:
        return [int(strNumber[2]), int(strNumber[1]), number//10000]
    else:
        raise Exception('More than five digits not expected')

def runProgram1202(inputPath, inputValue):

    Operation.setInputValue(inputValue)
    
    # Open file for reading the input sequence
    with open(inputPath) as fileP:

        # Read the complete sequence and remove unwanted characters
        initialSequence = fileP.read().strip()

        # The sequence as List of integers
        finalSeq = list(map(int, initialSequence.split(',')))

        seqLength = len(finalSeq)

        # Sequence length cannot be 0
        if seqLength == 0:
            raise Exception('WrongData', 'Empty sequence')
        
        currentIndex = 0

        # next operation
        currentOp = getOp(finalSeq[currentIndex])
        modes = getModes(finalSeq[currentIndex])
                
        # We could do a max length of sequence or when we have 99 at the
        # current index
        while currentIndex < seqLength and currentOp != 99:

            operation = getOperation(currentOp)

            [finalSeq, currentIndex] = operation.getValue(finalSeq, currentIndex, modes)
            
            # next operation
            if currentIndex < seqLength:
                currentOp = getOp(finalSeq[currentIndex])
                modes = getModes(finalSeq[currentIndex])

        return finalSeq
    
inputValue = 5
runProgram1202('InputDay05Q2.txt', inputValue)
