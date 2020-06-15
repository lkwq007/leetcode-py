# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max=0
        if root is None:
            return 0
        def depth(node):
            if node is None:
                return 0
            l=depth(node.left)
            r=depth(node.right)
            self.max=max(self.max,l+r)
            return 1+max(l,r)
        depth(root)
        return self.max