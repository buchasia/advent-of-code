from FactoryMethod import getOperation
from Operation import Operation

class Program1202:
    def __init__(self, filePath, startValue):
        self.filePath = filePath
        self.sequence = {}
        self.currentIndex = 0
        self.startValue = startValue
        self.getInitialSequence()
        self.finished = False
        
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
            sequenceAsList = list(map(int, initialSequence.split(',')));

            index = 0
            
            for element in sequenceAsList:
                self.sequence[index] = element
                index = index + 1

            if self.startValue != 0:
                self.sequence[0] = self.startValue

            # Sequence length cannot be 0
            if len(self.sequence) == 0:
                raise Exception('WrongData', 'Empty sequence')
        
    def run(self, initialValue):

        # next operation
        currentOp = Program1202.getOp(self.sequence[self.currentIndex])
        modes = Program1202.getModes(self.sequence[self.currentIndex])

        Operation.inputValues.append(initialValue)

        # We could do a max length of sequence or when we have 99 at the
        # current index
        while currentOp != 99:
            if currentOp == 3:
                if len(Operation.inputValues) == 0:
                    return

            #print(currentOp)
            operation = getOperation(currentOp)

            [self.sequence, self.currentIndex] = operation.getValue(self.sequence, self.currentIndex, modes)
            
            # next operation
            currentOp = Program1202.getOp(self.sequence[self.currentIndex])
            modes = Program1202.getModes(self.sequence[self.currentIndex])            

        self.finished = True

    def isFinished(self):
        return self.finished
