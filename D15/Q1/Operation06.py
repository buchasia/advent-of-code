from Operation import Operation

class Operation06(Operation):

    @staticmethod
    def getValue(sequence, currentIndex, modes):
        firstElement = Operation06.getSequenceElement(sequence, currentIndex + 1, modes[0])
        if firstElement == 0:
            secondElement = Operation06.getSequenceElement(sequence, currentIndex + 2, modes[1])
            return [sequence, secondElement]
        return [sequence, currentIndex + 3]
