from Operation import Operation

class Operation07(Operation):

    @staticmethod
    def getValue(sequence, currentIndex, modes):
        firstElement = Operation07.getSequenceElement(sequence, currentIndex + 1, modes[0])
        secondElement = Operation07.getSequenceElement(sequence, currentIndex + 2, modes[1])
        # if the entry does not exist it will be created, else we update the entry
        resultIndex = Operation07.getIndex(sequence, currentIndex + 3, modes[2])
        if firstElement < secondElement:
            sequence[resultIndex] = 1
        else:
            sequence[resultIndex] = 0

        #print('OP07', firstElement, '<', secondElement, '-->', sequence[resultIndex])
        #print('--> 3rd Index:', currentIndex + 3, 'IndexChanged:', resultIndex)
        return [sequence, currentIndex + 4]
