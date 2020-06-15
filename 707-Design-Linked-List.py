class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy=ListNode(0)
        self.tail=None
        self.total=0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index>=self.total:
            return -1
        count=0
        ptr=self.dummy.next
        while ptr:
            if count==index:
                return ptr.val
            count+=1
            ptr=ptr.next
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        tmp=ListNode(val,self.dummy.next)
        self.dummy.next=tmp
        self.total+=1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        ptr=self.dummy
        tmp=ListNode(val)
        while ptr.next:
            ptr=ptr.next
        ptr.next=tmp
        self.total+=1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index<self.total:
            count=0
            prev=self.dummy
            ptr=prev.next
            while ptr:
                if count==index:
                    tmp=ListNode(val,ptr)
                    prev.next=tmp
                    self.total+=1
                    return
                count+=1
                ptr=ptr.next
                prev=prev.next
        elif index==self.total:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index<self.total:
            count=0
            prev=self.dummy
            ptr=prev.next
            while ptr:
                if count==index:
                    prev.next=ptr.next
                    self.total-=1
                    return
                count+=1
                ptr=ptr.next
                prev=prev.next
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)