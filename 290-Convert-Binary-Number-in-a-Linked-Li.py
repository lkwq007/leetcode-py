# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ptr=head
        ret=0
        while ptr:
            ret*=2
            ret+=ptr.val
            ptr=ptr.next
        return ret

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ret=0
        while head:
            ret=2*ret+head.val
            head=head.next
        return ret