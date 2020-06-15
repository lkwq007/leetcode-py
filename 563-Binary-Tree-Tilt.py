# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.tilt=0
        def dfs(node):
            if node is None:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            self.tilt+=abs(left-right)
            return left+right+node.val
        dfs(root)
        return self.tilt