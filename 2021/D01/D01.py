import math

def getAllData(inputPath):

    measurements = []
    
    # Open file for reading measurements
    with open(inputPath) as fileP:

        # Read the first measurement
        valueLine = fileP.readline()

        while valueLine:

            measurement = int(valueLine)

            measurements.append(measurement)

            # Read the next measurement
            valueLine = fileP.readline()

    return measurements
            

# This method will compute the measurements that are larger than
# the previous measurements
def largerMeasurement(measurements, sumIndex):

    # Totalcount of measurements that are larger than the previous
    # measurements
    count = 0
    
    # loop over the measurements
    for i in range(len(measurements) - sumIndex + 1):

        # For first index we just do a tmp
        if i == 0:
            tmpMeasurement = sum(measurements[i:i + sumIndex])
            continue

        if sum(measurements[i:i + sumIndex]) > tmpMeasurement:
                count += 1

        tmpMeasurement = sum(measurements[i:i + sumIndex])
        
    return count

# Part 1
print('Part 1:', largerMeasurement(getAllData('Input.txt'), 1))

# Part 2
print('Part 2:', largerMeasurement(getAllData('Input.txt'), 3))
