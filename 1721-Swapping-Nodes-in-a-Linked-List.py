# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # two pass
        first=None
        ptr=head
        cnt=0
        while ptr:
            cnt+=1
            if cnt==k:
                first=ptr
            ptr=ptr.next
        total=cnt
        cnt=0
        ptr=head
        while ptr:
            cnt+=1
            if cnt==total-k+1:
                ptr.val,first.val=first.val,ptr.val
                break
            ptr=ptr.next
        return head

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # two pointer
        node_k=None
        ptr=head
        ptr2=head
        cnt=0
        while ptr:
            cnt+=1
            if cnt==k:
                node_k=ptr
                ptr2=head
            ptr=ptr.next
            ptr2=ptr2.next
        node_k.val,ptr2.val=ptr2.val,node_k.val
        return head