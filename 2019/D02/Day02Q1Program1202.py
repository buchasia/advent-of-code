# In this method we implement Program 1202 to get the final
# sequence

def runProgram1202(inputPath):

    # Open file for reading the input sequence
    with open(inputPath) as fileP:

        # Read the complete sequence and remove unwanted characters
        initialSequence = fileP.read().strip()

        # The sequence as List of integers
        finalSeq = list(map(int, initialSequence.split(',')))

        seqLength = len(finalSeq)

        # Sequence length cannot be 0
        if seqLength == 0:
            raise Exception('WrongData', 'Empty sequence')
        
        currentIndex = 0

        # Do the initial changes recommended in the problem description
        finalSeq[1] = 12
        finalSeq[2] = 2

        # next operation
        currentOp = finalSeq[currentIndex]
                
        # We could do a max length of sequence or when we have 99 at the
        # current index
        while currentIndex < seqLength and currentOp != 99:
            
            # For operations we need three values, if this is not the case we
            # cannot proceed
            if currentIndex + 3 > seqLength:
                raise Exception('SequenceIncomplete', 'Sequence is not as excepted')

            # Do plausibility test to check if the indices exist that needs to be
            # processed
            if finalSeq[currentIndex + 1] < seqLength:
                firstElement = finalSeq[finalSeq[currentIndex + 1]]
            else:
                raise Exception('FirstElementError', 'First Element Index not in Sequence')

            if finalSeq[currentIndex + 2] < seqLength:
                secondElement = finalSeq[finalSeq[currentIndex + 2]]
            else:
                raise Exception('SecondElementError', 'Second Element Index not in Sequence')

            if finalSeq[currentIndex + 3] >= seqLength:
                raise Exception('ResultIndexError', 'Result Index is not in Sequence')
            
            # perform operation on the sequence, operation 99 is already processed
            # in the while loop.
            if currentOp == 1:
                finalSeq[finalSeq[currentIndex + 3]] = firstElement + secondElement
            elif currentOp == 2:
                finalSeq[finalSeq[currentIndex + 3]] = firstElement * secondElement
            else:
                raise Exception('WrongOpCode', 'Op Code should be 1, 2 or 99.')
            
            # Increase the index to process the next operation
            currentIndex += 4

            # next operation
            if currentIndex < seqLength:
                currentOp = finalSeq[currentIndex]

    return finalSeq[0]

print(runProgram1202('InputDay02Q1.txt'))
