# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        ptr=head
        while ptr:
            if hasattr(ptr,"m"):
                return True
            ptr.m=0
            ptr=ptr.next
        return False

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        ptr_slow=head
        ptr_fast=head
        while True:
            if ptr_slow is None or ptr_fast is None or ptr_fast.next is None:
                return False
            ptr_slow=ptr_slow.next
            ptr_fast=ptr_fast.next.next
            if ptr_slow==ptr_fast:
                return True
        return False