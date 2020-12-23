# In this method we compute total fuel requirement for modules

def getDigits(number):
    digits = [digit for digit in number]
    return digits

def printDecodedImage(width, height, decodedImageData):
    for i in range(0, height):
        currentStart = i * width
        currentEnd = (i + 1) * width
        print(''.join(decodedImageData[currentStart:currentEnd]))
    
def getDecodedImage(inputPath, width, height):

    # Open file for reading module mass data
    with open(inputPath) as fileP:
        
        # Read image data
        imageFileData = fileP.read().strip()

        digits = getDigits(imageFileData)

        layerLength = width * height
        
        numberOfLayers = len(digits) // layerLength

        remainingIndex = range(0, layerLength)
        
        for i in range(0, numberOfLayers):
            currentStart = i * layerLength
            currentEnd = currentStart + layerLength
            layerElements = digits[currentStart:currentEnd]
            nextIndex = []
            # first Layer
            if i == 0:
                decodedImage = layerElements

            for j in remainingIndex:
                if decodedImage[j] != '2':
                    continue                    
                else:
                    decodedImage[j] = layerElements[j]
                    if decodedImage[j] == '2':
                        nextIndex.append(j)
                    
            remainingIndex = nextIndex
            
    printDecodedImage(width, height, decodedImage)

getDecodedImage('InputDay08Q2.txt', 25, 6)
