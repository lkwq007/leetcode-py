# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first=-1
        last=-1
        cnt=0
        idx=0
        prev=None
        minval=1000000
        maxval=1
        while head!=None:
            if prev and head.next:
                if prev.val<head.val and head.next.val<head.val or prev.val>head.val and head.next.val>head.val:
                    cnt+=1
                    if last!=-1:
                        minval=min(idx-last,minval)
                    last=idx
                    if first!=-1:
                        maxval=idx-first
                    else:
                        first=idx
            idx+=1
            prev=head
            head=head.next
        if cnt<2:
            return [-1,-1]
        return [minval,maxval]
