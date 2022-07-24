class ListNode:
    def __init__(self,val=0,dummy=False):
        self.val=val
        self.dummy=dummy
        self.prev=None
        self.next=None

class FrontMiddleBackQueue:

    def __init__(self):
        self.front=ListNode(dummy=True)
        self.back=ListNode(dummy=True)
        self.middle=ListNode(dummy=True)
        self.front.next=self.middle
        self.middle.next=self.back
        self.back.prev=self.middle
        self.middle.prev=self.front
        self.total=0

    def move2front(self):
        pass
    def move2back(self):
        pass
    def insert_after(self,val,ptr):
        node=ListNode(val)
        node.prev=ptr
        node.next=ptr.next
        ptr.next=node
        node.next.prev=node

    def pushFront(self, val: int) -> None:
        self.insert_after(val,self.front)
        if self.total%2==0:
            self.move2front()
        self.total+=1

    def pushMiddle(self, val: int) -> None:
        self.insert_after(val,self.middle)
        if self.total%2==1:
            self.move2back()
        self.total+=1

    def pushBack(self, val: int) -> None:
        self.insert_after(val,self.back.prev)
        if self.total%2==0:
            self.move2front()
        else:
            self.move2back()
        self.total+=1

    def popFront(self) -> int:
        

    def popMiddle(self) -> int:
        

    def popBack(self) -> int:
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()