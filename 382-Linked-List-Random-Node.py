# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
import random
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head=head
        self.ptr=head
        self.queue=deque([],maxlen=16)
        self.notfull=False
        for i in range(16):
            if self.ptr:
                self.queue.append(self.ptr.val)
                self.ptr=self.ptr.next
            else:
                self.notfull=True
                break
    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        idx=random.randrange(0,len(self.queue))
        if self.notfull:
            return self.queue[idx]
        ret=self.queue[idx]
        self.queue[idx]=self.queue[0]
        self.queue.popleft()
        if self.ptr:
            self.queue.append(self.ptr.val)
            self.ptr=self.ptr.next
        elif len(self.queue)<1:
            self.ptr=self.head
        return ret


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()