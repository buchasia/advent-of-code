class Operation:
    inputValues = []

    outputValues = []

    relativeBase = 0
    
    @staticmethod
    def getValue(sequence, currentIndex, modes):
            raise Exception('Implementation not found')
            
    @staticmethod
    def getSequenceElement(sequence, currentIndex, mode):
        if mode == 0:
            if sequence[currentIndex] in sequence:
                return sequence[sequence[currentIndex]]
            else:
                return 0
        elif mode == 1:
            if currentIndex in sequence:
                return sequence[currentIndex]
            else:
                return 0
        elif mode == 2:
            elementIndex = Operation.relativeBase + sequence[currentIndex]
            if elementIndex < 0:
                raise Exception('relative Index not positive')
            if elementIndex in sequence:
                return sequence[elementIndex]
            else:
                return 0
        else:
            raise Exception('Mode not supported')

    @staticmethod
    def getIndex(sequence, currentIndex, mode):
        if mode == 2:
            elementIndex = Operation.relativeBase + sequence[currentIndex]
        else:
            elementIndex = sequence[currentIndex]

        return elementIndex

    @staticmethod
    def setInputValue(inpValues):
        Operation.inputValues = inpValues


    @staticmethod
    def initializeOutput():
        Operation.outputValues = []

    @staticmethod
    def getOutput():
        return Operation.outputValues
