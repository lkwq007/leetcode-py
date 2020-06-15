# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root is None:
            return -1
        min_val=root.val
        self.min=-1
        def dfs(node):
            if node.val>min_val:
                self.min=node.val if self.min<0 else min(node.val,self.min)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        return self.min