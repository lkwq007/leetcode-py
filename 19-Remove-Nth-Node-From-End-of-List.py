# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # one pass
        dummy_head=ListNode(0)
        dummy_head.next=head
        count=0
        nth=dummy_head
        ptr=head
        while ptr is not None:
            if count>=n:
                nth=nth.next
            count+=1
            ptr=ptr.next
        tmp=nth.next
        nth.next=tmp.next
        return dummy_head.next

# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         dummy_head=ListNode(0)
#         dummy_head.next=head
#         ptr=head
#         # two pass
#         count=0
#         while ptr is not None:
#             count+=1
#             ptr=ptr.next
#         mark=count-n
#         count=0
#         ptr=head
#         last=dummy_head
#         while ptr is not None:
#             if count==mark:
#                 last.next=ptr.next
#                 break
#             else:
#                 last=ptr
#                 ptr=ptr.next
#                 count+=1
#         return dummy_head.next