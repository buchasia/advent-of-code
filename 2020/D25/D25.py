import timeit

def solveParts(doorsSubject, cardsSubject):
    nextNumber = 7
    encryptionKey = doorsSubject
    while nextNumber != cardsSubject:
        nextNumber = (nextNumber * 7) % 20201227
        encryptionKey = (encryptionKey * doorsSubject) % 20201227

    return encryptionKey
                
def solve(doorsSubject, cardsSubject):
    print([solveParts(doorsSubject, cardsSubject)])

#Timer Start
start = timeit.default_timer()

solve(5099500, 7648211)

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
