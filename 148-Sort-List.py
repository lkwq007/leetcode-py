# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # TLE
        def quick_sort(lst):
            if lst is None or lst.next is None:
                return lst,lst
            smaller_head=ListNode(0)
            smaller_ptr=smaller_head
            first=lst
            current=first.val
            ptr=lst.next
            prev=first
            ptr=lst
            while ptr:
                if ptr.val<current:
                    next=ptr.next
                    ptr.next=None
                    smaller_ptr.next=ptr
                    smaller_ptr=ptr
                    prev.next=next
                    ptr=next
                else:
                    prev=ptr
                    ptr=ptr.next
            if smaller_head.next:
                left_head,left_tail=quick_sort(smaller_head.next)
                left_tail.next=first
            else:
                left_head=first
            if first.next:
                right_head,right_tail=quick_sort(first.next)
                first.next=right_head
            else:
                right_tail=first
            return left_head,right_tail
        return quick_sort(head)[0]
                    
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge_sort(lst):
            if lst is None or lst.next is None:
                return lst
            first=lst
            second=lst
            prev=None
            while first and second and second.next:
                prev=first
                first=first.next
                second=second.next.next
            second=first
            prev.next=None
            first=merge_sort(lst)
            second=merge_sort(second)
            dummy=ListNode(0)
            ptr=dummy
            while first and second:
                if first.val<second.val:
                    ptr.next=first
                    first=first.next
                else:
                    ptr.next=second
                    second=second.next
                ptr=ptr.next
            if second:
                first=second
            ptr.next=first
            return dummy.next
        return merge_sort(head)