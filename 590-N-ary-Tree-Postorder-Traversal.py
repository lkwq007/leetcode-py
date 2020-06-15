"""
# Definition for a Node.

"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret=[]
        if root is None:
            return ret
        stack_val=[]
        stack_node=[root]
        while stack_node:
            node=stack_node.pop()
            if type(node)==int:
                ret.append(node)
                continue
            stack_node.append(node.val)
            if node.children:
                for item in reversed(node.children):
                    if item:
                        stack_node.append(item)
        return ret



class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret=[]
        if root is None:
            return ret
        def post(node):
            if node.children:
                for item in node.children:
                    if item:
                        post(item)
            ret.append(node.val)
        post(root)
        return ret