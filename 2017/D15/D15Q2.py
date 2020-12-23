def solveQuestion(currentA, currentB, multA, multB, divide):
    total = 0
    count = 0
    last16Bits = 2**16
    while count < 5000000:
        count += 1
        currentA = (currentA * multA) % divide

        while currentA % 4 != 0:
            currentA = (currentA * multA) % divide
        currentB = (currentB * multB) % divide

        while currentB % 8 != 0:
            currentB = (currentB * multB) % divide
            
        if currentA % last16Bits == currentB % last16Bits:
            total += 1

        if count % 500000 == 0:
            print(count, total)
    return total
        
print(solveQuestion(512, 191, 16807, 48271, 2147483647))
