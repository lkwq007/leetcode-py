class Node:
    def __init__(self,cap,idx):
        self.next=None
        self.prev=None
        self.vals=[0]*cap
        self.top=-1
        self.idx=idx
class DinnerPlates:

    def __init__(self, capacity: int):
        self.head=Node(capacity,-1)
        self.tail=self.head
        self.cap=capacity
        self.mapping={}

    def push(self, val: int) -> None:
        if self.head.prev==self.head:
            node=Node(self.cap,0)
            node.next=self.head
            node.prev=self.head
            self.head.next=node
            self.head.prev=node
        

    def pop(self) -> int:
        if self.head.prev==self.head:
            return -1
        return self.popAtStack(self.head.prev.idx)

    def popAtStack(self, index: int) -> int:
        if index not in self.mapping:
            return -1
        stack=self.mapping[index]
        ret=stack.vals[stack.top]
        stack.top-=1
        if stack.top<0:
            del self.mapping[index]
        stack.next.prev=stack.prev
        stack.prev.next=stack.next
        return ret
            


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)