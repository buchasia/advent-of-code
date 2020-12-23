from FactoryMethod import getOperation
from Operation import Operation

class Amplifier:
    def __init__(self, filePath, phase, isFirst):
        self.phase = phase
        self.filePath = filePath
        self.sequence = []
        self.seqLength = 0
        self.currentIndex = 0
        self.finished = False
        if isFirst:
            self.inputValues = [phase, 0]
        else:
            self.inputValues = [phase]
        self.getInitialSequence()

    def setNextAmplifier(self, nextAmplifier):
        self.nextAmplifier = nextAmplifier
    
    @staticmethod
    def getOp(number):
        strNumber = str(number)
        lenNumber = len(strNumber)
        if lenNumber == 1:
            return number
        elif lenNumber > 1:
            return number % 100

    @staticmethod
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
    
    def getInitialSequence(self):
        # Open file for reading the input sequence
        with open(self.filePath) as fileP:
            # Read the complete sequence and remove unwanted characters
            initialSequence = fileP.read().strip()

            # The sequence as List of integers
            self.sequence = list(map(int, initialSequence.split(',')))

            self.seqLength = len(self.sequence)
            
            # Sequence length cannot be 0
            if self.seqLength == 0:
                raise Exception('WrongData', 'Empty sequence')

    def appendInputValue(self, inputValue):
        self.inputValues.append(inputValue)

    def isFinished(self):
        return self.finished
        
    def runProgram(self):

        # next operation
        currentOp = Amplifier.getOp(self.sequence[self.currentIndex])
        modes = Amplifier.getModes(self.sequence[self.currentIndex])

        # We could do a max length of sequence or when we have 99 at the
        # current index
        while self.currentIndex < self.seqLength and currentOp != 99:
            if currentOp == 3:
                if len(self.inputValues) == 0:
                    return
                else:
                    Operation.setInputValue([self.inputValues[0]])
                    self.inputValues.pop(0)
            
            operation = getOperation(currentOp)

            [self.sequence, self.currentIndex] = operation.getValue(self.sequence, self.currentIndex, modes)

            if currentOp == 4:
                if not self.nextAmplifier.isFinished():
                    outputList = Operation.getOutput()
                    self.nextAmplifier.appendInputValue(outputList[0])
                    Operation.initializeOutput()
                    return    
            
            # next operation
            if self.currentIndex < self.seqLength:
                currentOp = Amplifier.getOp(self.sequence[self.currentIndex])
                modes = Amplifier.getModes(self.sequence[self.currentIndex])

        self.finished = True
            

            
