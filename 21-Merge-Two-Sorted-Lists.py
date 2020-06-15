# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head=ListNode(0)
        ptr1=l1
        ptr2=l2
        dummy_head.next=ptr1
        last=dummy_head
        while ptr1 is not None and ptr2 is not None:
            if ptr1.val<ptr2.val:
                last=last.next
                ptr1=ptr1.next
            else:
                last.next=ptr2
                tmp=ptr2.next
                ptr2.next=ptr1
                last=ptr2
                ptr2=tmp
        if ptr1 is None:
            ptr1=ptr2
        last.next=ptr1
        return dummy_head.next
