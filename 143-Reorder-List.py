# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        count=0
        ptr=head
        while ptr:
            count+=1
            ptr=ptr.next
        if count<3:
            return head
        total=count
        middle_cnt=total//2
        count=0
        ptr=head
        while ptr:
            count+=1
            if count==middle_cnt:
                break
            ptr=ptr.next
        rest=None
        if total%2==0:
            rest=ptr.next
            ptr.next=None
        else:
            ptr=ptr.next
            rest=ptr.next
            ptr.next=None
        cur=None
        ptr=rest
        while ptr:
            tmp=ptr.next
            ptr.next=cur
            cur=ptr
            ptr=tmp
        ptr1=head
        ptr2=cur
        while ptr2:
            next=ptr2.next
            ptr2.next=ptr1.next
            ptr1.next=ptr2
            ptr1=ptr2.next
            ptr2=next