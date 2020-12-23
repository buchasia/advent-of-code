from Operation import Operation

class Operation08(Operation):

    @staticmethod
    def getValue(sequence, currentIndex, modes):
        firstElement = Operation08.getSequenceElement(sequence, currentIndex + 1, modes[0])
        secondElement = Operation08.getSequenceElement(sequence, currentIndex + 2, modes[1])
        # if the entry does not exist it will be created, else we update the entry
        resultIndex = Operation08.getIndex(sequence, currentIndex + 3, modes[2])

        if firstElement == secondElement:
            sequence[resultIndex] = 1
        else:
            sequence[resultIndex] = 0
        #print('OP08', firstElement, '=', secondElement, '-->', sequence[resultIndex])
        #print('--> 3rd Index:', currentIndex + 3,  'IndexChanged:', resultIndex)
        return [sequence, currentIndex + 4]
