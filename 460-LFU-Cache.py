class ListNode:
    def __init__(self):
        self.val=0
        self.next=None
        self.prev=None

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.mapping={}
        self.cnt={}

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        self.cnt[key]+=1
        return self.mapping[key]

    def put(self, key: int, value: int) -> None:
        self.mapping[key]=value
        if key not in self.cnt:
            self.cnt[key]=1
        else:
            self.cnt[key]+=1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)