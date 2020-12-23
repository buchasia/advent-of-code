from Operation import Operation

class Operation99(Operation):

    @staticmethod
    def getNumberOfOperands():
        return 1

    @staticmethod
    def getValue(sequence, currentIndex, modes):
        return sequence
