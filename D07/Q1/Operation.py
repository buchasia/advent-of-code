class Operation:
    inputValues = []

    outputValues = []

    currentInputIndex = 0
    
    @staticmethod
    def getValue(sequence, currentIndex, modes):
            raise Exception('Implementation not found')
            
    @staticmethod
    def getSequenceElement(sequence, seqLength, currentIndex, mode):
        if mode == 0:
            if sequence[currentIndex] < seqLength:
                return sequence[sequence[currentIndex]]
            else:
                raise Exception('ElementError', 'Element Index not in Sequence')
        elif mode == 1:
            if currentIndex < seqLength:
                return sequence[currentIndex]
            else:
                raise Exception('ElementError', 'Element Index not in Sequence')
        else:
            raise Exception('Mode not supported')

    @staticmethod
    def setInputValue(inpValues):
        Operation.inputValues = inpValues

    @staticmethod
    def increaseCurrentInputIndex():
        Operation.currentInputIndex += 1

    @staticmethod
    def appendOutput(outVal):
        Operation.outputValues.append(outVal)

    @staticmethod
    def getOutput():
        return Operation.outputValues

    @staticmethod
    def initializeOutput():
        Operation.outputValues = []
        Operation.currentInputIndex = 0
