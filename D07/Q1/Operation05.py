from Operation import Operation

class Operation05(Operation):

    @staticmethod
    def getValue(sequence, currentIndex, modes):
        seqLength = len(sequence)

        # For this operation we need two values, if this is not the case we
        # cannot proceed
        if currentIndex + 2 > seqLength:
            raise Exception('SequenceIncomplete', 'Sequence is not as excepted')

        firstElement = Operation05.getSequenceElement(sequence, seqLength, currentIndex + 1, modes[0])
        if firstElement != 0:
            secondElement = Operation05.getSequenceElement(sequence, seqLength, currentIndex + 2, modes[1])
            return [sequence, secondElement]
        return [sequence, currentIndex + 3]
