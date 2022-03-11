class ListNode():
    def __init__(self) -> None:
        self.val=0
        self.prev=None
        self.next=None

class FrontMiddleBackQueue:

    def __init__(self):
        self.head=ListNode()
        self.tail=ListNode()
        self.middle=self.head
        self.head.next=self.tail
        self.tail.prev=self.head
        self.cnt=0

    def pushFront(self, val: int) -> None:
        self.cnt+=1
        node=ListNode()
        node.val=val
        node.next=self.head.next
        self.head.next=node
        node.prev=self.head
        node.next.prev=node
        if self.cnt%2

    def pushMiddle(self, val: int) -> None:
        self.cnt+=1
        node=ListNode()
        node.val=val
        node.next=self.middle.next
        self.middle.next=node
        node.prev=self.middle
        node.next.prev=node

    def pushBack(self, val: int) -> None:
        self.cnt+=1
        node=ListNode()
        node.val=val
        node.next=self.tail
        node.prev=self.tail.prev
        self.tail.prev=node
        node.prev.next=node


    def popFront(self) -> int:
        if self.cnt==0:
            return -1
        self.cnt-=1
        ptr=self.head.next
        self.head.next=ptr.next
        ptr.next.prev=self.head
        return ptr.val

    def popMiddle(self) -> int:
        if self.cnt==0:
            return -1
        self.cnt-=1
        ptr=self.middle.next
        self.middle.next=ptr.next
        ptr.next.prev=self.middle
        if self.cnt%2==0:
            self.middle=self.middle.prev
        return ptr.val

    def popBack(self) -> int:
        if self.cnt==0:
            return -1
        self.cnt-=1
        ptr=self.tail.prev
        self.tail.prev=ptr.prev
        ptr.prev.next=self.tail
        return ptr.val

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()