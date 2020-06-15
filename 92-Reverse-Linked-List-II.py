# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy_head=ListNode(0)
        dummy_head.next=head
        prev=dummy_head
        ptr=head
        count=0
        tail=None
        current=None
        while ptr:
            count+=1
            if m<=count<=n:
                tmp=ptr.next
                ptr.next=current
                current=ptr
                ptr=tmp
                if count==n:
                    tmp=prev.next
                    prev.next=current
                    tmp.next=ptr
            else:
                prev=prev.next
                ptr=ptr.next
        return dummy_head.next

            
            
                