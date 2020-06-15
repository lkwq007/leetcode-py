# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carrier=0
        head=l1
        last=l1
        while l1 is not None and l2 is not None:
            l1.val+=l2.val+carrier
            if l1.val>9:
                l1.val-=10
                carrier=1
            else:
                carrier=0
            last=l1
            l1=l1.next
            l2=l2.next
        if l1 is None:
            last.next=l2
            l1=l2
        while True:
            if l1 is None:
                if carrier>0:
                    last.next=ListNode(1)
                break
            l1.val+=carrier
            if l1.val>9:
                l1.val-=10
                carrier=1
            else:
                carrier=0
            last=l1
            l1=l1.next
        return head