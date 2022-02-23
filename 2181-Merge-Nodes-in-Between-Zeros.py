# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        acc=0
        ptr=head.next
        last=None
        ret=None
        while ptr:
            if ptr.val==0:
                if ret is None:
                    ret=ptr
                    last=ptr
                else:
                    last.next=ptr
                    last=ptr
                ptr.val=acc
                acc=0
            else:
                acc+=ptr.val
            ptr=ptr.next
        return ret

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        acc=0
        ptr=head.next
        last=head
        ret=None
        while ptr:
            acc+=ptr.val
            if ptr.val==0:
                ptr.val=acc
                acc=0
                if ret is None:
                    ret=ptr
                last.next=ptr
                last=ptr
            ptr=ptr.next
        return ret