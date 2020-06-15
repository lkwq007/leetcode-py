# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_head=ListNode(0)
        dummy_head.next=head
        last=dummy_head
        count=0
        if k<2:
            return head
        while head:
            count+=1
            if count==k:
                count=0
                seg_prev=last
                seg_next=head.next
                ptr=last.next
                last=ptr
                next=ptr.next
                while ptr!=head:
                    tmp=seg_prev.next
                    seg_prev.next=ptr
                    next=ptr.next
                    ptr.next=tmp
                    ptr=next
                else:
                    tmp=seg_prev.next
                    seg_prev.next=head
                    head.next=tmp
                last.next=seg_next
                head=seg_next
            else:
                head=head.next
        return dummy_head.next        