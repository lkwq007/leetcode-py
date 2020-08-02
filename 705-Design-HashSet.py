class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst=[-1]*20011
    
    def search(self,key):
        idx=key%20011
        i=1
        while self.lst[idx]!=key and self.lst[idx]!=-1:
            idx+=i
            i+=i
            idx=idx%20011
        return idx


    def add(self, key: int) -> None:
        idx=self.search(key)
        if self.lst[idx]==-1:
            self.lst[idx]=key

    def remove(self, key: int) -> None:
        idx=self.search(key)
        if self.lst[idx]==key:
            self.lst[idx]=-1

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx=self.search(key)
        return self.lst[idx]==key        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)