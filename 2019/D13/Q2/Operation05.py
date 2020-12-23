from Operation import Operation

class Operation05(Operation):

    @staticmethod
    def getValue(sequence, currentIndex, modes):
        firstElement = Operation05.getSequenceElement(sequence, currentIndex + 1, modes[0])
        #print('OP5', firstElement, '!= 0 -->', firstElement != 0 )
        if firstElement != 0:
            secondElement = Operation05.getSequenceElement(sequence, currentIndex + 2, modes[1])
            #print('--> new Index', secondElement)
            return [sequence, secondElement]
        #print('--> new Index', currentIndex + 3)
        return [sequence, currentIndex + 3]
