# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        def listlen(ptr):
            count=0
            while ptr:
                count+=1
                ptr=ptr.next
            return count            
        len1_=listlen(l1)
        len2_=listlen(l2)
        if len2_>len1_:
            l1,l2=l2,l1
            len1_,len2_=len2_,len1_
        def add(ptr1,ptr2,len1,len2):
            if ptr1 is None and ptr2 is None:
                return 0
            # return carry flag
            if len1==len2:
                carry=add(ptr1.next,ptr2.next,len1,len2)
                ptr1.val+=ptr2.val+carry
            else:
                carry=add(ptr1.next,ptr2,len1-1,len2)
                ptr1.val+=carry
            if ptr1.val>=10:
                ptr1.val-=10
                ret=1
            else:
                ret=0
            return ret
        carry=add(l1,l2,len1_,len2_)
        if carry:
            head=ListNode(1)
            head.next=l1
        else:
            head=l1
        return head