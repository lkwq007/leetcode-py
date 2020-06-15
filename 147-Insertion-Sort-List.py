# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        ptr=head.next
        last=head
        dummy_head=ListNode(0)
        dummy_head.next=head
        while ptr is not None:
            if ptr.val>=last.val:
                last=ptr
                ptr=ptr.next
            else:
                next=ptr.next
                cursor=dummy_head.next
                cursor_last=dummy_head
                while cursor!=last:
                    if cursor.val>ptr.val:
                        break
                    else:
                        cursor=cursor.next
                        cursor_last=cursor_last.next
                cursor_last.next=ptr
                tmp=ptr.next
                ptr.next=cursor
                last.next=tmp
                ptr=tmp
        return dummy_head.next