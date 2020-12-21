def solveQuestion(iteration):

    states = {'A': {0: {'value': 1, 'direction': 1, 'nextState': 'B'},
                    1: {'value': 0, 'direction': -1, 'nextState': 'C'}},
              'B': {0: {'value': 1, 'direction': -1, 'nextState': 'A'},
                    1: {'value': 1, 'direction': 1, 'nextState': 'D'}},
              'C': {0: {'value': 0, 'direction': -1, 'nextState': 'B'},
                    1: {'value': 0, 'direction': -1, 'nextState': 'E'}},
              'D': {0: {'value': 1, 'direction': 1, 'nextState': 'A'},
                    1: {'value': 0, 'direction': 1, 'nextState': 'B'}},
              'E': {0: {'value': 1, 'direction': -1, 'nextState': 'F'},
                    1: {'value': 1, 'direction': -1, 'nextState': 'C'}},
              'F': {0: {'value': 1, 'direction': 1, 'nextState': 'D'},
                    1: {'value': 1, 'direction': 1, 'nextState': 'A'}}}

#    states = {'A': {0: {'value': 1, 'direction': 1, 'nextState': 'B'},
#                   1: {'value': 0, 'direction': -1, 'nextState': 'B'}},
#             'B': {0: {'value': 1, 'direction': -1, 'nextState': 'A'},
#                   1: {'value': 1, 'direction': 1, 'nextState': 'A'}}}

    slots = {}
    currentSlotIndex = 0

    slots[0] = 0
    currentState = 'A'
    for i in range(iteration):
        if currentSlotIndex in slots:
            currentStateTemp = states[currentState][slots[currentSlotIndex]]['nextState']
            currentSlotIndexTemp = states[currentState][slots[currentSlotIndex]]['direction']
            slots[currentSlotIndex] = states[currentState][slots[currentSlotIndex]]['value']
            currentState = currentStateTemp
            currentSlotIndex += currentSlotIndexTemp
        else:
            slots[currentSlotIndex] = states[currentState][0]['value']
            currentSlotIndex += states[currentState][0]['direction']
            currentState = states[currentState][0]['nextState']

    return sum([value for index, value in slots.items()])
            
            
    

    
print(solveQuestion(12667664))
