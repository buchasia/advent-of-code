from Operation import Operation

class Operation04(Operation):

    @staticmethod
    def getValue(sequence, currentIndex, modes):
        seqLength = len(sequence)

        # For this operation we need three values, if this is not the case we
        # cannot proceed
        if currentIndex + 1 > seqLength:
            raise Exception('SequenceIncomplete', 'Sequence is not as excepted')
        
        outputVal = Operation04.getSequenceElement(sequence, seqLength, currentIndex + 1, modes[0])
        Operation04.appendOutput(outputVal)
        return [sequence, currentIndex + 2]
