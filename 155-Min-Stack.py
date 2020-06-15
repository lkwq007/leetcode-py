class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
        self.min=None

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dummy=Node(0)
        self.min=None
        self.total=0

    def push(self, x: int) -> None:
        self.total+=1
        tmp=Node(x,self.dummy.next)
        if self.min is None:
            self.min=x
            tmp.min=x
        elif self.min>x:
            self.min=x
            tmp.min=x
        else:
            tmp.min=self.min
        self.dummy.next=tmp

    def pop(self) -> None:
        if self.total>0:
            tmp=self.dummy.next
            self.dummy.next=tmp.next
            self.total-=1
            if self.total>0:
                self.min=self.dummy.next.min
            else:
                self.min=None

    def top(self) -> int:
        if self.total>0:
            return self.dummy.next.val

    def getMin(self) -> int:
        if self.total>0:
            return self.dummy.next.min
        
def dump(x):
    ptr=x
    while ptr:
        print(ptr.val,ptr.next)
        ptr=ptr.next

minStack=MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
dump(minStack.dummy)
minStack.getMin()
minStack.pop()
minStack.top()   
minStack.getMin()
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()