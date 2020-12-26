import timeit

def isValid(newPass):
    doubles = []
    isTriple = False
    for index, digit in enumerate(newPass):
        if digit in [105, 111, 108]:
            return False
        if index - 1 not in doubles and index < len(newPass) - 1 and digit == newPass[index + 1]:
            doubles.append(index)
        if index < len(newPass) - 2 and digit == newPass[index + 1] - 1 and digit == newPass[index + 2] - 2:
            isTriple = True

    if isTriple and len(doubles) == 2:
        return True

    return False

def solve(inputString):
    newPass = [ord(digit) for digit in inputString]
    ranAlready = True
    while not isValid(newPass) or ranAlready:
        newPass[-1] += 1
        ranAlready, counter = False, -1
        while newPass[counter] > 122: #z
            newPass[counter] = 97 #a
            counter -= 1
            newPass[counter] += 1

    return ''.join(chr(digit) for digit in newPass)
    
#Timer Start
start = timeit.default_timer()

newPass = solve('hxbxwxba')
newPass2 = solve(newPass)
print(newPass, newPass2)

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
