# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list2_tail=list2
        while list2_tail.next:
            list2_tail=list2_tail.next
        idx=0
        ptr=list1
        cut=None
        cut_tail=None
        while ptr:
            if idx==a-1:
                cut=ptr
            if idx==b+1:
                cut_tail=ptr
            ptr=ptr.next
            idx+=1
        cut.next=list2
        list2_tail.next=cut_tail
        return list1
