# This will return digits of a number. For example:
# 34569 = ['3', '4', '5', '6', '9']
def getDigits(number):
    digits = [int(digit) for digit in str(number)]
    return digits
    
def getNumber(digits):
    # Converting integer list to string list 
    strDigits = [str(digit) for digit in digits] 
      
    # Join list items using join() 
    number = int("".join(strDigits))

    return number

def hasDuplicate(digits):
    uniqueDigits = set(digits)
    if len(uniqueDigits) < len(digits):
        tempDigit = 0
        for digit in digits:
            if tempDigit == digit:
                return True
            else:
                tempDigit = digit
        return True
    else:
        return False

def isIncreasing(digits):
    tempDigit = digits[0]
    for digit in digits:
        if tempDigit > digit:
            return False
        tempDigit = digit
    return True

def isValidPassword(digits):
    if isIncreasing(digits) and hasDuplicate(digits):
        return True
    else:
        return False

def getNextNumber(digits):
    currentIndex = len(digits) - 1
    digits[currentIndex] += 1
    while digits[currentIndex] > 9:
        digits[currentIndex] -= 10
        currentIndex -= 1
        if currentIndex < 0:
            exit
        digits[currentIndex] += 1
    return digits

def minSecureContainer(minRange, maxRange):
    digits = getDigits(minRange)
    number = minRange
    listValidPass = []
    while number <= maxRange:
        if isValidPassword(digits):
            listValidPass.append(number)
        digits = getNextNumber(digits)
        number = getNumber(digits)
    return listValidPass
    
    
print(len(minSecureContainer(234208, 765869)))
