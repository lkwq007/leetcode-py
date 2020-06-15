"""
# Definition for a Node.

"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        map=dict()
        ptr=head
        dummy_head=Node(0)
        last=dummy_head
        map[None]=None
        while ptr:
            node=Node(ptr.val,random=ptr.random)
            map[ptr]=node
            last.next=node
            last=last.next
            ptr=ptr.next
        ptr=dummy_head.next
        while ptr:
            ptr.random=map[ptr.random]
            ptr=ptr.next
        return dummy_head.next
