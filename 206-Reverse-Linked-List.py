# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # without dummy
        prev=None
        ptr=head
        while ptr:
            tmp=ptr.next
            ptr.next=prev
            prev=ptr
            ptr=tmp
        return ptr

            
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy_head=ListNode(0)
        dummy_head.next=None
        prev=dummy_head
        ptr=head
        while ptr:
            tmp=ptr.next
            ptr.next=dummy_head.next
            dummy_head.next=ptr
            ptr=tmp
        return dummy_head.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # rec
        def reverse(ptr):
            if ptr.next is None:
                return ptr, ptr
            prev, head=reverse(ptr.next)
            prev.next=ptr
            return ptr, head
        if head:
            ptr,ret=reverse(head)
            ptr.next=None
            return ret
        else:
            return head