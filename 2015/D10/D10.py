import timeit

def solve(inputString, iteration = [40, 50]):
    newList = [int(digit) for digit in inputString]
    for i in range(iteration[1]):
        currentList, newList, lastDigit = list(newList), [], -1
        for digit in currentList:
            if lastDigit != digit:
                if lastDigit != -1:
                    newList += [counter, lastDigit]
                counter, lastDigit = 1, digit
            else:
                 counter += 1

        newList += [counter, lastDigit]
        
        if i + 1 in iteration:
            print(len(newList))

#Timer Start
start = timeit.default_timer()

solve("1113222113")

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
