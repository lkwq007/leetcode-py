# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k<1 or head is None:
            return head
        count=0
        dummy_head=ListNode(0)
        dummy_head.next=head
        last=dummy_head
        tail=dummy_head.next
        while head:
            count+=1
            if count>k:
                last=last.next
            tail=head
            head=head.next
        total=count
        if k>=total:
            k=k%total
            if k==0:
                return dummy_head.next
            count=0
            head=dummy_head.next
            last=dummy_head
            while head:
                count+=1
                if count>k:
                    last=last.next
                head=head.next
        head=dummy_head.next
        dummy_head.next=last.next
        tail.next=head
        last.next=None
        return dummy_head.next
        

        