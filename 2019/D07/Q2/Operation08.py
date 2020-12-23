from Operation import Operation

class Operation08(Operation):

    @staticmethod
    def getValue(sequence, currentIndex, modes):
        seqLength = len(sequence)

        # For this operation we need two values, if this is not the case we
        # cannot proceed
        if currentIndex + 2 > seqLength:
            raise Exception('SequenceIncomplete', 'Sequence is not as excepted')

        firstElement = Operation08.getSequenceElement(sequence, seqLength, currentIndex + 1, modes[0])
        secondElement = Operation08.getSequenceElement(sequence, seqLength, currentIndex + 2, modes[1])

        if sequence[currentIndex + 3] >= seqLength:
            raise Exception('ResultIndexError', 'Result Index is not in Sequence')
            
        if firstElement == secondElement:
            sequence[sequence[currentIndex + 3]] = 1
        else:
            sequence[sequence[currentIndex + 3]] = 0
        return [sequence, currentIndex + 4]
