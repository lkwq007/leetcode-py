# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy_head=ListNode(0)
        even_head=ListNode(0)
        dummy_head.next=head
        prev=dummy_head
        even_prev=even_head
        ptr=head
        count=0
        while ptr:
            if ptr.next:
                tmp=ptr.next
                ptr.next=tmp.next
                even_prev.next=tmp
                tmp.next=None
                prev=ptr
                ptr=ptr.next
                even_prev=even_prev.next
            else:
                break
        if ptr:
            ptr.next=even_head.next
        else:
            prev.next=even_head.next
        return dummy_head.next