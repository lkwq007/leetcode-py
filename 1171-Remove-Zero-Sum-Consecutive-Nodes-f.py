# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        record={}
        dummy=ListNode(0)
        dummy.next=head
        record[0]=[dummy]
        ptr=head
        acc=0
        while ptr:
            acc+=ptr.val
            if acc in record:
                for item in record[acc]:
                    item.next=ptr.next
                record[acc].append(ptr)
            else:
                record[acc]=[ptr]
            ptr=ptr.next
        return dummy.next

