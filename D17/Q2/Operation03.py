from Operation import Operation

class Operation03(Operation):

    @staticmethod
    def getValue(sequence, currentIndex, modes):
        elementIndex = Operation03.getIndex(sequence, currentIndex + 1, modes[0])
        #print('OP03', 'nextIndex:', elementIndex, 'mode:', modes[0], 'currentBase:', Operation.relativeBase)
        # if the entry does not exist it will be created, else we update the entry
        sequence[elementIndex] = Operation.inputValues[0]
        Operation.inputValues.pop(0)
        #print('--> newValue:', sequence[elementIndex] )
        
        return [sequence, currentIndex + 2]
