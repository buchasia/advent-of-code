# In this method we implement Program 1202 to get the final
# sequence

import itertools

from Amplifier import Amplifier
from Operation import Operation

def AmplificationCircuit(inputPath, phasesPoss, amplifierCount):
    outputSignals = []
    for phasePoss in phasesPoss:
        amplifiers = []
        counter = 0
        finishCount = 0
        currentAmplifier = 0
        for phase in phasePoss:
            counter = counter + 1
            if counter == 1:
                amplifiers.append(Amplifier(inputPath, phase, True))
            else:
                amplifiers.append(Amplifier(inputPath, phase, False))

        for i in range(0, amplifierCount - 1):
            amplifiers[i].setNextAmplifier(amplifiers[i + 1])

        amplifiers[amplifierCount - 1].setNextAmplifier(amplifiers[0])
        
        while finishCount != amplifierCount:
            amplifiers[currentAmplifier].runProgram()
            if amplifiers[currentAmplifier].isFinished():
                finishCount += 1
            currentAmplifier += 1
            currentAmplifier = currentAmplifier % 5
            
        outputList = Operation.getLastOutput04()
        outputSignals.append(outputList)
    return outputSignals
            

    
# Number of amplification units
n = 5

# Possible phases
phases = list(range(5, 10))

# all possible combinations of phases:
phasesPoss = list(itertools.permutations(phases, n))

print(max(AmplificationCircuit('InputDay07Q2.txt', phasesPoss, n)))
