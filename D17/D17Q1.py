def solveQuestion(stepSize, insertCount):
    
    currentPos = 0
    buffer = [0]

    for i in range(1, insertCount + 1):
        currentIndexJump = currentPos + stepSize
        currentIndexActual = (currentIndexJump % len(buffer)) + 1
        buffer.insert(currentIndexActual, i)
        currentPos = currentIndexActual

    return buffer[currentPos + 1]
    
          
print(solveQuestion(345, 2017))
