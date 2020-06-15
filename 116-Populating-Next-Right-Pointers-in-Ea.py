"""
# Definition for a Node.

"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def connect_node(node,right):
            # root is a perfect binary tree
            if node is None:
                return
            node.next=right
            rightmost=right
            if right:
                rightmost=right.left if right.left else right.right
            if node.left:
                if node.right:
                    connect_node(node.left,node.right)
                else:
                    connect_node(node.left,rightmost)
            if node.right:
                connect_node(node.right,rightmost)
        connect_node(root,None)
        return root