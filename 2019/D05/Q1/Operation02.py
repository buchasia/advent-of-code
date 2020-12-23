from Operation import Operation

class Operation02(Operation):

    @staticmethod
    def getNumberOfOperands():
        return 4

    @staticmethod
    def getValue(sequence, currentIndex, modes):
        seqLength = len(sequence)
        # For this operation we need three values, if this is not the case we
        # cannot proceed
        if currentIndex + 3 > seqLength:
            raise Exception('SequenceIncomplete', 'Sequence is not as excepted')

        # Do plausibility test to check if the indices exist that needs to be
        # processed
        firstElement = Operation02.getSequenceElement(sequence, seqLength, currentIndex + 1, modes[0])
        secondElement = Operation02.getSequenceElement(sequence, seqLength, currentIndex + 2, modes[1])

        if sequence[currentIndex + 3] >= seqLength:
            raise Exception('ResultIndexError', 'Result Index is not in Sequence')
                    
        sequence[sequence[currentIndex + 3]] = firstElement * secondElement

        return sequence
