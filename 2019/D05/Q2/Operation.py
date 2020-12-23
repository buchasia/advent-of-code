class Operation:
    inputValue = 0
    
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
    def setInputValue(inpValue):
        Operation.inputValue = inpValue

	
