# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                break
        else:
            return None
        ptr=head
        while ptr!=slow:
            ptr=ptr.next
            slow=slow.next
        return ptr

def linked_list(lst):
    dummy_head=ListNode(0)
    tmp=ListNode(0)
    dummy_head.next=tmp
    prev=tmp
    for item in lst:
        node=ListNode(item)
        prev.next=node
        prev=node
    prev.next=tmp.next
    return dummy_head

x=Solution()
lst=linked_list([-10,-3,0,5,9])
x.detectCycle(lst)


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        record=dict()
        ptr=head
        while ptr:
            if ptr in record:
                return ptr
            record[ptr]=0
            ptr=ptr.next
        return None