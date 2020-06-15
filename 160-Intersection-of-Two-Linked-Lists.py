# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # space O(1)
        dummyA=ListNode(0)
        dummyA.next=headA
        dummyB=ListNode(0)
        dummyB.next=headB
        while headA!=headB:
            if headA and headB:
                headA=headA.next
                headB=headB.next
            elif headA is None:
                headA=dummyB.next
                dummyB.next=None
                headB=headB.next
            elif headB is None:
                headB=dummyA.next
                dummyA.next=None
                headA=headA.next
        return headA

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        record=dict()
        while headA or headB:
            if headA and headA in record:
                return headA
            if headB and headB in record:
                return headB
            if headA==headB:
                return headA
            if headA:
                record[headA]=0
                headA=headA.next
            if headB:
                record[headB]=0
                headB=headB.next
        return None