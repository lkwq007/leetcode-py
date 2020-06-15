"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def flat(node):
            ptr=node
            prev=node
            while ptr:
                prev=ptr
                if ptr.child:
                    next=ptr.next
                    child_tail=flat(ptr.child)
                    ptr.next=ptr.child
                    ptr.child.prev=ptr
                    ptr.child=None
                    child_tail.next=next
                    if next:
                        next.prev=child_tail
                    ptr=child_tail
                else:
                    ptr=ptr.next
            return prev
        flat(head)
        return head
