# In this method we implement Program 1202 to get the expected output

def runProgram1202(inputPath, noun, verb):

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
        finalSeq[1] = noun
        finalSeq[2] = verb

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

def getNounAndVerb(inputPath, expectedOutput):
    # Asuming that the possible values are between 0 and 100 for
    # both noun and verb
    possNouns = range(0, 100)
    possVerbs = range(0, 100)

    for noun in possNouns:
        for verb in possVerbs:
            # run the program for differnt noun and verb combination
            output = runProgram1202(inputPath, noun, verb)

            # if the output is the expected output then we return the
            # result as requested
            if output == expectedOutput:
                return noun * 100 + verb
                
expectedOutput = 19690720
print(getNounAndVerb('InputDay02Q2.txt', expectedOutput))
