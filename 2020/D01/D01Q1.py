import math

# This method will compute the two numbers who sum to given number and return
# the multiple
def sum2Numbers(inputPath, totalSum):

    listRestSum = set()
    
    # Open file for reading module mass data
    with open(inputPath) as fileP:

        # Read the first amount
        valueLine = fileP.readline()

        # Do this until there is accounting unit in the file
        while valueLine:

            amount = int(valueLine)
            
            if amount in listRestSum:
                return amount * ( totalSum - amount )

            restAmount = totalSum - amount

            listRestSum.add(restAmount)

            valueLine = fileP.readline()

print(sum2Numbers('InputD01Q1.txt', 2020))
