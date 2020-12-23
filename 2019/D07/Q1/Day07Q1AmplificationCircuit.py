# In this method we implement Program 1202 to get the final
# sequence

import itertools

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

def runProgram1202(inputPath, inputValues):

    Operation.setInputValue(inputValues)
    
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

def AmplificationCircuit(inputPath, initialSeed, phasesPoss):
    outputList = {}
    finalOutput = []
    for phasePoss in phasesPoss:
        currentPhaseSequence = ''
        
        # set the input value for first amlification unit
        outputVal = initialSeed
        for phase in phasePoss: 
            currentPhaseSequence += str(phase)
            if currentPhaseSequence in outputList:
                outputVal = outputList[currentPhaseSequence]
                continue
            inputValues = [phase, outputVal]
            runProgram1202(inputPath, inputValues)

            outputVal = Operation.getOutput()[0]
            outputList[currentPhaseSequence] = outputVal
            Operation.initializeOutput()
        finalOutput.append(outputVal)
    return finalOutput

    
# Number of amplification units
n = 5

# Possible phases
phases = list(range(0, n))

# all possible combinations of phases:
phasesPoss = list(itertools.permutations(phases, 5))

# Initial seed for 1st amplification unit
inputValue = 0
print(max(AmplificationCircuit('InputDay07Q1.txt', inputValue, phasesPoss)))
