# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head=ListNode(0)
        dummy_head.next=head
        prev=dummy_head
        ptr=head
        while ptr:
            if ptr.val==val:
                prev.next=ptr.next
                ptr=ptr.next
            else:
                prev=ptr
                ptr=ptr.next
        return dummy_head.next