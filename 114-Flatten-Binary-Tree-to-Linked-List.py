# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        stack=[root]
        dummy=TreeNode(0)
        last=dummy
        while stack:
            node=stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            last.right=node
            node.left=None
            last=node