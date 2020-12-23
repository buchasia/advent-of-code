from Operation import Operation

class Operation03(Operation):

    @staticmethod
    def getNumberOfOperands():
        return 2

    @staticmethod
    def getValue(sequence, currentIndex, modes):
        seqLength = len(sequence)
        # For this operation we need one values, if this is not the case we
        # cannot proceed
        if currentIndex + 1 > seqLength:
            raise Exception('SequenceIncomplete', 'Sequence is not as excepted')
        
        if sequence[currentIndex + 1] < seqLength:
            sequence[sequence[currentIndex + 1]] = 1
        else:
            raise Exception('ElementError', 'Element Index not in Sequence')

        return sequence
