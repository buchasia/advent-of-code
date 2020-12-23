from Operation import Operation

class Operation02(Operation):

    @staticmethod
    def getValue(sequence, currentIndex, modes):
        firstElement = Operation02.getSequenceElement(sequence, currentIndex + 1, modes[0])
        secondElement = Operation02.getSequenceElement(sequence, currentIndex + 2, modes[1])
        
        # if the entry does not exist it will be created, else we update the entry
        resultIndex = Operation02.getIndex(sequence, currentIndex + 3, modes[2])
        sequence[resultIndex] = firstElement * secondElement

        #print('OP02', firstElement, '*', secondElement, '-->', sequence[resultIndex])
        #print('--> 3rd Index:', currentIndex + 3,  'IndexChanged:', resultIndex)
        
        return [sequence, currentIndex + 4]
