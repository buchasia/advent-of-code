import math

# This method will compute the three numbers who sum to given number and return
# the multiple
def sum3Numbers(inputPath, totalSum):

    listNumbers = set()
    listSum2Numbers = {}
    
    # Open file for reading module mass data
    with open(inputPath) as fileP:

        # Read the first amount
        valueLine = fileP.readline()

        # Do this until there is accounting unit in the file
        while valueLine:

            amount = int(valueLine)

            for sum2Numbers in listSum2Numbers:
                total = amount + listSum2Numbers[sum2Numbers]
                if total ==totalSum:
                    return amount * sum2Numbers[0] * sum2Numbers[1]
            
            for number in listNumbers:
                sum2Numbers = number + amount
                if sum2Numbers not in listSum2Numbers:
                    listSum2Numbers[(amount, number)] = sum2Numbers
            
            if amount not in listNumbers:
                listNumbers.add(amount)

            valueLine = fileP.readline()

print(sum3Numbers('InputD01Q2.txt', 2020))
