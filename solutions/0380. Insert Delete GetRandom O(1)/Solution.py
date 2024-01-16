import random


class RandomizedSet:

    def __init__(self):
        self.itemMap = {}
        self.itemList = []

    def insert(self, val: int) -> bool:
        isNotExists = val not in self.itemMap
        if isNotExists:
            self.itemMap[val] = len(self.itemList)
            self.itemList.append(val)        
        return isNotExists        

    def remove(self, val: int) -> bool:
        isExists = val in self.itemMap
        if isExists:
            idx = self.itemMap[val]
            lastItem = self.itemList[-1]
            self.itemList[idx] = lastItem
            self.itemMap[lastItem] = idx
            self.itemList.pop()
            del self.itemMap[val]
        return isExists
        

    def getRandom(self) -> int:
        return random.choice(self.itemList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()