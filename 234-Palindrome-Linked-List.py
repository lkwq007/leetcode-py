# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #  O(n) time and O(1) space
        if head is None or head.next is None:
            return True
        count=0
        dummy=ListNode(0)
        dummy.next=head
        ptr=head
        while ptr:
            count+=1
            ptr=ptr.next
        total=count
        ptr=head
        middle_cnt=total//2
        while ptr:
            count+=1
            if count==middle_cnt:
                break
        if count%2==0:
            middle=ptr
        else:
            middle=ptr.next
        
        buffer=[]
        ptr=head
        while ptr:
            buffer.append(ptr)
            ptr=ptr.next
        total=len(buffer)
        for i in range(0,total//2):
            if buffer[i].val!=buffer[total-i-1].val:
                return False
        return True

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        buffer=[]
        ptr=head
        while ptr:
            buffer.append(ptr)
            ptr=ptr.next
        total=len(buffer)
        for i in range(0,total//2):
            if buffer[i].val!=buffer[total-i-1].val:
                return False
        return True