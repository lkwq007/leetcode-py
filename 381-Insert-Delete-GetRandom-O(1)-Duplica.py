import random
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapping={}
        self.lst=[]

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        idx=len(self.lst)
        self.lst.append(val)
        flag=False
        if val not in self.mapping:
            self.mapping[val]={}
            flag=True
        self.mapping[val][idx]=1
        return flag
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.mapping or len(self.mapping[val])<1:
            return False
        idx=next(iter(self.mapping[val].keys()))
        target_idx=len(self.lst)-1
        del self.mapping[val][idx]
        if idx!=target_idx:
            target_val=self.lst[target_idx]
            del self.mapping[target_val][target_idx]
            self.lst[idx]=target_val
            self.mapping[target_val][idx]=1
        self.lst.pop()
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        idx=random.randrange(0,len(self.lst))
        return self.lst[idx]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()