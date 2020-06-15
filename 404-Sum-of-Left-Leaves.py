# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        stack=[(root,False)]
        acc=0
        while stack:
            node,left=stack.pop()
            if node.left==None and node.right==None and left:
                acc+=node.val
            if node.left:
                stack.append((node.left,True))
            if node.right:
                stack.append((node.right,False))
        return acc