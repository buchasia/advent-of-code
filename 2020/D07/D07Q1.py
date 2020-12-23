def solveQuestion(inputPath, searchBag):
    
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()
    
    bagsContent = {}
    searchBags = []
    
    for valueLine in fileLines:
        valueLine = str(valueLine).rstrip("\n")

        [bagType, contentText] = valueLine.split(' contain ')

        bagType = bagType.split(' bags')
        
        # The content is in the format: 3 pale red bags, 1 clear teal bag.
        # We split with space we will get ['3', 'pale', 'red', 'bags,', '1',...]
        # Then the second, third, 6th, 7th are the bag types
        contents = contentText.split(' ')
        counter = 1
        while counter < len(contents):
            contentName = contents[counter] + ' ' + contents[counter + 1]
            if contentName not in bagsContent:
                bagsContent[contentName] = [bagType[0]]
            else:
                bagsContent[contentName].append(bagType[0])
            counter += 4
    
    searchBags = [searchBag]
    counter = 0
    while counter < len(searchBags):
        currentBag = searchBags[counter]
            
        if currentBag in bagsContent:
            for bag in bagsContent[currentBag]:
                if bag not in searchBags:
                    searchBags.append(bag)
                        
        counter += 1

    return len(searchBags) - 1

print(solveQuestion('InputD07Q1.txt', 'shiny gold'))
