# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pass
        group=1
        cnt=0
        ptr=head
        last=None
        prev=None
        while ptr:
            cnt+=1
            if group&1:
                last=ptr
                ptr=ptr.next
                if cnt==group:
                    group+=1
                    cnt=0
            else:
                next=ptr.next
                if cnt==1:
                    tail=ptr
                else:
                    ptr.next=prev
                prev=ptr
                ptr=next
                if cnt==group:
                    tail.next=ptr
                    last.next=prev
                    cnt=0
                    group+=1
                if ptr==None:
                    if cnt&1:
                        tmp=prev
                        prev=None
        return head
        