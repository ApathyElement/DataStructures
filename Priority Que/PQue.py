class PriorityQue(object):
    def __init__(self,inarr):
        self.posDict = {}
        #from node values to position indecies
        self.treeArr = []
        for _ in inarr:
            self.insert(_)

    def getPosition(self, val):
        if val in self.posDict:
            return self.posDict[val][-1]
        else:
            return None

    def insertPosition(self, val, position):
        if val in self.posDict:
            self.posDict[val].append(position)
        else:
            self.posDict[val] = [position] 

    def removePosition(self, val, position):
        if val not in self.posDict:
            return False
        else:
            if position not in self.posDict[val]:
                return False
            else:
                self.posDict[val].remove(position)
                if len(self.posDict[val]) == 0:
                    del self.posDict[val]
                return True

    def getLeftChildValue(self, index):
        child = self.getLeftChild(index)
        return self.treeArr[child] if child is not None else None

    def getRightChildValue(self, index):
        child = self.getRightChild(index)
        return self.treeArr[child] if child is not None else None

    def getParentValue(self, index):
        parent = self.getParent(index)
        return self.treeArr[parent] if parent is not None else None
            
    def getLeftChild(self, index):
        ind = 2*index + 1
        return ind if ind <= self.lastElementPos else None

    def getRightChild(self, index):
        ind =  2*index + 2
        return ind if ind <= self.lastElementPos else None

    def getParent(self, index):
        if index == 0:
            return None
        if index % 2 == 0:
            return int((index - 2)/2)
        else:
            return int((index - 1)/2)

    def getValue(self, index):
        if self.lastElementPos == -1:
            return None
        return self.treeArr[index]

    def swap(self, ind1, ind2):
        if ind1 == ind2:
            return None
        if ind1 < 0 or ind2 < 0:
            return None
        self.removePosition(self.getValue(ind1),ind1)
        self.removePosition(self.getValue(ind2), ind2)
        self.insertPosition(self.getValue(ind2),ind1)
        self.insertPosition(self.getValue(ind1), ind2)

        self.treeArr[ind1], self.treeArr[ind2] = self.getValue(ind2), self.getValue(ind1)

    def insert(self, x):
        self.treeExtend(x)
        self.bubble(self.lastElementPos)

    def removeByIndex(self, x):
        if self.getLeftChildValue(x) == None and self.getRightChildValue(x) == None:
            self.removePosition(self.getValue(x),x)
            self.treeArr.pop(x)
        else:
            self.swap(x, self.lastElementPos)
            self.removeByIndex(self.lastElementPos)
            self.bubble(x)

    def remove(self, x):
        index = self.getPosition(x)
        if index is not None:
            self.removeByIndex(index)
            return True
        else:
            return False

    def peek(self):
        if self.lastElementPos >= 0:
            return self.getValue(0)
        else:
            return None

            

    def poll(self):
        if self.lastElementPos >= 0:
            temp = self.getValue(0)
            self.swap(0, self.lastElementPos)
            self.removeByIndex(self.lastElementPos)
            self.bubble(0)
            return temp
        else:
            return None


    def greaterThanEq(self, x, y): # x >= y
        if x is None and y is None:
            return True
        if x is None:
            return False
        if y is None:
            return True
        return True if x >= y else False

    def greaterThan(self, x, y): # x > y
        if x is None and y is None:
            return False
        if x is None:
            return False
        if y is None:
            return False
        return True if x > y else False

    def bubble(self, index):
        tempIndex = self.bubbleUp(index)
        self.bubbleDown(tempIndex)

    def isleaf(self,index):
        if self.getLeftChildValue(index) == None and self.getRightChildValue(index) == None:
            return True
        else:
            return False
        

    def bubbleUp(self, index):
        if not self.greaterThanEq(self.getValue(index), self.getParentValue(index)):
            self.swap(index, self.getParent(index))
            return self.bubbleUp(self.getParent(index))
        return index

    def bubbleDown(self, index):
        if self.isleaf(index):
            return index

        if self.greaterThan(self.getLeftChildValue(index),self.getRightChildValue(index)):
            minIndex, maxIndex = self.getRightChild(index), self.getLeftChild(index)
        else:
            maxIndex, minIndex = self.getRightChild(index), self.getLeftChild(index)

            # maxIndex is the index of child with greatest value

        if minIndex != None:
            if self.greaterThan(self.getValue(index), self.getValue(minIndex)):
                self.swap(index, minIndex)
                return self.bubbleDown(minIndex)

        if maxIndex != None:
            if self.greaterThan(self.getValue(index), self.getValue(maxIndex)):
                self.swap(index, maxIndex)
                return self.bubbleDown(maxIndex)

        return index


    @property
    def lastElementPos(self):
        return  len(self.treeArr) - 1 if len(self.treeArr) - 1 >= 0 else -1


    def treeExtend(self, x):
        self.treeArr.append(x)
        self.insertPosition(x,self.lastElementPos)

    def __str__(self):
        return str(self.treeArr) + ' - ' + str(self.posDict)

