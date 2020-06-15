# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        tmp=root.right
        root.right=root.left
        root.left=tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root