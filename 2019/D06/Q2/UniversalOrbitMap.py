class UniversalOrbitMap:
    # orbitMap is a dictionary. An example:
    # { 'A' : {'master': 'B', 'parent': 'C', 'path': '001.001.001' 'childCount': 2} }
    def __init__(self):
        self.orbitMap = {}

    def addToMap(self, around, orbiter):
        if around not in self.orbitMap:
            self.orbitMap[around] = self.createNewOrbit(around)
            
        if orbiter not in self.orbitMap:
            self.orbitMap[orbiter] = self.createNewOrbit(orbiter)

        self.updateOrbiterMap(around, orbiter)
        
    def createNewOrbit(self, objectName):
        
        orbitMap = {}
        orbitMap['master'] = objectName
        if objectName != 'COM':
            orbitMap['parent'] = objectName
        else:
            orbitMap['parent'] = ''
        orbitMap['path'] = '001'
        orbitMap['childCount'] = 0

        return orbitMap

    def updateOrbiterMap(self, around, orbiter):
        self.orbitMap[around]['childCount'] += 1
        childPath = str(self.orbitMap[around]['childCount']).zfill(3)
        basePath = self.orbitMap[around]['path'] + '.' + childPath 
        self.orbitMap[orbiter]['path'] = basePath
        self.orbitMap[orbiter]['parent'] = around
        self.orbitMap[orbiter]['master'] = self.orbitMap[around]['master']

        self.updateChildWithBasePath(orbiter, basePath)

    def updateChildWithBasePath(self, orbiter, basePath):
        toModifyParent = [orbiter]
        while len(toModifyParent) > 0:
            currentParent = toModifyParent[0]
            toModifyParent.pop(0)
            for oMapObject in self.orbitMap:
                if self.orbitMap[oMapObject]['parent'] != currentParent:
                    continue
                toModifyParent.append(oMapObject)
                self.orbitMap[oMapObject]['path'] = basePath + self.orbitMap[oMapObject]['path'][3:]
                self.orbitMap[oMapObject]['master'] = self.orbitMap[currentParent]['master']

    def getAllOrbits(self):
        totalOrbit = 0
        for oMapObject in self.orbitMap:
            totalOrbit += len(self.orbitMap[oMapObject]['path'].split('.')) -  1
        return totalOrbit

    def getOrbitMap(self):
        return self.orbitMap

    def getNumberOfOrbitalTransfer(self, fromObject, toObject):
        fromPath = self.getPath(fromObject)
        toPath = self.getPath(toObject)
        lenFromPath = len(fromPath)
        lenToPath = len(toPath)
        maxLength = lenFromPath if lenFromPath > lenToPath else lenToPath

        for i in range(0, maxLength):
            if fromPath[i] != toPath[i]:
                lastCommonIndex = i
                break

        return [fromPath, toPath, lenToPath + lenFromPath - 2 * ( i + 1 ) ]
            

        print(fromPath)
        print(toPath)

    def getPath(self, oMapObject):
        pathList = [oMapObject]
        childList = [oMapObject]
        while len(childList) > 0:
            currentChild = childList[0]
            childList.pop(0)
            currentParent = self.orbitMap[currentChild]['parent']
            if currentParent == '':
                break
            pathList.insert(0, currentParent)
            childList.append(currentParent)

        return pathList
