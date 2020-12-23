from Operation import Operation

class Operation09(Operation):

    @staticmethod
    def getValue(sequence, currentIndex, modes):
        firstElement = Operation09.getSequenceElement(sequence, currentIndex + 1, modes[0])
        #print('OP09', 'nextIndex:', currentIndex + 1, 'mode:', modes[0], 'previousBase:', Operation.relativeBase)
        Operation.relativeBase += firstElement
        #print('--> valueToIncrease:', firstElement, 'relativeBase:', Operation.relativeBase)
        return [sequence, currentIndex + 2]
