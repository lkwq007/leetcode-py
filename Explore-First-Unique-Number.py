class ListNode:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.queue=nums
        self.mapping={}
        self.unique=ListNode(None)
        self.unique.next=self.unique
        self.unique.prev=self.unique
        for item in nums:
            self.update(item)

    def update(self,item):
        if item in self.mapping:
            node=self.mapping[item]
            if node:
                node.prev.next=node.next
                node.next.prev=node.prev
                self.mapping[item]=None
        else:
            node=ListNode(item)
            self.mapping[item]=node
            node.prev=self.unique.prev
            node.next=self.unique
            node.prev.next=node
            node.next.prev=node

    def showFirstUnique(self) -> int:
        if self.unique.next==self.unique:
            return -1
        else:
            return self.unique.next.val

    def add(self, value: int) -> None:
        self.queue.append(value)
        self.update(value)



# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)