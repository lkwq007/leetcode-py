# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_head=ListNode(0)
        dummy_head.next=head
        rest=ListNode(0)
        rest.next=None
        last=dummy_head
        rest_head=rest
        while head:
            if head.val<x:
                last=head
                head=head.next
            else:
                rest_head.next=head
                rest_head=head
                tmp=head.next
                head.next=None
                head=tmp
                last.next=head
        last.next=rest.next
        return dummy_head.next