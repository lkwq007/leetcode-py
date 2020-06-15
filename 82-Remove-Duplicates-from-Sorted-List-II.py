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
        current=None
        while head:
            if head.next is not None and head.val==head.next.val:
                current=head.val
                last.next=head.next.next
                head=head.next
            elif current==head.val:
                last.next=head.next
                head=head.next
            else:
                last=head
                head=head.next
        return dummy_head.next

def deleteDuplicates( head: ListNode) -> ListNode:
    dummy_head=ListNode(None)
    dummy_head.next=head
    last=dummy_head
    current=None
    while head:
        if head.next is not None and head.val==head.next.val:
            current=head.val
            last.next=head.next.next
            head=head.next
        elif current==head.val:
            last.next=head.next
            head=head.next
        else:
            last=head
            head=head.next
    return dummy_head.next

print(deleteDuplicates(ListNode(1)))
lst=ListNode(1)
lst.next=ListNode(1)
print(deleteDuplicates(lst))
