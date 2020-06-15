"""
# Definition for a Node.

"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ret=[]
        if root is None:
            return ret
        stack=[root]
        while stack:
            node=stack.pop()
            ret.append(node.val)
            if node.children:
                for item in reversed(node.children):
                    if item:
                        stack.append(item)
        return ret