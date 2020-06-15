# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count=0
        ptr=head
        while ptr:
            count+=1
            ptr=ptr.next
        ptr=head
        middle_cnt=count//2
        count=0
        while ptr:
            if count==middle_cnt:
                break
            count+=1
            ptr=ptr.next
        return ptr