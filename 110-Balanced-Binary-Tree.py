# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag=True
        def dfs(node:TreeNode):
            if node is None:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            a=max(left,right)
            b=min(left,right)
            if a>b+1:
                self.flag=False
            return a+1
        dfs(root)
        return self.flag
            