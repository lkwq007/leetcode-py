# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack=[]
        ptr1=head
        ptr2=head
        while ptr2:
            stack.append(ptr1.val)
            ptr1=ptr1.next
            ptr2=ptr2.next.next
        ret=0
        while ptr1:
            ret=max(ret,ptr1.val+stack[-1])
            stack.pop()
            ptr1=ptr1.next
        return ret