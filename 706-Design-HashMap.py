class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.idx=[-1]*22111
        self.val=[-1]*22111
    
    def hash(self,key):
        return key%22111

    def key(self, key):
        acc=0
        hash=key%22111
        while True:
            if (self.idx[(hash+acc*acc)%22111]==key or self.idx[(hash+acc*acc)%22111]==-1):
                break
            acc+=1
        return (hash+acc*acc)%22111

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx=self.key(key)
        self.idx[idx]=key
        self.val[idx]=value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.val[self.key(key)]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx=self.key(key)
        # self.idx[idx]=-1
        self.val[idx]=-1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)