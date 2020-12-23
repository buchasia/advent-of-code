def solveQuestion(stepSize, insertCount):
    
    currentPos = 0
    buffer = [0]
    value = 0
    for i in range(1, insertCount + 1):
        currentIndexJump = currentPos + stepSize
        currentPos = (currentIndexJump % i) + 1
        if currentPos == 1:
            value = i
        
    return value
          
print(solveQuestion(345, 50000000))
