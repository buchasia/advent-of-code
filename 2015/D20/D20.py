import timeit
import math
from threading import Thread

def sumDiv(number):
    maxD = int(math.sqrt(number))
    count = 1
    for i in range(2, maxD + 1):
        if number % i == 0:
            count += i
            if number % i != i:
                count += number // i
    return count    

# The elvs visit only the first 50 Houses.
def solve2(presentCount, presentMultiplier):
    count = 0
    presentSum = {}
    minCount = presentCount
    while minCount > count:
        count += 1
        currentPresentCount = count * presentMultiplier
        for i in range(1, 51):
            currentHouse = i * count
            if currentHouse in presentSum:
                presentSum[currentHouse] += currentPresentCount
            else:
                presentSum[currentHouse] = currentPresentCount

            if presentSum[currentHouse] > presentCount:
                if minCount > currentHouse:
                    minCount = currentHouse
    print('P2:', minCount)

# The elvs visit infinite houses, it is similar to computing the sum of all
# divisors
def solve1(presentCount, presentMultiplier):
    count = 0
    currentSum = 0
    while currentSum < presentCount:
        count += 1
        summing = sumDiv(count)
        currentSum = (summing + count if count != 1 else 0) * presentMultiplier
    print('P1:', count)

t1, t2 = Thread(target=solve1, args=(34000000, 10)), Thread(target=solve2, args=(34000000, 11))
t1.start()
t2.start()
