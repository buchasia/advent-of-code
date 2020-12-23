def countTrees(inputPath, numberOfRows, numberOfColumns):

    maxTicketId = 0
    ticketIds = []
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()
    
    rowSteps = ''
    columnSteps = ''
    
    for valueLine in fileLines:
        valueLine = str(valueLine).rstrip("\n")

        columnSteps = valueLine[7:]
        rowSteps = valueLine[:7]

        ticketIndex = getIndex(columnSteps, 'R', numberOfColumns) + getIndex(rowSteps, 'B', numberOfRows) * 8

        if ticketIndex not in ticketIds:
            ticketIds.append(ticketIndex)


    ticketIds.sort()

    for i in range(len(ticketIds) - 1):
        if ticketIds[i + 1] - ticketIds[i] == 2:
            return ticketIds[i] + 1

def getIndex(steps, upperIndicator, upperLimit):
    startIndex = 0
    endIndex = upperLimit - 1
    for step in steps:
        if step == upperIndicator:
            startIndex += int((endIndex - startIndex + 1) / 2)
        else:
            endIndex -= int((endIndex - startIndex + 1) / 2)

    return startIndex

print(countTrees('InputD05Q1.txt', 128, 8))
