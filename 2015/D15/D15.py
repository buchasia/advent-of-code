import timeit

def getInput():
    return {'Frosting': {'capacity': 4, 'durability': -2, 'flavor': 0, 'texture': 0, 'calories': 5},
            'Candy': {'capacity': 0, 'durability': 5, 'flavor': -1, 'texture': 0, 'calories': 8},
            'Butterscotch': {'capacity': -1, 'durability': 0, 'flavor': 5, 'texture': 0, 'calories': 6},
            'Sugar': {'capacity': 0, 'durability': 0, 'flavor': -2, 'texture': 2, 'calories': 1}}

def getContent(inputData, calories = 0):
    maxScore = 0
    for i in range(0, 101):
        for j in range(0, 101):
            for k in range(0, 101):
                l = 100 - i - j - k
                if l < 0:
                    continue

                sumDict = {feature: (inputData['Frosting'][feature] * i +
                                     inputData['Candy'][feature] * j +
                                     inputData['Butterscotch'][feature] * k +
                                     inputData['Sugar'][feature] * l)
                           for feature in inputData['Frosting']}

                score = 1
                for feature in sumDict:
                    if sumDict[feature] < 0:
                        score = 0
                    else:
                        if feature != 'calories':
                            score *= sumDict[feature]

                if score > maxScore and (calories == 0 or sumDict['calories'] == calories):
                        maxScore = score

    return maxScore           

def solve():
    inputData = getInput()

    print([getContent(inputData),
           getContent(inputData, calories = 500)])

#Timer Start
start = timeit.default_timer()

solve()

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
