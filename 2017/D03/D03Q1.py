def solveQuestion(value):

    n = -1
    total = 0
    while total < value:
        n += 1
        total = 4*n*n - 4*n + 1

    n = n - 1
    minSpiralVal = 4*n*n - 4*n + 1
    
    difference = value - minSpiralVal

    # if difference is more than n - 1
    if difference < n:
        return n + difference
    elif difference == n:
        return n
    elif difference > n and difference < 2*n:
        return n + difference - n
    

print(solveQuestion(361527))
