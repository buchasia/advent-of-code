def solveQuestion(inputPath):    
    fileP = open(inputPath, 'r')
    fileLines= fileP.readlines()
    fileP.close()

    counter = -1
    particles = {}
    for line in fileLines:
        counter += 1
        line = line.strip()

        [otherVal, accText] = line.split('>, a=<')
        accValues = list(map(int, accText[:-1].split(',')))

        [otherVal, velText] = otherVal.split('>, v=<')
        velValues = list(map(int, velText.split(',')))

        [otherVal, posText] = otherVal.split('p=<')
        posValues = list(map(int, posText.split(',')))

        particles[counter] = {}
        particles[counter]['p'] = posValues
        particles[counter]['v'] = velValues
        particles[counter]['a'] = accValues

    for t in range(1, 10000):
        for particle in particles:
            for i in range(3):
                particles[particle]['v'][i] += particles[particle]['a'][i]
                particles[particle]['p'][i] += particles[particle]['v'][i]
        positions = {}
        for particle in particles:
            if (particles[particle]['p'][0], particles[particle]['p'][1], particles[particle]['p'][2]) in positions:
                positions[(particles[particle]['p'][0], particles[particle]['p'][1], particles[particle]['p'][2])].append(particle)
            else:
                positions[(particles[particle]['p'][0], particles[particle]['p'][1], particles[particle]['p'][2])] = [particle]

        for position in positions:
            if len(positions[position]) > 1:
                for index in positions[position]:
                    particles.pop(index)
    return len(particles)
        
print(solveQuestion('InputD20Q2.txt'))
