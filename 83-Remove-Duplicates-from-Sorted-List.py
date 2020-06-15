# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head=ListNode(None)
        dummy_head.next=head
        last=dummy_head
        while head is not None:
            if head.val==last.val:
                head=head.next
            else:
                last.next=head
                last=head
                head=head.next
        last.next=head
        return dummy_head.next