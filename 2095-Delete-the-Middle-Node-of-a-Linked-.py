# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        ptr=head
        slow=head
        prev=None
        while ptr and ptr.next:
            ptr=ptr.next.next
            prev=slow
            slow=slow.next
        prev.next=slow.next
        return head
