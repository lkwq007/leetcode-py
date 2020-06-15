# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head=ListNode(0)
        dummy_head.next=head
        last=dummy_head
        first=head
        while True:
            if first is None or first.next is None:
                break
            second=first.next
            third=second.next
            last.next=second
            second.next=first
            first.next=third
            first=third
            last=first
        return dummy_head.next