import timeit
import re
import copy

# This function reads the input file and prepares the data in the needed format
def getInput(inputPath):
    fileP = open(inputPath, 'r')
    
    # this regex will return a list with each line with two steps:
    # [('A', 'B')] where 'B' depends on 'A'
    regex = re.compile('(?:Step (\w)[ \w]*step (\w))')

    return regex.findall(''.join([line.strip() for line in fileP.readlines()]))

# This function returns the dependency list and all tasks to be performed
def getDependencyList(inputData):
    dependencyList = {}
    allSteps = set()
    
    for line in inputData:

        # All Steps on which the current Step needs to wait upon
        if line[1] not in dependencyList:
            dependencyList[line[1]] = set()
        dependencyList[line[1]].add(line[0])

        # Set of all steps that are to be performed
        allSteps.update([line[0], line[1]])

    return [dependencyList, allSteps]

# startSecond is the offset needed to perform a task
# maxWorkers is the number of workers that can work simultaneously
def simulateStepsWithWorkers(dependencyList, allSteps, startSeconds = 60, maxWorkers = 5):

    # Initialize the dictionary for each worker
    workers = {i: {'finishTime': 0, 'step': ''} for i in range(maxWorkers)}

    #Create a deep copy of the dependency list
    depList = copy.deepcopy(dependencyList)

    # The simulation will run per second
    time = -1
    dependencyString = ''
    
    while 1:
        time += 1

        # We identify those workers whose finishTime is current Time or who are waiting for
        # next Step to be performed
        freeWorkers = []
        for workerId in workers:
            if workers[workerId]['finishTime'] == time:
                # If the worker finishes at this time step we need to initialize the
                # worker and add the task to the dependencyString
                freeWorkers.append(workerId)
                workers[workerId]['finishTime'] = 0
                dependencyString += workers[workerId]['step']
                workers[workerId]['step'] = ''
            elif workers[workerId]['finishTime'] == 0:
                freeWorkers.append(workerId)

        # We remove all finished Steps from dependency list
        for step in depList:
            for nextStep in dependencyString:
                depList[step].discard(nextStep)

        # We remove all Steps that do not have any dependency anymore from the dependency list
        depList = {step: depList[step] for step in depList if len(depList[step]) > 0}

        # Get all steps that can be performed at current time step
        nextPossible = sorted([step for step in allSteps
                               if (step not in dependencyString and
                                  step not in depList and
                                  step not in [workers[workerId]['step'] for workerId in workers])])

        # We can only have minimum number of steps starting from the two values below
        maxPossibleSteps = min(len(freeWorkers), len(nextPossible))

        # Assign the workers with the next steps and update the finishTime
        for i in range(maxPossibleSteps):
            workers[freeWorkers[i]]['finishTime'] = time + startSeconds + ord(nextPossible[i]) - 64
            workers[freeWorkers[i]]['step'] = nextPossible[i]

        # If the dependencyString has all Steps we stop processing
        if len(dependencyString) == len(allSteps):
            return [time, dependencyString]

def solveParts(inputData):
    dependencyList, allSteps = getDependencyList(inputData)
    return [
            # For first part we have one worker without any add on to time needed
            simulateStepsWithWorkers(dependencyList, allSteps, startSeconds = 0, maxWorkers = 1),

            # For second part we use the default values for startSeconds and maxWorkers
            simulateStepsWithWorkers(dependencyList, allSteps)]

# This function reads the input data in the format that can be used by solvers        
def solve(inputPath):
    inputData = getInput(inputPath)
    print(solveParts(inputData))

#Timer Start
start = timeit.default_timer()

solve("D07.txt")

# Timer ends
stop = timeit.default_timer()
print('Time: ', stop - start)
