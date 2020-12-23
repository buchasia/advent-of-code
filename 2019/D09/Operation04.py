from Operation import Operation

class Operation04(Operation):

    @staticmethod
    def getValue(sequence, currentIndex, modes):
        outputVal = Operation04.getSequenceElement(sequence, currentIndex + 1, modes[0])
        #print('>>>>>>>>>>>>>', outputVal, '<<<<<<<<<<<<<<')
        print(outputVal)
        return [sequence, currentIndex + 2]
