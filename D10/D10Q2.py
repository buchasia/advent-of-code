def solveQuestion(inputPath):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    botMoves = {}
    botValues = {}
    
    for line in fileLines:
        line = line.strip('\n')
        isLowOutput = False
        isHighOutput = False
        if line[:5] == 'value':
            splitText = line.split(' ')
            value = int(splitText[1])
            botIndex = int(splitText[5])

            if botIndex in botValues:
                botValues[botIndex].append(value)
            else:
                botValues[botIndex] = [value]
        else:
            splitText = line.split(' ')
            if splitText[5] == 'output':
                isLowOutput = True
            if splitText[10] == 'output':
                isHighOutput = True
            botIndexSource = int(splitText[1])
            botIndexLow = int(splitText[6])
            botIndexHigh  = int(splitText[11])

            botMoves[botIndexSource] = {}
            if isLowOutput == True:
                botMoves[botIndexSource]['low'] = -1 * botIndexLow - 1
            else:
                botMoves[botIndexSource]['low'] = botIndexLow

            if isHighOutput == True:
                botMoves[botIndexSource]['high'] = -1 * botIndexHigh - 1
            else:
                botMoves[botIndexSource]['high'] = botIndexHigh

    while 1:
        for bot in botValues:
            values = list(botValues[bot])
            if len(values) == 2:
                moves = botMoves[bot]
                
                botValues[bot] = []
                lowBotIndex = moves['low']
                highBotIndex = moves['high']

                if values[0] > values[1]:
                    highValue = values[0]
                    lowValue = values[1]
                else:
                    highValue = values[1]
                    lowValue = values[0]

                if -1 in botValues and -2 in botValues and -3 in botValues:
                    return botValues[-1][0] * botValues[-2][0] * botValues[-3][0]
                
                if lowBotIndex in botValues:
                    botValues[lowBotIndex].append(lowValue)
                else:
                    botValues[lowBotIndex] = [lowValue]
                if highBotIndex in botValues:
                    botValues[highBotIndex].append(highValue)
                else:
                    botValues[highBotIndex] = [highValue]
                break
    
print(solveQuestion('InputD10Q2.txt'))
