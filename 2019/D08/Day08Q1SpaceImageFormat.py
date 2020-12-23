# In this method we compute total fuel requirement for modules

def getDigits(number):
    digits = [int(digit) for digit in number]
    return digits

def getCheckSum(inputPath, width, height):

    # Open file for reading module mass data
    with open(inputPath) as fileP:
        
        # Read image data
        imageFileData = fileP.read().strip()

        digits = getDigits(imageFileData)

        numberOfLayers = len(digits) // (width * height)

        minStats = {'zero': width * height, 'checkSum': 0}
        
        for i in range(0, numberOfLayers):
            currentStart = i * width * height
            currentEnd = currentStart + width * height
            layerElements = digits[currentStart:currentEnd]
            count0 = layerElements.count(0)
            count1 = layerElements.count(1)
            count2 = layerElements.count(2)
            if minStats['zero'] > count0:
                minStats['zero'] = count0
                minStats['checkSum'] = count1 * count2

    return minStats['checkSum']
                
            

        


print(getCheckSum('InputDay08Q1.txt', 25, 6))
