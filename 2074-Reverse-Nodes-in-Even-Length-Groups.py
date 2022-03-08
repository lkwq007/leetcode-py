# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last=head
        ptr=head.next
        target=2
        cnt=0
        while ptr:
            cnt+=1
            if cnt==target or ptr.next is None:
                if cnt%2==0:
                    next_group=ptr.next
                    ptr=last.next
                    prev=next_group
                    while ptr.next!=next_group:
                        next=ptr.next
                        ptr.next=prev
                        prev=ptr
                        ptr=next
                    ptr.next=prev
                    tmp=ptr
                    ptr=last.next
                    last.next=tmp
                last=ptr
                target+=1
                cnt=0
            ptr=ptr.next
        return head
        